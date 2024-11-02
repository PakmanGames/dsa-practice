import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# calculate mae based on number of leaf nodes
def get_mae_tree(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

def get_mae_forest(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

# get info from csv file
melbourne_file_path = './melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# create model
melbourne_model = RandomForestRegressor(random_state=1)

# drop missing data rows
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

# features that determine the price y
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# split data to train and validate
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae_tree(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d" %(max_leaf_nodes))
    print("TREE: Mean Absolute Error: %d" %(my_mae))
    my_forest_mae = get_mae_forest(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("FOREST: Mean Absolute Error: %d" %(my_forest_mae))
    print("\n")