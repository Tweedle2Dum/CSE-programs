a=eval(input("Enter matrix 1: "))
b=eval(input("Enter matrix 2: "))
s=[]
for i in range(len(a)):
    l=[]
    for j in range(len(a[i])):
        l.append(a[i][j]-b[i][j])
    s.append(l)
print("\n".join(map(str,s)))