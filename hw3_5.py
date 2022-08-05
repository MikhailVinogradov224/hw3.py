f1,f2 = 1,1
r,m = f1,f2
n = int(input())
s = []
s.append(r)
s.append(m)
for i in range(2,n):
    f1,f2 = f2,f1+f2
    s.append(f2)
    s.sort()   
print(s)
s.reverse()
a = ['-{}'.format(number) for number in s]
print(a)