#Jessica Noel
#I pledge my honor that I have abided by the Stevens Honor System
#10/3/19
#Lab 6

##################################################


def decimalToBinary(x):
    '''will convert a decimal number to a R2L number'''
    if x == 1:
        return [1]
    elif x%2 == 0:
        return (decimalToBinary(x//2) + [0])
    else:
        return  (decimalToBinary(x//2) + [1])

    
##################################################

    
def binaryToDecimal(num):
    '''given a R2L binary formatted number the function will output the equivalent integer'''
    if num == '':
        return 0
    else:
        return binaryToDecimal(num[:-1])*2+int(num[-1])

    
##################################################
def incrementBinary(num):
    return helper1(num, 1)

def helper1(num, c):
    if num == []:
        if c == 1:
            return (num + [c])
    else:
            return []
    if (num[0]+c) > 1:
        return [0]+helper1(num[1:], 1)
    elif num[0]+c == 1:
        return [1]+ helper1(num[1:], 0)
    else:
        if num[-1]==0:
            return num[0:-1]
        return num


###################################################


def addBinary(num1,num2):
    '''Will output the sum of two R2L numbers'''
    return helper2(num1, num2, 0)
def helper2(num1,num2,x):
    '''helper function for addBinary function'''
    if len(num1)>len(num2):
        length = len(num1) - len(num2)
        num2 += ([0] * length)
    elif (len(num1) < len(num2)):
        length = len(num2) -len(num1)
        num1 += [0] * length
    if num1==1 or num2==[]:
        if x==0:
            return []
        else:
            return [x]
    result =  num1[0] + num2[0]+x
    if result == 0:
        return [0] + helper2(num1[1:], num2[1:], 0)
    if result == 1:
        return [1]  + helper2(num1[1:], num2[1:],0)
    if result == 2:
        return [0] + helper2(num1[1:], num2[1:],1)
    if result == 3:
        return [1] + helper2(num1[1:], num2[1:],1)
