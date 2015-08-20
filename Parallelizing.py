from multiprocessing import Pool
from contextlib import closing

def factorial(x):
    fac = 1
    for i in range(x):
        fac *= (i+1)
    return fac
values = [i for i in range(10)]

#if __name__ == '__main__':
#    with Pool(5) as p:
#        sol = p.map(factorial, values)
#if __name__ == '__main__':
#    with closing(Pool(processes=2)) as pool:
#        sol = pool.map(factorial,values)
#print(sol)     
from time import time as tic
values = [i for i in range(10)]
start = tic()
if __name__ == '__main__':
    with closing(Pool(processes=2)) as p:
        sol = p.map(factorial, values)
print('Parallel time:',tic()-start)
start = tic()
sol = [factorial(i) for i in values]
print('Linear time:',tic()-start)


attributes = [(1,2,3,4),(3,4,5,6)]
Solution = []
def basic_add(x):
    return[x[0]+x[1]+x[2]+x[3] , x[1]]

if __name__ == '__main__':
    with closing(Pool(processes=2)) as p:
        data = p.map(basic_add, [(1,2,3,4),(3,4,5,6)])
        
print(data)