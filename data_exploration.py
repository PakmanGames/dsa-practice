import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# calculate mae based on number of leaf nodes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

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

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae))