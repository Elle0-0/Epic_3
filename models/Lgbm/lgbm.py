# IMPORTS

import lightgbm as lgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# READ DATA


# Read the CSV file
data = pd.read_csv('C:\\Users\\ticta\\MyRepos\\Epic_3\\datasets\\clean\\combined-data.csv')
# Display the first few rows of the DataFrame
print(data.head())


# PROCESS DATA AND PLOT


import numpy as np
# Split the data into X and Y
X = data.filter(regex='co2_total')
Y = data.filter(regex='surface_temperature')
X_values = X.values.flatten()
Y_values = Y.values.flatten()

# Calculate row averages
X_column_averages = np.mean(X, axis=0)
Y_column_averages = np.mean(Y, axis=0)

print("Row averages of X:", X_column_averages)
print("Row averages of Y:", Y_column_averages)


plt.figure(figsize=(10, 6))
plt.scatter(X_values, Y_values)
plt.xlabel('CO2 Total')
plt.ylabel('Surface Temperature')
plt.title('CO2 Total vs Surface Temperature')
plt.figure(figsize=(10, 6))

# Plot the row averages
plt.figure(figsize=(10, 6))

# Plot the row averages
plt.scatter(X_column_averages, Y_column_averages, color='r', label='Row Averages')

plt.xlabel('Average CO2 Total')
plt.ylabel('Average Surface Temperature')
plt.title('Average CO2 Total vs Average Surface Temperature')

# Set the limits of the x and y axes
plt.xlim(80, 130)

plt.legend()
plt.show()

# %% [markdown]
# TRAIN MODEL

# %%
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
X_train,X_valid,y_train,y_valid = train_test_split(X_column_averages,Y_column_averages,random_state=42,test_size=0.2)
#X_train,X_valid,y_train,y_valid = train_test_split(X_values,Y_values,random_state=42,test_size=0.2)
X_valid = np.reshape(X_valid, (-1, 1))
X_train = np.reshape(X_train, (-1, 1))
train = lgb.Dataset(X_train, label=y_train)
valid = lgb.Dataset(X_valid, label=y_valid)
parameters = {
    "objective": "regression",
    "metric": "l2",
    "boosting_type": "gbdt",
    "verbose": -1,
    "num_leaves": 100,
    "learning_rate": 0.25,
    "feature_fraction": 0.90,
}
print(X_train.shape)
print(y_train.shape)

print("X_train dimensions: ", X_train.ndim)
print("y_train dimensions: ", y_train.ndim)


# %%
import matplotlib.pyplot as plt

# Assuming your data is 1-dimensional
plt.figure(figsize=(10, 6))

# Plot the training data
plt.scatter(X_train, y_train, color='blue', label='Training data')

# Plot the test data
plt.scatter(X_valid, y_valid, color='red', label='Test data')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Training and Test Data')
plt.legend()
plt.show()

# %%
import lightgbm as lgb
model_lgbm = lgb.train(parameters, train, valid_sets=valid, num_boost_round=1200)

# Mean squared error evalutation

from sklearn.metrics import mean_squared_error

y_train_pred = model_lgbm.predict(X_train)
y_valid_pred = model_lgbm.predict(X_valid)

# Make predictions
y_train_pred = model_lgbm.predict(X_train, num_iteration=model_lgbm.best_iteration)
y_valid_pred = model_lgbm.predict(X_valid, num_iteration=model_lgbm.best_iteration)

# Print RMSE
print('The RMSE of prediction on training set is: ', mean_squared_error(y_train, y_train_pred) ** 0.5)
print('The RMSE of prediction on validation set is: ', mean_squared_error(y_valid, y_valid_pred) ** 0.5)

from sklearn.metrics import mean_absolute_error

 # Calculate the mean absolute error

print("Mean Absolute Error (MAE) on training set:", mean_absolute_error(y_train, y_train_pred))
print("Mean Absolute Error (MAE) on validation set:", mean_absolute_error(y_valid, y_valid_pred ))



# Mean Absolute Squared Error

# Assuming X_test is your test data
X_test = np.array([110]).reshape(-1, 1)
y_test_pred = model_lgbm.predict(X_test, num_iteration=model_lgbm.best_iteration)
print("The predicted value for 110 is:", y_test_pred[0])

import matplotlib.pyplot as plt

# Assuming your data is 1-dimensional
plt.figure(figsize=(10, 6))

# Plot the training data
plt.scatter(X_train, y_train, color='blue', label='Training data')

# Plot the test data
plt.scatter(X_valid, y_valid, color='red', label='Test data')

# Plot the prediction
plt.scatter(X_test, y_test_pred, color='purple', label='Prediction')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Training, Test Data and Prediction')
plt.legend()
plt.show()


