#loading the framework and api's
from flask import Flask,render_template,request

#loading the diabetes prediction model
import dia_model_source
#loading the heart disease prediction model
import heart_model_source
#loading the prankinson's disease prediction model
import prankinsons_model_source

app=Flask(__name__)

#homepage
@app.route("/")
def home():
    return render_template("home.html")

#diabetes page
@app.route("/diabetesprediction",methods=["POST","GET"])
def diabetesprediction():
    if request.method=="POST":
        preg = int(request.form.get('pregnancies', 0))
        gluco = float(request.form.get('glucose', 0))
        bp = float(request.form.get('bloodPressure', 0))
        sthick = float(request.form.get('skinThickness', 0))
        ins = float(request.form.get('insulin', 0))
        bmi = float(request.form.get('bmi', 0))
        pedigree = float(request.form.get('pedigreeFunction', 0))
        age = int(request.form.get('age', 0))

        result=dia_model_source.diabetes_prediction(preg,gluco,bp,sthick,ins,bmi,pedigree,age)
        return render_template("dia_result.html",result=result)
    return render_template("diabetes.html")

#heart page
@app.route("/heartdiseaseprediction",methods=["POST","GET"])
def heartdiseaseprediction():
    if request.method=="POST":
        age=int(request.form['age'])
        sex=int(request.form['sex'])
        cp=float(request.form['cp'])
        trestbps=float(request.form['trestbps'])
        chol=float(request.form['chol'])
        fbs=float(request.form['fbs'])
        restecg=float(request.form['restecg'])
        thalach=float(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=float(request.form['oldpeak'])
        slope=float(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])

        result=heart_model_source.heart_disease_function(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return render_template("heart_result.html",result=result)

    return render_template("heart.html")

#prankinsons page
@app.route("/prankinsonsdiseaseprediction",methods=["POST","GET"])
def prankinsonsdiseaseprediction():
    if request.method=="POST":
        mdvp_fo = float(request.form['mdvp_fo'])
        mdvp_fhi = float(request.form['mdvp_fhi'])
        mdvp_flo = float(request.form['mdvp_flo'])
        mdvp_jitter = float(request.form['mdvp_jitter'])
        mdvp_jitter_abs = float(request.form['mdvp_jitter_abs'])
        mdvp_rap = float(request.form['mdvp_rap'])
        mdvp_ppq = float(request.form['mdvp_ppq'])
        jitter_ddp = float(request.form['jitter_ddp'])
        mdvp_shimmer = float(request.form['mdvp_shimmer'])
        mdvp_shimmer_db = float(request.form['mdvp_shimmer_db'])
        shimmer_apq3 = float(request.form['shimmer_apq3'])
        shimmer_apq5 = float(request.form['shimmer_apq5'])
        mdvp_apq = float(request.form['mdvp_apq'])
        shimmer_dda = float(request.form['shimmer_dda'])
        nhr = float(request.form['nhr'])
        hnr = float(request.form['hnr'])
        rpde = float(request.form['rpde'])
        dfa = float(request.form['dfa'])
        spread1 = float(request.form['spread1'])
        spread2 = float(request.form['spread2'])
        d2 = float(request.form['d2'])
        ppe = float(request.form['ppe'])

        result=prankinsons_model_source.parkinsons_disease_function(mdvp_fo,mdvp_fhi,mdvp_flo,mdvp_jitter,mdvp_jitter_abs,mdvp_rap,mdvp_ppq,jitter_ddp,mdvp_shimmer,mdvp_shimmer_db,shimmer_apq3,shimmer_apq5,mdvp_apq,shimmer_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe)

        return render_template("prankinsons_result.html",result=result)

    return render_template("prankinsons.html")

#health guard page


#main Function --> Where the execution starts from...
if __name__=="__main__":
    app.run(debug=True)#Making debug flag as a true,because it shows the errors whenever there isa bug.
