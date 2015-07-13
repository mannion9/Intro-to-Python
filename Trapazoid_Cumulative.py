x=[0,1,2,3,4,5]
y=[0,1,2,3,4,5]

def trapazoid(x,y,option):
    if option == 'Sum':
        return (x[-1]-x[0])/(2*(len(x)-1))*(y[0]+2*sum(y[1:-1])+y[-1])
    index ,count,done= 0,0,[0]
    def area_trap(a,b,y_1,y_2):
        return (b-a)/2*(y_1+y_2)
    while index < len(x)-1:
        if option == 'Cumulative':
            count += area_trap(x[index],x[index+1],y[index],y[index+1])
        if option == 'Discrete':
            count = area_trap(x[index],x[index+1],y[index],y[index+1])
        done.append(count)
        index += 1
    else:
        return done
    return done

done = trapazoid(x,y,'Discrete')
print(done)




