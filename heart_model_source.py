import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,VotingClassifier
from sklearn.svm import SVC

#data loading
df=pd.read_csv("dataset/heart.csv")

#data Feature extraction
x=df.drop('target',axis=1)
y=df['target']

#data Splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Model Defination
heart_model=VotingClassifier(estimators=[('dt',DecisionTreeClassifier()),('rf',RandomForestClassifier()),('svc',SVC())],voting='hard')

#model training
heart_model.fit(x_train,y_train)

#prediction model function
def heart_disease_function(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Create a DataFrame for the input data
    input_data_heart = {
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    }
    input_df_heart = pd.DataFrame(input_data_heart)

    # Predict using the model
    heart_predicted = heart_model.predict(input_df_heart)
    
    if heart_predicted[0] == 1:
        return "⚠️ Based on the model's analysis, there is a high likelihood of heart disease. 🩺 Please consult a cardiologist or healthcare professional for further evaluation and advice."
    else:
        return "✅ The model predicts no significant likelihood of heart disease at this time. 💓 Maintaining a heart-healthy lifestyle is always recommended, including regular exercise and a balanced diet!"


#print(heart_disease_function(44, 1, 2, 140, 235, 0, 0, 180, 0, 0.0, 2, 0, 2))
#1
