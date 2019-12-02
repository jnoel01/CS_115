# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Jessica Noel
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System
# Purpose : Create functions using Hmmm to output wanted outcome.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3, r2, r1
03 jltzn r3 05
04 jgtzn r3 07
05 write r1
06 halt
07 write r2
08 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 ≥ 0
Power = """
00 read r1
01 read r2
02 addn r2, -1
03 copy r3, r1
04 mul r3, r3, r1
05 addn r2, -1
06 jnezn r2 4
07 write r3
08 halt
"""


# Fibonacci
#  Write a hmmm function that gets one numner,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 ≥ 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 addn r1 1
02 jeqzn r1 10
03 setn r3 1
04 setn r2 0 
05 add r4, r3, r2  
06 copy r3, r2
07 copy r2, r4
08 addn r1 -1
09 jnezn r1 05
10 write r3
11 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Max  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


