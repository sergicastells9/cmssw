import json
import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line options parser")
    parser.add_argument("-if", "--inputFile", help="File to JSONize", type=str, required=True)
    args = parser.parse_args()

    A = []
    B = []
    C = []
    D = []

    xrd = "root://xrootd-cms.infn.it/"

    with open(args.inputFile, "r") as file:
        for line in file:
            if "Run2018A" in line:
                A.append(line.strip())
            if "Run2018B" in line:
                B.append(line.strip())
            if "Run2018C" in line:
                C.append(line.strip())
            if "Run2018D" in line:
                D.append(line.strip())

    json_string = '{ "Data" : { '
    for era in ["A","B","C","D"]:
    # for era in ["D"]:
        if era in "ABC":
            json_string += '"2018' + era + '" : { "files" : [], "GT" : [], "era" : [] },'
        else:
            json_string += '"2018' + era + '" : { "files" : [], "GT" : [], "era" : [] } } }'

    data = json.loads(json_string)

    for letter, obj in zip(["A","B","C","D"], [A,B,C,D]):
    # for str, obj in zip(["D"], [D]):
        data["Data"][f"2018{letter}"]["files"].extend(obj)
        data["Data"][f"2018{letter}"]["GT"] = "106X_dataRun2_v33"
        data["Data"][f"2018{letter}"]["era"] = "run2_nanoAOD_106Xv1"


    with open("Data_Datasets.json", "w+") as file:
        json.dump(data, file, indent=2)