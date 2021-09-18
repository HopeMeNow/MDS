import numpy as np
from math import *

from time import time



def exact_checker(middle):
    count=0
    
    st=time()
    f=lambda x: cos(x)
    a=0
    b=np.pi/2
    n=101
    I=middle(f, a, b,  n)
    dur=time()-st
    err=np.abs(I-1)
    print('Test 1  |::|  err=', err, '  |::|   time=', dur, 's')
    if err<0.05:
        count+=1
        print('Test 1  |::|  accuracy OK')
    else:
        print('Test 1  |::|  accuracy FAILED')
    
    st=time()
    f=lambda x: x**x
    a=0
    b=2
    n=101
    I=middle(f, a, b,  n)
    dur=time()-st
    err=np.abs(I-2.83288)
    print('Test 2  |::|  err=', err, '  |::|   time=', dur, 's')
    if err<0.05:
        count+=1
        print('Test 2  |::|  accuracy OK')
    else:
        print('Test 2  |::|  accuracy FAILED')
        
    st=time()
    f=lambda x: e**(-x**2)
    a=-2
    b=2
    n=201
    I=middle(f, a, b,  n)
    dur=time()-st
    err=np.abs(I-1.7641627)
    print('Test 3  |::|  err=', err, '  |::|   time=', dur, 's')
    if err<1.9:
        count+=1
        print('Test 3  |::|  accuracy OK')
    else:
        print('Test 3  |::|  accuracy FAILED')
    print('Passed: ', count, '/3')
    
