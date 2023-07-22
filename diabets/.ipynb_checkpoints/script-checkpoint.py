import pandas as pd
import sqlite3

df = pd.read_csv('Datasets/diabetes.csv')
cnn = sqlite3.connect('Database/Database.db')