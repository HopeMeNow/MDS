import numpy as np

def test_reader(X, N, m):
    return [X.shape[0], X.shape[1], N, m]
    

def test_loss(loss, X, datY):
    ws=np.loadtxt('.tests/loss.test', delimiter=',')
    return [loss(w, X, datY) for w in ws]
    
def test_grad(grad, X, datY):
    ws=np.loadtxt('.tests/grad.test', delimiter=',')
    return [np.sqrt(np.sum(np.power(grad(w, X, datY), 2))) for w in ws]

def test_norm(X):
    return [np.linalg.norm(np.mean(X, axis=0)), np.linalg.norm(np.std(X, axis=0)-np.ones(X.shape[1]))]
    

def test_new_loss(new_loss, X, datY):
    a=2
    b=1
    ws=np.loadtxt('.tests/newloss.test', delimiter=',')
    return [new_loss(w, X, datY, a, b) for w in ws]


def test_new_grad(new_grad, X, datY):
    a=2
    b=1
    ws=np.loadtxt('.tests/newgrad.test', delimiter=',')
    return [np.linalg.norm(new_grad(w, X, datY, a, b)) for w in ws]