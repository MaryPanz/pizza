import sys
from tabulate import tabulate
import csv
import pandas as pd


# 1 cmd line arg
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file!")
    sys.exit(1)
else:
    try:
        with open(sys.argv[1]) as file:
            df = pd.read_csv(sys.argv[1])
            table = tabulate(df, headers = "keys", showindex = "never", tablefmt = "grid")
            print(table)
    except FileNotFoundError:
        print("File does not exist!")
