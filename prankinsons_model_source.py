import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,VotingClassifier
from sklearn.svm import SVC

#data loading
df=pd.read_csv("dataset/parkinsons.csv")

#data Feature extraction
x=df.drop(['status','name'],axis=1)
y=df['status']

#data Splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Model Defination
parkinsons_model=RandomForestClassifier(n_estimators=50)

#model training
parkinsons_model.fit(x_train,y_train)

#prediction model function
def parkinsons_disease_function(MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent,
                                MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                                MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
                                MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1,
                                spread2, D2, PPE):
    # Create a DataFrame for the input data
    input_data_parkinsons = {
        'MDVP:Fo(Hz)': [MDVP_Fo_Hz],
        'MDVP:Fhi(Hz)': [MDVP_Fhi_Hz],
        'MDVP:Flo(Hz)': [MDVP_Flo_Hz],
        'MDVP:Jitter(%)': [MDVP_Jitter_percent],
        'MDVP:Jitter(Abs)': [MDVP_Jitter_Abs],
        'MDVP:RAP': [MDVP_RAP],
        'MDVP:PPQ': [MDVP_PPQ],
        'Jitter:DDP': [Jitter_DDP],
        'MDVP:Shimmer': [MDVP_Shimmer],
        'MDVP:Shimmer(dB)': [MDVP_Shimmer_dB],
        'Shimmer:APQ3': [Shimmer_APQ3],
        'Shimmer:APQ5': [Shimmer_APQ5],
        'MDVP:APQ': [MDVP_APQ],
        'Shimmer:DDA': [Shimmer_DDA],
        'NHR': [NHR],
        'HNR': [HNR],
        'RPDE': [RPDE],
        'DFA': [DFA],
        'spread1': [spread1],
        'spread2': [spread2],
        'D2': [D2],
        'PPE': [PPE]
    }
    input_df_parkinsons = pd.DataFrame(input_data_parkinsons,index=[0])

    # Predict using the model
    parkinsons_predicted = parkinsons_model.predict(input_df_parkinsons)
    if parkinsons_predicted[0] == 1:
        return "⚠️ Based on the model's analysis, there is a high likelihood of Parkinson's disease. 🧠 Please consult a neurologist or healthcare professional for a detailed assessment and further advice."
    else:
        return "✅ The model predicts no significant likelihood of Parkinson's disease at this time. 🌿 Maintaining a healthy lifestyle and staying active is always beneficial!"


#print(parkinsons_disease_function(116.014,141.781,110.655,0.01284,0.00011,0.00655,0.00908,0.01966,0.06525,0.584,0.0349,0.04825,0.04465,0.1047,0.01767,19.649,0.417356,0.823484,-3.74779,0.234513,2.33218,0.410335))
