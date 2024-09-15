import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# get info from csv file
melbourne_file_path = './melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# create model
melbourne_model = DecisionTreeRegressor()

# drop missing data rows
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

# features that determine the price y
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# split data to train and validate
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# fit the model
melbourne_model.fit(train_X, train_y)

# check model accuracy using the validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))