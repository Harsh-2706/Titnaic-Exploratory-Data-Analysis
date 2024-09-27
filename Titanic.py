import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic_original.csv')

print(data.info())

print(data.describe())

print(data.isnull().sum())

print(data['sex'].value_counts())
print(data['embarked'].value_counts())

plt.hist(data['age'], bins=20)
plt.xlabel('age')
plt.ylabel('Count')
plt.title('Distribution of Passenger Ages')
plt.show()

sns.barplot(x='sex', y='survived', data=data)
plt.xlabel('sex')
plt.ylabel('survival rate')
plt.title('survival rate by sex')
plt.show()
