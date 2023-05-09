from tensorflow.keras.applications.vgg16 import VGG16

model = VGG16(weights='imagenet')
model.save('./models/my_model')
