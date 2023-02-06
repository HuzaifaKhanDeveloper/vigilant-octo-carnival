#Question No 07
o=input("Write Length of First Side Of Triangle:")
v=float(o)
m=input("Write Length Of Second Side Of Triangle:")
i=float(m)
l=input("Write Length Of Third Side Of Triangle:")
z=float(l)
#To find Peremeter
s=v/2+i/2+z/2
e=s-v
f=s-i
g=s-z
q=s*e*f*g
r=q**0.5
print("Area Of Triangle %.2f" %(r))# vigilant-octo-carnival
