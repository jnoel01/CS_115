'''
Name: Jessica Noel

Date: 9/24/19

CS115 - HW 2 ~ Recursion

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

## Part 1 ~ Change

def makeChange(val, coins):
    '''Will return the least amount of coins needed to obtain the given value, as well as return the
specific coins used to obtain the value'''
    if val == 0:
        return [val, []]
    elif coins == []:
        return [float('inf'), []]
    elif coins[0] > val:
        return makeChange(val, coins[1:])
    else:
        loseIt= makeChange(val, coins[1:])
        useIt= makeChange(val - coins[0], coins)
        other= [useIt[0] +1, [coins[0]] + useIt[1]]
        if loseIt[0] > other[0]:
            return other
        else:
            return loseIt

## Part 2 ~ Least Common Substrings


def LCS(a,b):
    '''function will return the least common substring between (a,b) (least common amount
of letters within two words (strings)'''
    if a== '' or b=='':
        return ''
    elif (a[0] == b[0]):
        return a[0]+LCS(a[1:],b[1:])
    else:
        loseIt=LCS(a[1:],b)
        useIt=LCS(a,b[1:])
    if (len(useIt)>len(loseIt)):
        return useIt
    return loseIt

def helper(s1,s2,a):
    if s1=='' or s2=='':
        return []
    if s1[0]==s2[0]:
        a+=1
        return [a] +helper(s1[1:], s2[1:],a)
    else:
        a += 1
        return helper(s1[1:], s2, a)

def PLCS(a,b):
    common = LCS(a,b)
    if common == '':
        return [[-1],[-1]]
    else:
        return [helper(a, common, -1)] + [helper(b, common, -1)]
    
