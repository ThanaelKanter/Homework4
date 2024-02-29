ls=[2,2,4,4,6,6]
rem = []
for i in ls:
    if i not in rem:
        rem.append(i)
print(str(rem))