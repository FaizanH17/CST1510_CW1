"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = None   # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case

import pandas as pd     # this imports pandas to work with data and tables
import matplotlib.pyplot as plt     # matplotlib is used to create charts
df = pd.read_csv("it_storage.csv")  # here we load the csv file into the dataframe
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100 
df["status"] = df["percent"].apply( 
    lambda x: "OVERLIMIT" if x > 90 else "WARNING" if x >= 75 else "OK" # checks the percentage and give every row a status
)
print(df) # displays the whole dataframe
print("\nServers that need attention")
print(df[df["status"]!= "OK"])
# this displays rows where attention is needed.