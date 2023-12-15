import os
from pathlib import Path
import json
import argparse
import subprocess

"""
Make sure to have a GRID proxy and to load brilcalc first:
voms-proxy-init --voms cms
source /cvmfs/cms-bril.cern.ch/cms-lumi-pog/brilws-docker/brilws-env
export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda3/bin:$PATH

Example:
python3 lumi_from_das.py -d /EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD,/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD,/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD,/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD -of test.txt
"""

class splitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(
            namespace,
            self.dest,
            values.split(",")
        )

parser = argparse.ArgumentParser(description="Command line options parser")
parser.add_argument("-d", "--dataset", help="Dataset(s) to query", action=splitArgs, type=str, required=True)
parser.add_argument("-of", "--outputFile", help="Output file", type=str, required=True)
args = parser.parse_args()

dbs_out = []
for dataset in args.dataset:
    dbs_out.extend(
        subprocess.run([
            f'dasgoclient -query "run lumi dataset={dataset}"'],
            shell = True,
            stdout = subprocess.PIPE,
            universal_newlines = True).stdout.split("\n")[:-1]
    )

d = {}
for line in dbs_out:
    l = line.split(" ")
    lumi = sorted([int(x) for x in l[1].replace("\n","").strip("[").strip("]").split(",")])

    new = []
    mx = lumi[0]
    curr = []
    for idx in range(len(lumi)):
        curr = [mx, lumi[idx]]
        if idx == len(lumi)-1:
            if len(lumi) > 1:
                new.append(curr)
            if len(lumi) == 1:
                new.append([lumi[0], lumi[0]])
            continue
        elif lumi[idx+1] - lumi[idx] > 1:
            new.append(curr)
            mx = lumi[idx+1]

    d.update({l[0]: new})

with open(args.outputFile, "w") as f:
    json.dump(d, f)
    print("Dumped run/lumi JSON")

print(
    subprocess.run([
        "brilcalc",
        "lumi",
        "--normtag",
        "/cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json",
        "-u",
        "/pb",
        "-i",
        args.outputFile
    ],
    stdout = subprocess.PIPE,
    universal_newlines = True).stdout
)
