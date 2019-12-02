from functools import reduce

lst =['caterpillar','bear','snail','moose']

lstLen=list(map(len, lst))
print(lst[lstLen.index(reduce(max,lstLen))])


