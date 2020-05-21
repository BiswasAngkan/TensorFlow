# Angkan Biswas
# 21.05.2020
# To check similarity of two images by measuring SSIM(Structural Similarity)
 
from tensorflow.keras.preprocessing.image import load_img
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf

def main():
	imgPath1 = '/home/dell/Downloads/frog.jpeg'
	imgPath2 = '/home/dell/Downloads/Figure.png'
	
	img1 = img_load(imgPath1)
	img2 = img_load(imgPath2)
	
	ssim = tf.image.ssim(img1, img2, max_val = 255 )
	print(ssim)
	ssimValue = tf.keras.backend.get_value(ssim)
	print(ssimValue)	

	if ssimValue == 1.0:
		print('Two images are same')	
	else:
		print('Two images are diffrent')	

def img_load(imgPath):
	img = load_img(imgPath, target_size = (256, 256))
	img = np.array(img, dtype = np.uint8)	
	img = tf.convert_to_tensor(img)	
	return img

def plot_fig(img):
	plt.imshow(img)
	plt.axis('off')
	plt.show()
	plt.close()

main()
