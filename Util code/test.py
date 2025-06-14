# import numpy as np
# from keras.preprocessing.image import ImageDataGenerator
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from keras.callbacks import ModelCheckpoint

# # Load data using memory map
# x = np.load('x.npy', mmap_mode='r')
# y = np.load('y.npy', mmap_mode='r')

# # Create a random subset of indices
# np.random.seed(0)
# indices = np.random.choice(len(x), size=81675, replace=False)

# # Model Definition
# new_model = Sequential()
# new_model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
# new_model.add(MaxPooling2D((2, 2)))
# new_model.add(Conv2D(64, (3, 3), activation='relu'))
# new_model.add(MaxPooling2D((2, 2)))
# new_model.add(Conv2D(128, (3, 3), activation='relu'))
# new_model.add(MaxPooling2D((2, 2)))
# new_model.add(Flatten())
# new_model.add(Dense(512, activation='relu'))
# new_model.add(Dense(1, activation='sigmoid'))  # Binary classification

# # Compilation
# new_model.compile(optimizer='adam',
#                   loss='binary_crossentropy', metrics=['accuracy'])

# # Data augmentation configuration
# datagen = ImageDataGenerator(validation_split=0.1)

# # Model checkpoints
# checkpoint = ModelCheckpoint(
#     'model_weights.h5', monitor='val_accuracy', save_best_only=True, mode='max')
# callbacks_list = [checkpoint]

# # Batch processing
# batch_size = 1000
# for i in range(0, len(indices), batch_size):
#     batch_indices = indices[i:i+batch_size]
#     x_subset = x[batch_indices]
#     y_subset = y[batch_indices]

#     # Create the generators
#     train_generator = datagen.flow(
#         x_subset, y_subset, batch_size=16, subset='training')
#     val_generator = datagen.flow(
#         x_subset, y_subset, batch_size=16, subset='validation')

#     # Train the model on this batch
#     new_model.fit(train_generator, validation_data=val_generator,
#                   epochs=10, callbacks=callbacks_list)

# # Note: After training, you might want to evaluate your model on a separate test set or make predictions.
