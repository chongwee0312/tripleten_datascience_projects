#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# file_name: optunaopt.py

import optuna
from tqdm.auto import tqdm
import time


# In[ ]:


def sklearn_opt(model, objective, n_trials, direction, X_train, y_train, model_name='model'):    
    '''
    Optimise a scikit-learn model with the Optuna library.

    The model is optimised based on a user-defined objective function.

    Parameters
    ----------
    model : class
        The scikit-learn model class (e.g., LogisticRegression, DecisionTree, etc.) that 
        you want to optimise.
    objective : function
        The objective function to be minimised or maximised during optimisation. This function should 
        take a single argument `trial` object, and it should return a numerical score to be optimised.
    n_trials : int
        The number of trials (iterations) for the optimisation process.
    direction : str, {'minimize', 'maximize'}
        Direction of optimisation. Set `minimize` for minimisation and `maximize` for maximisation.
    X_train : array-like of shape (n_samples, n_features)
        The data to fit. For example, a list or an array.
    y_train : array-like of shape (n_samples,)
        The target variable to try to predict.
    model_name : str, default 'model'
        A string representing the name of the model. 

    Returns
    -------
    tuple
        A tuple containing the optimised model and the training time.
        
    Examples
    --------
    >>> from sklearn.datasets import load_iris    
    >>> from sklearn.linear_model import LogisticRegression
    >>> from sklearn.model_selection import cross_val_score

    >>> def objective(trial):
    >>>     # Define your objective function to be minimised or maximised        
    >>>     C = trial.suggest_float('C', 1e-3, 1e1, log=True)        
        
    >>>    clf = LogisticRegression(C=C)
    >>>     # Assume X_train, y_train are defined
    >>>     accs = cross_val_score(clf, X_train, y_train, scoring='accuracy', cv=5)
        
    >>>     # Return a numerical score to be minimised or maximised
    >>>     return accs.mean()

    >>> # Assume X_train, y_train are defined
    >>> best_model, train_time = sklearn_clf_opt(LogisticRegression, objective, n_trials=50, 
    ...                                          direction='maximize', X_train=X_train, y_train=y_train,
    ...                                          model_name='MyLogisticRegression')
    '''
    # Set the optuna verbosity level to warning only
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    
    # Create the optimisation study
    study = optuna.create_study(sampler=optuna.samplers.TPESampler(seed=42),
                                direction=direction,
                                study_name=f'{model_name}_study')    

    # Optimise the model and show the progress bar
    with tqdm(total=n_trials, desc=f'Optimising {model_name}... ') as pbar:
        def callback(study, trial):
            pbar.update(1)    
        study.optimize(objective, n_trials=n_trials, callbacks=[callback])

    # Print the best hyperparameter found
    print('Best hyperparameters:')
    display(study.best_params)    

    # Recreate the best model
    best_model = model(**study.best_params) 

    # Train the model and record the training time          
    train_start = time.time()
    best_model.fit(X_train, y_train)
    train_end = time.time()
    train_time = round((train_end - train_start) * 1000)

    return best_model, train_time


# In[ ]:


def keras_opt(model, objective, n_trials, direction, X_train, y_train, model_name='model'):    
    '''
    Optimise a Keras model with the Optuna library.

    The model is optimised based on a user-defined objective function.

    Parameters
    ----------
    model : callable
        A function or callable class that generates an instance of the Keras model. 
        This should be a function that takes hyperparameters `units`, `hidden_layers`, 
        `learning_rate`, `dropout_rate` (optional) and returns a Keras model instance.
    objective : function
        The objective function to be minimised or maximised during optimisation. This function should 
        take a single argument `trial` object, and it should return a numerical score to be optimised.
    n_trials : int
        The number of trials (iterations) for the optimisation process.
    direction : str, {'minimize', 'maximize'}
        Direction of optimisation. Set `minimize` for minimisation and `maximize` for maximisation.
    X_train : array-like of shape (n_samples, n_features)
        The data to fit. For example, a list or an array.
    y_train : array-like of shape (n_samples,)
        The target variable to try to predict.
    model_name : str, default 'model'
        A string representing the name of the model. 

    Returns
    -------
    tuple
        A tuple containing the optimised model and the training time.
        
    Examples
    --------
    >>> from keras.models import Sequential
    >>> from keras.layers import Dense
    >>> from keras.optimizers import Adam

    >>> def keras_clf(units, hidden_layers, learning_rate):
    >>>     clf = Sequential()
    >>>     for _ in range(hidden_layers):
    >>>         clf.add(Dense(units, activation='relu'))
    >>>     clf.add(Dense(1, activation='sigmoid'))

    >>>     clf.compile(loss='binary_crossentropy',
    ...                 optimizer=Adam(learning_rate=learning_rate),
    ...                 metrics=['accuracy'])

    >>>     return clf
    
    >>> def objective(trial):
    >>>     units = trial.suggest_int('units', 8, 128, log=True)
    >>>     hidden_layers = trial.suggest_int('hidden_layers', 1, 3)
    >>>     learning_rate = trial.suggest_float('learning_rate', 1e-5, 1e-1, log=True)
    >>>     epochs = trial.suggest_int('epochs', 5, 50)

    >>>     clf = keras_clf(units, hidden_layers, learning_rate)
    
    >>>     # Assume X_train, y_train are defined
    >>>     clf.fit(X_train, y_train, epochs=epochs, verbose=0)
        
    >>>     # Return a numerical score to be minimised or maximised
    >>>     return clf.evaluate(X_train, y_train)[1]  # Use accuracy as the score

    >>> # Assume X_train, y_train are defined
    >>> best_model, train_time = keras_clf_opt(keras_clf, objective, n_trials=50, 
    ...                                        direction='maximize', X_train=X_train, y_train=y_train,
    ...                                        model_name='MyKerasModel')                             
    '''
    # Set the optuna verbosity level to warning only
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    
    # Create the optimisation study
    study = optuna.create_study(sampler=optuna.samplers.TPESampler(seed=42),
                                direction=direction,
                                study_name=f'{model_name}_study')

    # Optimise the model and show the progress bar
    with tqdm(total=n_trials, desc=f'Optimising {model_name}... ') as pbar:
        def callback(study, trial):
            pbar.update(1)    
        study.optimize(objective, n_trials=n_trials, callbacks=[callback])

    # Print the best hyperparameter found
    print('Best hyperparameters:')
    display(study.best_params)    

    # Recreate the best model
    units = study.best_params['units']
    hidden_layers = study.best_params['hidden_layers']
    learning_rate = study.best_params['learning_rate']
    epochs = study.best_params['epochs']
    
    if study.best_params['dropout_rate'] is not None:
        best_model = model(units=units, 
                           hidden_layers=hidden_layers, 
                           learning_rate=learning_rate,
                           dropout_rate=study.best_params['dropout_rate'])
    else:
        best_model = model(units=units, 
                           hidden_layers=hidden_layers, 
                           learning_rate=learning_rate)

    # Train the model and record the training time          
    train_start = time.time()
    best_model.fit(X_train, y_train, epochs=epochs, verbose=0)
    train_end = time.time()       
    train_time = round((train_end - train_start) * 1000)

    return best_model, train_time

