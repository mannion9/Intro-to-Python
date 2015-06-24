x=[0,1,2,3,4,5]
y=[0,1,2,3,4,5]

def trapazoid(x,y):
    index ,count,done= 0,0,[0]
    def area_trap(a,b,y_1,y_2):
        return (b-a)/2*(y_1+y_2)
    while index < len(x)-1:
        count += area_trap(x[index],x[index+1],y[index],y[index+1])
        done.append(count)
        index += 1
    return done

done = trapazoid(x,y)
print(done)




