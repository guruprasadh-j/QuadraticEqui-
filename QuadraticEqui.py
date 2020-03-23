import math
x=list(map(float,input().split()))
a = x[0]
b = x[1]
c = x[2]


d = (b**2) - (4*a*c)

s1 = (-b-math.sqrt(d))/(2*a)
s2 = (-b+math.sqrt(d))/(2*a)

print ('%.2f'%s2)
print ('%.2f'%s1)
