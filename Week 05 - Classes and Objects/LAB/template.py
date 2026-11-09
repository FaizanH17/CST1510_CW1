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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

from py_compile import main


records = []   # replace with your code


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
# created a class called record
class Record: # this sets up the information for each record when made
    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts


# right here it creates two records r1 and r2
r1 = Record("10.0.0.5", 12, 400)
r2 = Record("192.168.1.1", 5, 200)


# here this is where it Prints first report
print("==============================")
print("CYBER SECURITY REPORT")
print("==============================")
print("Source IP:", r1.source_ip)
print("Failed Logins:", r1.failed_logins)
print("Total Attempts:", r1.total_attempts)

#  and here it prints the second report
print("==============================")
print("CYBER SECURITY REPORT")
print("==============================")
print("Source IP:", r2.source_ip)
print("Failed Logins:", r2.failed_logins)
print("Total Attempts:", r2.total_attempts)