Hello i have created a website something like this, feel free to check this out.
code: 
from flask import Flask, render_template,request
import predict

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        if request.method == "POST":
            pregnancies = request.form.get("pregnancies")
            glucose = request.form.get("glucose")
            bloodpressure = request.form.get("bloodpressure")
            skinthickness = request.form.get("skinthickness")
            insulin = request.form.get("insulin")
            bmi = request.form.get("bmi")
            dpfunc = request.form.get("dpfunc")
            age = request.form.get("age")
            model = request.form.get("model")

            result = predict.predict(
                pregnancies, 
                glucose, 
                bloodpressure, 
                skinthickness, 
                insulin,
                bmi,
                dpfunc,
                age,
                model
            )
            
            if result == 1:
                message = "It seems you may have Diabetes, Consult your Doctor!"
            else:
                message= "It seems you are free from Diabates. Eat Healthy and Stay Healthy!"
            return render_template("index.html", data = [{"msg":message}])
    except:
        return "Please check if values are entered correcty"
    return render_template("index.html")


if __name__ == "__main__":
    app.run()




