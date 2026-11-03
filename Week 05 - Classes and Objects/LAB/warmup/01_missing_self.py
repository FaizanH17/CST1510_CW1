# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self):    # this parameter should be self
        return self

r = Record()
print(r.status())
