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
class Record:
    """ Store a  servers hostname and storage information. """
    def __init__(self, hostname, gb_used, gb_total):
        """ store the servers detatils"""
        self.hostname = hostname
        self.gb_used = gb_used
        self.gb_total = gb_total
    def percent(self):
        """ calculate the percentage of storage used """
        return (self.gb_used / self.gb_total) * 100
    def status(self):
        """ return the status of the server based on storage used """
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"
    def summary(self):
        """ return a summary of the server's storage information """
        return f"{self.hostname}: {self.gb_used}GB used of {self.gb_total}GB ({self.percent():.2f}%) - {self.status()}"
    
    def Record_load_records(path):
        """ load records from a file and return a list of Record objects """
        records = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                hostname, gb_used, gb_total = line.split(',')
                record = Record(
                    hostname,
                    float(gb_used),
                    float(gb_total)
                )
                records.append(record)
        return records
    def main():
        r1 = Record("srv-01", 87.0, 100.0)
        r2 = Record("srv-02", 95.0, 100.0)

        print(r1.summary())
        print(r2.summary())
        print("\nChanging the first server:")
        r1.gb_used = 110.0
        print(r1.summary())
        print(r2.summary())
        print("\nLoading server records from a file:")

        try:
            records = Record.Record_load_records("records_sample.txt")
            over_limit_count = 0
            for record in records:
                status = record.status()
                print(f"{record.hostname} {status}")
                if status == "OVER LIMIT":
                    over_limit_count += 1
            print(f"\nTotal servers over limit: {over_limit_count}")
        except FileNotFoundError:
            print("Error: records_sample.txt not found.")
            if __name__ == "__main__":
                main()