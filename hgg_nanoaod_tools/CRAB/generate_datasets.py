import argparse
import json
import subprocess

class splitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(
            namespace,
            self.dest,
            values.split(",")
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line options parser")
    parser.add_argument("-d", "--dataset", help="Dataset(s) to query", action=splitArgs, type=str, required=True)
    args = parser.parse_args()

    dbs_out = []
    for dataset in args.dataset:
        dbs_out.extend(
            subprocess.run([
                f'dasgoclient -query "file dataset={dataset}"'],
                shell = True,
                stdout = subprocess.PIPE,
                universal_newlines = True).stdout.split("\n")[:-1]
        )
    
    with open("data_2018.txt", "w") as f:
        for fname in dbs_out:
            f.write(fname)
            f.write("\n")
    
    print("Finished querying datasets!")