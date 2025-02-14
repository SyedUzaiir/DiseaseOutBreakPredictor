import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,VotingClassifier
from sklearn.svm import SVC

#data loading
df=pd.read_csv("dataset/diabetes pre processed.csv")

#data Feature extraction
x=df.drop(['Outcome'],axis=1)
y=df['Outcome']

#data Splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Model Defination
diabetes_model=RandomForestClassifier(n_estimators=100,criterion='gini')

#model training
diabetes_model.fit(x_train,y_train)

#prediction model function
def diabetes_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):

  input_data_dia={
      'Pregnancies':Pregnancies,
      'Glucose':Glucose,
      'BloodPressure':BloodPressure,
      'SkinThickness':SkinThickness,
      'Insulin':Insulin,
      'BMI':BMI,
      'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
      'Age':Age
  }
  input_df=pd.DataFrame(input_data_dia,index=[0])
  dia_prediction=diabetes_model.predict(input_df)
  if dia_prediction[0] == 1:
    return "⚠️ Based on the model's analysis, there is a high likelihood of diabetes. 🩺 Please consult a healthcare professional for further advice."
  else:
    return "✅ The model predicts no significant likelihood of diabetes at this time. 🌿 Maintaining a healthy lifestyle is always recommended!"


#print(diabetes_prediction(1,84,64,23,115,36.9,0.471,28))
