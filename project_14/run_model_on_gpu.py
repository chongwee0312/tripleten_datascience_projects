
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, GlobalMaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LearningRateScheduler, ReduceLROnPlateau


def load_train(path):
    '''
    Loads the train part of dataset from the given path
    '''      
    train_gen = ImageDataGenerator(validation_split=0.2,
                                   rescale=1./255,
                                   horizontal_flip=True,
                                   rotation_range=20,
                                   zoom_range=0.2,
                                   shear_range=0.2)
    
    df_labels = pd.read_csv(path + 'labels.csv')
    directory = path + 'final_files'

    train_gen_flow = train_gen.flow_from_dataframe(
        dataframe=df_labels,
        directory=directory,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='training',
        seed=42
    )

    return train_gen_flow


def load_test(path):
    
    '''
    Loads the validation/test part of dataset from the given path
    '''
    test_gen = ImageDataGenerator(validation_split=0.2, 
                                  rescale=1./255)
    
    df_labels = pd.read_csv(path + 'labels.csv')
    directory = path + 'final_files'
    
    test_gen_flow = test_gen.flow_from_dataframe(
        dataframe=df_labels,
        directory=directory,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='validation',
        seed=42
    )

    return test_gen_flow


def create_model(input_shape):
    
    '''
    Returns a defined model
    '''
    # Get the base model - ResNet50
    base_model = ResNet50(
        input_shape=input_shape, weights='imagenet', include_top=False
    )    
    
    # Create the model
    model = Sequential()
    model.add(base_model)
    model.add(GlobalAveragePooling2D())
    # model.add(GlobalMaxPooling2D())
    model.add(Dropout(0.3))
    # model.add(Dense(256, activation='relu'))    
    model.add(Dense(1, activation='relu'))
    
    model.compile(loss='mse', 
                  optimizer=Adam(learning_rate=0.0005), 
                  metrics=['mae'])

    return model


def train_model(model,
                train_data,
                test_data,
                batch_size=None,
                epochs=20, 
                steps_per_epoch=None,
                validation_steps=None):
    '''
    Trains and returns the model with the given parameters
    '''
    # Calculate the steps for training and validation if not provided
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
    if validation_steps is None:
        validation_steps = len(test_data)

    # Self define a learning rate decay function
    # def lr_schedule(epoch):
    #     if epoch < 10:
    #         return 0.0003
    #     else:
    #         return 0.0001
    # lr_callback = LearningRateScheduler(lr_schedule)
    
    # Apply the ReduceLROnPlateau function
    reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                                  factor=0.3,
                                  patience=2,
                                  verbose=1)
    
    # Train the model
    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size,
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              callbacks=[reduce_lr],
              verbose=2)

    return model


