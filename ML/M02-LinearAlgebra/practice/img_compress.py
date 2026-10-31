from PIL import Image
import numpy as np
from numpy.linalg import svd
import matplotlib.pyplot as plt

def compress(a, k):
    U, s, Vt = svd(a, full_matrices=False)
    compressed=U[:,:k] @ np.diag(s[:k]) @ Vt[:k, :]
    return compressed

img = Image.open('image.jpeg').convert("RGB")
img.show()

img_array=np.array(img)

img_r=img_array[:,:,0]
img_b=img_array[:,:,1]
img_g=img_array[:,:,2]

k=80
comp_r=compress(img_r, k)[:,:,None]
comp_b=compress(img_b, k)[:,:,None]
comp_g=compress(img_g, k)[:,:,None]
comp=np.append(np.append(comp_r, comp_b, axis=2), comp_g, axis=2)
plt.imshow(np.clip(comp/255, 0, 1), vmin=0, vmax=255)
plt.show()

