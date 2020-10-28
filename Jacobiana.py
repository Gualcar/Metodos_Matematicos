import numpy as np

def func(x):
    f1 = x[0]**2 + x[1]**2 
    f2 = x[0]*x[1]
    f = np.append(f1,f2)
    return f

def jacobiana(func,x0,dx):

    f0 = func(x0)

    xn = np.copy(x0)

    n = len(f0)
    m = len(x0) 

    jac = np.zeros((n,m))

    for i in range(m):

        #Porque não deu xn[i] = xn[i] + dx??
        xn = np.zeros(m)
        xn[i] = dx
        fn = func(xn+x0)

        jac[:,i] = (fn-f0)/dx

    return jac

dx = 1e-4
x0 = np.array([1,2])

print(jacobiana(func,x0,dx))
