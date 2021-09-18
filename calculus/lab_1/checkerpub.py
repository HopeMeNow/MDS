import numpy as np
from math import *


from time import time

def findif_check(derForward):
    count=0
    I=[0.001, 2*np.pi]
    f=lambda x: sin(x)
    h=0.01
    st=time()
    x, dy=derForward(f, I, h)
    dur=time()-st

    if x.shape[0]!=dy.shape[0]:
        print('FAILED: x and dy shape mismatch!')
    else:
        df=lambda x: cos(x)    
        err=np.max(np.abs(dy-np.vectorize(df)(x)))
        print('Test 1 |::|  err=', np.max(np.abs(dy-np.cos(x))), '  |::|  time: ', dur, 's')
        if err<2*0.0075:
            count+=1
            print('Test 1 |::|  accuracy OK') 
        else:
            print('Test 1 |::|  accuracy FAIL') 
        f=lambda x: x**x
        I=[0.001, 1]

        st=time()
        x, dy=derForward(f, I, h)
        dur=time()-st
        
        df=lambda x: x**x*(log(x)+1)
        err=np.max(np.abs(dy-np.vectorize(df)(x)))
        print('Test 2 |::|  err=', err, '  |::|  time: ', dur, 's')
        if err<2:
            count+=1
            print('Test 2 |::|  accuracy OK')
        else:
            print('Test 2 |::|  accuracy FAIL')

        f=lambda x: e**(-x**2)
        I=[0.001, 1]

        st=time()
        x, dy=derForward(f, I, h)
        dur=time()-st
        
        df=lambda x: -2*x*e**(-x**2)
        err=np.max(np.abs(dy-np.vectorize(df)(x)))
        print('Test 3 |::|  err=', err, '  |::|  time: ', dur, 's')
        if err<2*0.01:
            count+=1
            print('Test 3 |::|  accuracy OK')
        else:
            print('Test 3 |::|  accuracy FAIL')
    print('Passed: ', count, '/ 3')

    
def getNoised(n, alpha, sigma):
    x=np.linspace(0, 10, n)
    y=np.sin(x)
    noise=np.random.normal(0, sigma, n)
    ar=np.zeros(n)
    for i in range(1, n):
        ar[i]=ar[i-1]*alpha+noise[i]
    return x, y+ar

def coef(x,y):
    return (x.shape[0]*np.sum(np.multiply(x,y))-np.sum(x)*np.sum(y))/(x.shape[0]*np.sum(np.power(x, 2))-np.sum(x)*np.sum(x))


