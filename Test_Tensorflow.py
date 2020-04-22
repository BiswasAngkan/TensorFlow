# Angkan Biswas
# 22.04.2020
# Load an image using TensorFlow's module 



from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import cv2

imgPath = '/home/dell/PythonCode/Picture/apple.jpg'
img = load_img(imgPath, target_size = (255, 255))
img = np.array(img)
print(img.shape)

bgrImg = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

cv2.imshow('Apple', bgrImg)
cv2.waitKey(0)
