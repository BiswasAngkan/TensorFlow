# Angkan Biswas
# 26.04.2020
# To load pretrained model

''' For the first time model will be downloaded from Keras repository & it will be saved in users home directory. Next time model will be loaded from the users home directory, i.e., /home/dell/.keras/models/'''


from tensorflow.keras.applications.vgg16 import VGG16			
from tensorflow.keras.applications.mobilenet import MobileNet

vgg16Model = VGG16()				# Load pretrained model VGG16 [size = 528 MB]
vgg16Model.summary()				# Display model arcitracture
del vgg16Model					# Delete loaded model. It is nessary when multiple models need to loaded

mobileModel =MobileNet()			# Load pretrained mobile [size = 17 MB]
mobileModel.summary()				# Display model arcitracture
