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

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = ""      # : replace with an input() call
first = 0.0     # : replace with an input() call, converted
second = 0.0    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = 0.0   # 
percent = 0.0      # 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you

print("=" * 30)
hostname = input("Enter your hostname:")
print(f"Your hostname is: {hostname}")
print("=" * 30)
gb_used = float(input("Enter the amount of GB used:"))
print(f"You have used: {gb_used} GB")
gb_total = float(input("Enter the total amount of GB:"))
print(f"The total amount of GB is: {gb_total}")
gb_remaining = gb_total - gb_used
percent_used = (gb_used / gb_total) * 100
print(f"GB remaining: {gb_remaining}")
print(f"Percentage used: {percent_used:.2f}%")
print("=" * 30)