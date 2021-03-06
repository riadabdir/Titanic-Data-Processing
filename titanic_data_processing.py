# -*- coding: utf-8 -*-
"""Titanic Data Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13AHtEtib4ow7TxG4DSwwgINN9Z9-xNvt

**Mount The Drive**
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""**Read and Show Tha Dataset**"""

import pandas as pd

#Read Dataset from Drive
titanic = pd.read_csv('gdrive/My Drive/10th Semester/AI Lab/Lab Assignment/titanic.csv')

#Show Dataset
titanic.head()

#Dataset Information
titanic.info()

#Null Value in Dataset
titanic.isnull().sum()

"""**Import Library for Data Visualization**"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set()

"""**Create Function to See the Graph**"""

def bar_chart(feature):
  survived = titanic[titanic['Survived']==1][feature].value_counts()
  dead = titanic[titanic['Survived']==0][feature].value_counts()
  df = pd.DataFrame([survived,dead])
  df.index = ['Survived','Dead']
  df.plot(kind='bar',stacked = True, figsize=(10,5))

"""**Find The Title from Name Column**


"""

titanic.head()

#Find The Title from Name Column
titanic_data = [titanic]
for dataset in titanic_data:
  dataset['Title'] = dataset['Name'].str.extract('([A-Za-z]+)\.',expand =False)

titanic['Title'].value_counts()

"""**Maping Name Title into Number**"""

title_mapping = {"Mr":1,"Mrs":2,"Miss":3,
                 "Master":4,"Dr":4,"Rev":4,"Mlle":4,"Major":4,"Col":4,"Capt":4,"Lady":4,"Ms":4,"Countess":4,"Mme":4,"Don":4,"Sir":4,"Jonkheer":4}

for dataset in titanic_data:
  dataset['Title'] = dataset['Title'].map(title_mapping)

titanic.head()

"""**Drop Unnecessary Column (Name)**"""

titanic.drop('Name',axis=1,inplace=True)

titanic.head()

"""**Maping Sex Columns into Number**"""

sex_mapping = {"male":1,"female":2}
for dataset in titanic_data:
  dataset['Sex'] = dataset['Sex'].map(sex_mapping)

titanic.head()

"""**Missing Value Fill Up of Age**"""

titanic["Age"].fillna(titanic.groupby("Title")["Age"].transform("median"),inplace=True)

titanic.isnull().sum()

"""**Different Age Divide in Catagorial Data**"""

facet = sns.FacetGrid(titanic, hue="Survived", aspect=4)
facet.map(sns.kdeplot, 'Age', shade = True)
facet.set(xlim = (0,titanic['Age'].max()))
facet.add_legend()
plt.show()

"""**Survived People By Age Limit**"""

facet = sns.FacetGrid(titanic, hue="Survived", aspect=4)
facet.map(sns.kdeplot, 'Age', shade = True)
facet.set(xlim = (0,titanic['Age'].max()))
facet.add_legend()
plt.xlim(0,30)

"""**Mapping Age Column**"""

for dataset in titanic_data:
  dataset.loc[dataset['Age']<=18, 'Age'] = 1
  dataset.loc[(dataset['Age']>18) & (dataset['Age']<=30), 'Age'] = 2
  dataset.loc[(dataset['Age']>30) & (dataset['Age']<=50), 'Age'] = 3
  dataset.loc[dataset['Age'] >50, 'Age'] = 4

titanic.head()

"""**Missing Value Fill Up of Embarked**"""

Pclass1 = titanic[titanic['Pclass']==1]['Embarked'].value_counts()
Pclass2 = titanic[titanic['Pclass']==2]['Embarked'].value_counts()
Pclass3 = titanic[titanic['Pclass']==3]['Embarked'].value_counts()
df = pd.DataFrame([Pclass1,Pclass2,Pclass3])
df.index = ['1st Class','2nd Class','3rd Class']
df.plot(kind = 'bar', stacked = True, figsize=(10,5))

for dataset in titanic_data:
  dataset['Embarked'] = dataset['Embarked'].fillna('S')

titanic.isnull().sum()

"""**Mapping Embarked Column**"""

embarked_mapping = {"S":1,"C":2,"Q":3}
for dataset in titanic_data:
  dataset['Embarked'] = dataset['Embarked'].map(embarked_mapping)

titanic.head()

"""**Different Fare Divide in Catagorial Data**"""

facet = sns.FacetGrid(titanic, hue="Survived", aspect=4)
facet.map(sns.kdeplot, 'Fare', shade = True)
facet.set(xlim = (0,titanic['Fare'].max()))
facet.add_legend()
plt.show()

"""**Survived People By Fare Limit**"""

facet = sns.FacetGrid(titanic, hue="Survived", aspect=4)
facet.map(sns.kdeplot, 'Fare', shade = True)
facet.set(xlim = (0,titanic['Fare'].max()))
facet.add_legend()
plt.xlim(0,20)

"""**Mapping Fare Column**"""

for dataset in titanic_data:
  dataset.loc[dataset['Fare']<=20, 'Fare'] = 1
  dataset.loc[(dataset['Fare']>20) & (dataset['Fare']<=60), 'Fare'] = 2
  dataset.loc[(dataset['Fare']>60) & (dataset['Fare']<=100), 'Fare'] = 3
  dataset.loc[dataset['Fare'] >100, 'Fare'] = 4

titanic.head()

"""**Drop Unnecessary Column (Ticket & Cabin)**"""

column_drop = ['Ticket','Cabin']
titanic = titanic.drop(column_drop, axis=1)

"""**Drop Unnecessary Column (SibSp & Parch)**"""

column_drop = ['SibSp','Parch']
titanic = titanic.drop(column_drop, axis=1)

titanic.head()

"""**Divide The Dataset Into Two Part**"""

titanic_data = titanic.drop('Survived',axis=1)
target = titanic['Survived']
titanic_data.shape, target.shape

"""**Splitting The Dataset into Train and Test Data**"""

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(titanic_data, target, test_size= .30, random_state = 42)
print("X-Train: ",xtrain.shape)
print("X-Test: ",xtest.shape)
print("Y-Train: ",ytrain.shape)
print("Y-Test: ",ytest.shape)

ytest.value_counts()

"""**Training and Testing the Dataset**"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
dt = DecisionTreeClassifier()
dt.fit(xtrain, ytrain)
y_predict = dt.predict(xtest)

"""**Performance Evaluation**"""

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(ytest, y_predict))
print(classification_report(ytest, y_predict))

"""**Overall Accuracy**"""

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,y_predict))

titanic.head()

"""**Data Visualization**"""

#Visualization of Pclass Column
bar_chart("Pclass")

#Visualization of Sex Column
bar_chart("Sex")

#Visualization of Age Column
bar_chart("Age")

#Visualization of Title Column
bar_chart('Title')

#Visualization of Fare Column
bar_chart("Fare")

#Visualization of Embarked Column
bar_chart('Embarked')