import random
c = 0
d = 0
end=10
angles=[]
angles_1=[]
while c < 10:
    x=((random.gauss(0,10)**(2))**(1/2))
    angles.append(x)
    c = c+1
while d <10:
    y=random.randrange(0, 90)
    angles_1.append(y)
    d=d+1
