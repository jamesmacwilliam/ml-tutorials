from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

size = 128

model = Sequential()

# note: input shape is 128x128 (size from capture_images.py x 3 for RGB)

# 3 layers of convolution is arbitrary, the maxpooling after each one handles varying
# image sizes

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(size, size, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())

# reduce overfitting
model.add(Dropout(0.5))

model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# compile with RMSprop optimizer learning rate of 0.0003 (this can be adjusted up/down)
model.compile(optimizer=RMSprop(lr=0.0003), loss='binary_crossentropy', metrics=['acc'])

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

validation_datagen = ImageDataGenerator(rescale=1.255)

train_generator = train_datagen.flow_from_directory('data/train',
                                                    target_size=(size,size),
                                                    class_mode='binary', batch_size=64)

validation_generator = validation_datagen.flow_from_directory('data/valid',
                                                              target_size=(size,size),
                                                              class_mode='binary', batch_size=64)

# 63 == steps, 64 == batch_size
# 63 * 64 =~ 4000+ (steps per epoch)
# 7 * 64 =~ 400 (validation steps)
model.fit_generator(train_generator, epochs=5, workers=4, steps_per_epoch=63,
                    validation_data=validation_generator, validation_steps=7)

model.save('model.h5')
