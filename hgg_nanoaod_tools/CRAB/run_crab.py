# Run this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh

import subprocess
import os
import shutil
import argparse
import json
import CRABClient
from CRABAPI.RawCommand import crabCommand

def generateSubmit(dataset, cfg, year):
    submit = f"""
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	 =  'MNConversion_{cfg}_{year}'
config.General.transferLogs	 =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName          = '{cfg}_{year}_cfg.py'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '{dataset}'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob          = 30
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/store/user/castells/outputs/MNConversion_{year}/'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_CERNBOX'
    """

    with open(f"{cfg}_{year}_submit.py", "w") as file:
        file.write(submit)

def run_crab():
    # Remove any previous CRAB submission directories
    if(os.path.exists("./MNConversion_crab/")):
        shutil.rmtree("./MNConversion_crab/")
        print("Removed old CRAB submission directories.")

    # Load in datasets from json
    with open("MC_Datasets.json") as file:
        datasets = json.load(file)

    # Generate cfg with cmsDriver for each dataset and submit to crab
    for mc in ["MC_Signal", "MC_Background"]:
        if args.all:
            pass
        elif args.signal and mc == "MC_Background":
            continue
        elif args.background and mc == "MC_Signal":
            continue

        for year in range(2016,2019,1):
            for dataset in datasets[f"{mc}"][f"{year}"]["files"]:
                GT = datasets[f"{mc}"][f"{year}"]["GT"]
                era = datasets[f"{mc}"][f"{year}"]["era"]
                cfg = dataset.split("/")[1]

                # Generate cfg
                subprocess.run(["cmsDriver.py", "--python_filename", f"{cfg}_{year}_cfg.py", "--eventcontent", "NANOAODSIM", "--customise", "Configuration/DataProcessing/Utils.addMonitoring", "--datatier", "NANOAODSIM", "--fileout", f"file:{cfg}_{year}.root", "--conditions", f"{GT}", "--step", "NANO", "--filein", f"dbs:{dataset}", "--era", f"Run2_{year},{era}", "--mc", "-n", "-1", "--no_exec"])

                # Generate submit script and submit to CRAB
                generateSubmit(dataset, cfg, year)
                subprocess.run(f"crab submit -c {cfg}_{year}_submit.py", shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specifies what samples to convert from miniAOD to nanoAOD.")
    sample_parser = parser.add_mutually_exclusive_group(required=True)
    sample_parser.add_argument('--signal', dest='signal', action='store_true', help='Run over only signals.')
    sample_parser.add_argument('--background', dest='background', action='store_true', help='Run over only backgrounds.')
    sample_parser.add_argument('--all', dest='all', action='store_true', help='Run over all samples.')
    args = parser.parse_args()

    run_crab()

