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

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
# here it create a list of records and it three different records that are stored together.
records = [
    {
        "source_ip": "10.0.0.5",
        "failed_logins": 12,
        "total_attempts": 400
    },
    {
        "source_ip": "192.168.1.1",
        "failed_logins": 300,
        "total_attempts": 400
    },
    {
        "source_ip": "172.16.0.1",
        "failed_logins": 380,
        "total_attempts": 400
    }
]


#At this point it checks the record and decide its status which means checking the percentage and deciding the result.
def check_record(record):
    """Checks failed logins and returns the status."""

    percent = (record["failed_logins"] / record["total_attempts"]) * 100

    if percent >= 90:
        status = "OVER LIMIT"
    elif percent >= 75:
        status = "WARNING"
    else:
        status = "OK"

    return percent, status


# Print the report for each record
def print_report(record):
    """Prints the cyber security report."""

    percent, status = check_record(record)

    print("------------------------------")
    print("CYBER SECURITY REPORT")
    print("------------------------------")
    print("Source IP:", record["source_ip"])
    print("Failed Logins:", record["failed_logins"])
    print("Total Attempts:", record["total_attempts"])
    print("Percentage:", round(percent, 2), "%")
    print("Status:", status)
    print("------------------------------")


# Go through each record and print its report and repeats the report for every record in list
for record in records:
    print_report(record)