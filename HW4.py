#Jessica Noel
#I pledge my honor that I have abided by the Stevens Honor System
#CS-115 B/C

from importlib import reload as Rfrsh
import hmmm

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1 ■■■ f(5) = 5 ■■■ f(9) = 34
RecFibSeq = """ # You may not need all lines
00 setn r15, 42
01 read r1
02 calln r14, 5
03 write r4
04 halt
05 setn r13, 1
06 jnezn r1 8
07 jumpr r14
08 pushr r1,  r15
09 pushr r14, r15
10 addn r1,  -1
11 calln r14, 6
12 add r2, r4, r13
13 copy r4, r13
14 copy r13, r2
15 popr r14, r15
16 popr r1,  r15
17 jumpr r14
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = False

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
