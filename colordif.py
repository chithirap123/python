color1=input("enter a set of colors(space seperated):")
color2=input("enter a set of colors(space seperated):")
c1=set(color1.split())
c2=set(color2.split())
print("the diffrence between",c1,"and",c2,"is",c1.difference(c2))
