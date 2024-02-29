ls50 = [i for i in range (0,51)]
print(ls50)

lis = [3,4,5]
def sqrls(lis):
    return [i**2 for i in lis]
print(sqrls(lis))

lsA = [1,2,3,4,5,6,7,8,9,10]
lsB = [20,21,22,23,24,25,26,27,28,29,30]
lsC = lsA+lsB
def oddNum(lsC):
    for i in lsC:
        if i % 2 !=0:
            print(i)
print(oddNum(lsC))