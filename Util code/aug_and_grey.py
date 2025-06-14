import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import os

# Define your directory path and save path
input_directory = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\no_yawn'
output_directory = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\new_no_yawn'

# Image augmentation configuration
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


def convert_and_save_grayscale(img, filename):
    # Convert RGB to grayscale using mean of channels
    gray = np.mean(img, axis=-1, keepdims=True)

    # Convert from array to image and save
    gray_img = array_to_img(gray)
    gray_img.save(os.path.join(output_directory, filename))


if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each image in the directory
for filename in os.listdir(input_directory):
    # add more formats if needed
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(input_directory, filename)

        # Load image
        img = load_img(img_path)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        # Apply augmentations
        i = 0
        for batch in datagen.flow(x, batch_size=1):
            convert_and_save_grayscale(
                batch[0], f"augmented_{filename.split('.')[0]}_{i}.jpg")
            i += 1
            if i > 35:  # Save 20 augmented versions per image, change this if you want more or less
                break
