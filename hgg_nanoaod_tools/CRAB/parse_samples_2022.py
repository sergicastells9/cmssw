import json
import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line options parser")
    parser.add_argument("-if", "--inputFile", help="File to JSONize", type=str, required=True)
    args = parser.parse_args()

    data = {"Data": {}}
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []

    xrd = "root://xrootd-cms.infn.it/"

    with open(args.inputFile, "r") as file:
        for line in file:
            for era_letter, era_list in zip(["A","B","C","D","E","F","G"], [A,B,C,D,E,F,G]):
                if era_letter in line:
                    era_list.append(line.strip())

    for era_letter, era_list in zip(["A","B","C","D","E","F","G"], [A,B,C,D,E,F,G]):
        data["Data"].update({f"Run2022{era_letter}": {"files": era_list}})
        data["Data"][f"Run2022{era_letter}"]["GT"] = "130X_dataRun3_v2"
        if era_letter in ["B", "G"]:
            data["Data"][f"Run2022{era_letter}"]["era"] = "run3_nanoAOD_130Xv2"
        else:
             data["Data"][f"Run2022{era_letter}"]["era"] = "run3_nanoAOD_130Xv1"

    with open("2022_Data_Datasets.json", "w+") as file:
        json.dump(data, file, indent=2)
