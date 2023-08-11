import json
import sys

A = []
B = []
C = []
D = []

xrd = "root://xrootd-cms.infn.it/"

with open("data_2018.txt", "r") as file:
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

for str, obj in zip(["A","B","C","D"], [A,B,C,D]):
# for str, obj in zip(["D"], [D]):
    data["Data"][f"2018{str}"]["files"].append(obj)
    data["Data"][f"2018{str}"]["GT"].append("106X_dataRun2_v36")
    data["Data"][f"2018{str}"]["era"].append("run2_nanoAOD_106Xv1")


with open("Data_Datasets.json", "w+") as file:
    json.dump(data, file)
