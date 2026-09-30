import numpy as np

w = np.ones((2,3,4))
x = np.ones(4)
y = np.ones((2,2))


print(np.einsum("ijk,l,mn->ijklmn",w,x,y).shape)

#print(w @ x)
#print(np.sum(x[None, :] * w, axis=1))



#print(np.tensordot(w, x, axes=0))
#print(np.einsum("ij,k->ijk", w,x))