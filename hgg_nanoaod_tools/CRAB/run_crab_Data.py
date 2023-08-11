# Run this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh

import subprocess
import os
import shutil
import argparse
import json
try:
    import CRABClient
    from CRABAPI.RawCommand import crabCommand
except:
    print("\n!!!!!\nRun this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh\n!!!!!\n")
    raise


def generateSubmit(dataset, cfg):
    submit = f"""
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	 =  'MNConversion_{cfg}_data'
config.General.transferLogs	 =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName          = '{cfg}_data_cfg.py'
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
config.Data.outLFNDirBase        = '/store/user/castells/outputs/MNConversion_{cfg}/'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_CERNBOX'
    """

    with open(f"{cfg}_data_submit.py", "w") as file:
        file.write(submit)

def run_crab(args):
    # Remove any previous CRAB submission directories
    if(os.path.exists("./MNConversion_crab/")):
        shutil.rmtree("./MNConversion_crab/")
        print("Removed old CRAB submission directories.")

    # Load in datasets from json
    with open("Data_Datasets.json") as file:
        datasets = json.load(file)

    # Generate cfg with cmsDriver for each dataset and submit to crab
    for year in ["2018A", "2018B", "2018C", "2018D"]:
        for dataset in datasets["Data"][f"{year}"]["files"]:
            GT = datasets["Data"][f"{year}"]["GT"]
            era = datasets["Data"][f"{year}"]["era"]
            cfg = year

            # Generate cfg
            subprocess.run(["cmsDriver.py", "--python_filename", f"{cfg}_data_cfg.py", "--eventcontent", "NANOAODSIM", "--customise", "Configuration/DataProcessing/Utils.addMonitoring", "--datatier", "NANOAODSIM", "--fileout", f"file:{cfg}_data.root", "--conditions", f"{GT}", "--step", "NANO", "--filein", f"dbs:{dataset}", "--era", f"Run2_{year[:-1]},{era}", "--mc", "-n", "-1", "--no_exec"])

            if not args.gen:
                # Generate submit script and submit to CRAB
                generateSubmit(dataset, cfg)
                subprocess.run(f"crab submit -c {cfg}_data_submit.py", shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specifies what samples to convert from miniAOD to nanoAOD.")
    parser.add_argument("-gen", "--gen-only", dest="gen", action="store_true", help="Only generate config file without submitting.")
    args = parser.parse_args()

    run_crab(args)
