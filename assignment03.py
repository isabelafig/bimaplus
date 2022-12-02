#Ask how many points the user wants:
n=int(input("Type the number of vertices that the polygon that you want to calculate has: "))
print("Enter the points in counter-clockwise order: ")
#list of the coordinates
x=[]
y=[]

for i in range(n):
    xi=float(input(f"x[{i+1}]:"))
    yi=float(input(f"y[{i+1}]:"))
    x.append(xi)
    y.append(yi)

#this is the table:
print()
print("The vertices of the polygonon are:")
print()
print(f"{'x':>14}  {'Y':>10}")
print("-"   * 28)

for i in range(0,n):
    print("Point" , i+1 , ":" , f"{x[i]:>5} {y[i]:>10}")

print("-"   * 28)

#this are the formulas:
a=0
sx=0
sy=0
ix=0
iy=0
ixy=0
for i in range(0,n):
    a=a+(x[i]+x[i-1])*(y[i]-y[i-1])
    sx=sx+(x[i]-x[i-1])*(y[i]**2+y[i-1]*y[i]+y[i-1]**2)
    sy=sy+(y[i]-y[i-1])*(x[i]**2+x[i-1]*x[i]+x[i-1]**2)
    ix=ix+(x[i]-x[i-1])*(y[i]**3+y[i]**2*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    iy=iy+(y[i]-y[i-1])*(x[i]**3+x[i]**2*x[i-1]+x[i]*x[i-1]**2+x[i-1]**3)
    ixy=ixy+(y[i]-y[i-1])*(y[i]*(3*x[i]**2+2*x[i-1]*x[i]+x[i-1]**2)+y[i-1]*(3*x[i-1]**2+2*x[i-1]*x[i]+x[i]**2))
print()
Ax=1/2*a
Sx=-1/6*sx
Sy=1/6*sy
Ix=-1/12*ix
Iy=1/12*iy
Ixy=-1/24*ixy
XT=Sy/Ax
YT=Sx/Ax
IXT=Ix-(YT**2*Ax)
IYT=Iy-(XT**2*Ax)
IXYT=Ixy+(XT*YT*Ax)

#this are the outputs:
print("Geometric characteristics:")
print()
print("Ax=", round(Ax,2))
print("Sx=",round(Sx,2))
print("Sy=",round(Sy,2))
print("Ix=",round(Ix,2))
print("Iy=",round(Iy,2))
print("Ixy=",round(Ixy,2))
print("XT=",round(XT,2))
print("YT=",round(YT,2))
print("IXT=",round(IXT,2))
print("IYT=",round(IYT,2))
print("IXYT=",round(IXYT,2))