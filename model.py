import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


# create df
train = pd.read_csv('data/sum_sub_df1_10052020.csv')

# drop null values
train.dropna(inplace=True)

# features and target
target = 'Deaths'
features = ['date_sec', 'Confirmed', 'Recovered']

# X matrix, y vector
X = train[features]
y = train[target]

# model 
model = LinearRegression()
model.fit(X, y)
model.score(X,y)

pickle.dump(model, open('model.pkl', 'wb')) # write data dump

model = pickle.load(open('model.pkl','rb')) # read data dump
# print predictions with 'date_sec' : 1589095613, 'Confirmed' : 230, 'Recovered' : 150
