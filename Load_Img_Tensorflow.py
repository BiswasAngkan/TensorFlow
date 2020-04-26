# Angkan Biswas
# 26.04.2020
# Load an image using TensorFlow's & display using Matplotlib module 


import numpy as np
from tensorflow.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt


imgPath = '/home/dell/PythonCode/Picture/apple.jpg'
img = load_img(imgPath, target_size =(240, 240))

img = np.array(img, dtype = np.uint)

plt.title('apple')
plt.imshow(img)
plt.show()
plt.close
