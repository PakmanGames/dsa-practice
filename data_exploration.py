import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# get info from csv file
melbourne_file_path = './melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# create model
melbourne_model = DecisionTreeRegressor(random_state=1)

# drop missing data rows
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

# features that determine the price y
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

melbourne_model.fit(X,y)

print("predictions for these 5 houses: ")
print(X.head())
print("predictions are:")
print(melbourne_model.predict(X.head()))