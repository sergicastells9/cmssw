# Run this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh

import subprocess
import os
import shutil
import argparse
import json
from tdqm import tdqm
try:
    import CRABClient
    from CRABAPI.RawCommand import crabCommand
except:
    print("\n!!!!!\nRun this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh\n!!!!!\n")
    raise


def generateCfg(
    f: str,
    cfg_path: str,
    files_per_job: int = 6
) -> List:

    submit = []
    dataset = set()
    new_cfgs = []
    cut = -1
    count = 0

    with open(f, "r") as fin:
        files = False
        lines = fin.readlines()

        for idx, line in enumerate(lines):
            if ") )," in line:
                files = False

            if files:
                dataset.add(
                    line.strip().replace(",", "")
                )
                count += 1
            elif not files:
                submit.append(line)
            
            if "fileNames = cms.untracked.vstring(" in line:
                cut = idx + 1
                files = True

    print("Loaded samples and cfg file")
    dataset = list(dataset)

    if not os.path.exists("./cfgs/"):
        os.mkdir("./cfgs/")

    for cfg in tqdm(range(int(len(dataset) / files_per_job) + 1)):
        new_path = f"./cfgs/{cfg_path}_{cfg}.py"
        new_cfgs.append(new_path)

        with open(new_path, "w") as fout:
            for line in submit[:cut]:
                fout.write(line)
            
            for data in dataset[cfg * files_per_job : (cfg + 1) * files_per_job if cfg < len(dataset) - files_per_job else -1]:
                fout.write(f"\t{data},\n")
            
            for line in submit[cut:]:
                fout.write(line)

    print(f"Generated new cfg files for {f}")
    return new_cfgs


def generateSubmit(dataset, cfg):
    submit = f"""
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	     =  'MNConversion_{cfg}_data'
config.General.transferLogs	     =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'
config.JobType.numCores          = 8
config.JobType.maxMemoryMB       = 20000

# Name of the CMSSW configuration file
config.JobType.psetName          = '{cfg}_data_cfg.py'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '{dataset}'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob         = 30
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/store/user/castells/outputs/MNConversion_{cfg}/'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_CERNBOX'
    """

    path = f"{cfg}_data_submit.py"
    with open(path, "w") as file:
        file.write(submit)
    
    return path

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
            subprocess.run(["cmsDriver.py", "--python_filename", f"{cfg}_data_cfg.py", "--eventcontent", "NANOAOD", "--customise", "Configuration/DataProcessing/Utils.addMonitoring", "--datatier", "NANOAOD", "--fileout", f"file:{cfg}_data.root", "--conditions", f"{GT}", "--step", "NANO", "--filein", f"dbs:{dataset}", "--era", f"Run2_{year[:-1]},{era}", "--data", "-n", "-1", "--no_exec", "--nThreads", "8"])

            # Generate submit file
            path = generateSubmit(dataset, cfg)
            new_cfgs = generateCfg(path, path.replace(".py", ""), 8)

            if not args.gen:
                # Submit to CRAB
                subprocess.run(f"crab submit -c {cfg}_data_submit.py", shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specifies what samples to convert from miniAOD to nanoAOD.")
    parser.add_argument("-gen", "--gen-only", dest="gen", action="store_true", help="Only generate config file without submitting.")
    args = parser.parse_args()

    run_crab(args)
