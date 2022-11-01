import glob
import CaptchaCracker as cc

# Training image data path
train_img_path_list = glob.glob("data/train_numbers_only/*.png")

# Training image data size
img_width = 200
img_height = 50

# Creating an instance that creates a model
CM = cc.CreateModel(train_img_path_list, img_width, img_height)

# Performing model training
model = CM.train_model(epochs=100)

# Saving the weights learned by the model to a file
model.save_weights("../model/weights.h5")