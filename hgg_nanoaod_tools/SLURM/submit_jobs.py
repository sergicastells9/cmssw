""" Simple script to submit on SLURM (Tier3 PSI) to produce custom NanoAODs from MiniAODs with Lindsey's branch.
Flags:
    - datasets: path to a JSON file in the format {"dataset": [file1, file2, etc.]}
    - output-dir: inside it, directories for each "dataset" key in the JSON file are created, with the produced NanoAODs inside them
    - sample: either data or mc
    - validate: produce only the cmsRun config files without submitting the jobs

The script creates three subdirectories in the current directory: 
    - config: contains the cmsRun config files created
    - jobs: contains the produced SLURM config files, to be submitted with sbatch
    - logs: stores the *.out and *.err files for each job

Example:
$ python3 submit_jobs.py --datasets /work/gallim/CMSSW/CMSSW_10_6_26/src/hgg_nanoaod_tools/filefetcher/nanoaod_production_data.json --output-dir /work/gallim/CMSSW/CMSSW_10_6_26/src/hgg_nanoaod_tools/SLURM/output --sample data
"""
import argparse
import json
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
            description=""
            )

    parser.add_argument(
        "--datasets",
        required=True,
        type=str,
        help="JSON file containing the datasets we want to convert to NanoAOD"
    )
    
    parser.add_argument(
        "--output-dir",
        required=True,
        type=str,
        help="Path to output directory"
    )

    parser.add_argument(
        "--sample",
        type=str,
        required=True,
        choices=["data", "mc"],
        help="Data or MC"
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        default=False,
        help="Print cmsRun config files without submitting the jobs"
    )

    return parser.parse_args()


def mkdir(dr):
    '''make a directory (dr) if it doesn't exist'''
    if not os.path.exists(dr):
        os.mkdir(dr)


base_cmd = "cmsDriver.py RECO --customise Configuration/DataProcessing/Utils.addMonitoring --eventcontent NANOAOD --datatier NANOAOD --era Run2_2017,run2_nanoAOD_106Xv1 --scenario pp --step NANO --no_exec --nThreads 16"
custom_options = "--filein {} --fileout {} --python_filename {}"
commands = {
        "data": " ".join([base_cmd, custom_options, "--data --conditions 106X_dataRun2_v32"]),
        "mc": " ".join([base_cmd, custom_options, "--mc --conditions 106X_mc2017_realistic_v8"])
        }


def main(args):
    with open(args.datasets) as f:
        # dictionary in the form {"sample": [file1, file2, ...]}
        datasets_dict = json.load(f)

    curr_dir = os.getcwd()
    # create job directory
    job_directory = os.path.join(curr_dir, "jobs")
    mkdir(job_directory)

    # create log directory
    log_dir = os.path.join(curr_dir, "logs")
    mkdir(log_dir)

    # create config files directory
    conf_dir = os.path.join(curr_dir, "config")
    mkdir(conf_dir)

    for dataset_name, files in datasets_dict.items():
        output_dir = os.path.join(args.output_dir, dataset_name)
        mkdir(output_dir)

        for root_file in files:
            filein = root_file
            simple_name_in = root_file.split("/")[-1]
            simple_name_out = simple_name_in.split(".")[0] + "_NanoAOD." + simple_name_in.split(".")[1]
            fileout = os.path.join(output_dir, simple_name_out)

            print("simple_name_in: {}".format(simple_name_in))
            print("simple_name_out: {}".format(simple_name_out))
            print("fileout: {}".format(fileout))

            unique_job_id = "{}_{}".format(dataset_name, simple_name_in.split(".")[0])
            job_file = os.path.join(job_directory, "{}.job".format(unique_job_id))
            conf_file = os.path.join(conf_dir, "{}_cfg.py".format(unique_job_id))
            command = commands[args.sample].format(filein, fileout, conf_file)
            # create config file
            os.system(command)

            if not args.validate:
                print("Creating and submitting job")
                with open(job_file, "w") as fh:
                    fh.writelines("#!/bin/bash\n")
                    fh.writelines("#SBATCH --job-name={}.job\n".format(unique_job_id))
                    fh.writelines("#SBATCH --output={}/{}.out\n".format(log_dir, unique_job_id))
                    fh.writelines("#SBATCH --error={}/{}.err\n".format(log_dir, unique_job_id))
                    fh.writelines("#SBATCH --mem=5G\n")
                    fh.writelines("#SBATCH --cpus-per-task=2\n")
                    fh.writelines("cmsRun {}".format(conf_file))

                os.system("sbatch {}".format(job_file))



if __name__ == "__main__":
    args = parse_arguments()
    main(args)
