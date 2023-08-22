# Run this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh

import subprocess
import os
import shutil
import argparse
import json
from tqdm import tqdm
from typing import List
try:
    import CRABClient
    from CRABAPI.RawCommand import crabCommand
except:
    print("\n!!!!!\nRun this first: source /cvmfs/cms.cern.ch/common/crab-setup.sh\n!!!!!\n")
    raise


def generateCfg(
    f: str,
    cfg_path: str,
    original_dataset: str,
    files_per_job: int = 6
) -> List:

    submit = []
    dataset = set()
    new_cfgs = []
    new_subs = []
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
    
    if not os.path.exists("./subs/"):
        os.mkdir("./subs/")

    for cfg in tqdm(range(int(len(dataset) / files_per_job) + 1)):
        new_path = f"./cfgs/{cfg_path}_{cfg}.py"
        new_cfgs.append(new_path)

        new_sub = generateSubmit(
            original_dataset,
            new_path,
            f"MNConversion_{new_path.replace('.py', '').replace('./cfgs/','').replace('_cfg','')}"
        )
        new_subs.append(new_sub)

        with open(new_path, "w") as fout:
            for line in submit[:cut]:
                fout.write(line)
            
            for data in dataset[cfg * files_per_job : (cfg + 1) * files_per_job if cfg < len(dataset) - files_per_job else -1]:
                fout.write(f"\t{data},\n")
            
            for line in submit[cut:]:
                if f"fileName = cms.untracked.string('file:{cfg_path.replace('_cfg','')}.root')," in line:
                    line = line.replace(f"{cfg_path.replace('_cfg','')}.root", f"{cfg_path.replace('_cfg','')}_{cfg}.root")
                fout.write(line)

    print(f"Generated new cfg and submit files for {f}")
    return new_subs


def generateSubmit(
    dataset: str,
    cfg: str,
    requestName: str
) -> str:

    submit = f"""
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	     =  '{requestName}'
config.General.transferLogs	     =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'
config.JobType.numCores          = 8
config.JobType.maxMemoryMB       = 20000

# Name of the CMSSW configuration file
config.JobType.psetName          = '{cfg}'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '{dataset}'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'FileBased'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob         = 3
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/store/user/castells/outputs/{requestName}'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_CERNBOX'
    """

    path = f"./subs/{cfg.replace('_cfg','').replace('./cfgs/','').replace('.py','')}_submit.py"
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
            path = f"{cfg}_data_cfg.py"
            subprocess.run(["cmsDriver.py", "--python_filename", path, "--eventcontent", "NANOAOD", "--customise", "Configuration/DataProcessing/Utils.addMonitoring", "--datatier", "NANOAOD", "--fileout", f"file:{cfg}_data.root", "--conditions", f"{GT}", "--step", "NANO", "--filein", f"dbs:{dataset}", "--era", f"Run2_{year[:-1]},{era}", "--data", "-n", "-1", "--no_exec", "--nThreads", "8"])

            # Generate new cfgs and submit files
            # new_subs = generateCfg(path, path.replace(".py", ""), dataset, 5)
            new_subs = []
            new_subs.append(
                generateSubmit(dataset, path, path.replace(".py", ""))
            )

            if not args.gen:
                # Submit to CRAB
                for sub in new_subs:
                    subprocess.run(f"crab submit -c {sub}", shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specifies what samples to convert from miniAOD to nanoAOD.")
    parser.add_argument("-gen", "--gen-only", dest="gen", action="store_true", help="Only generate config file without submitting.")
    args = parser.parse_args()

    run_crab(args)
