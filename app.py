from flask import Flask, request,render_template  # import main Flask class and request object
import random
import pickle
import pandas as pd
from pycaret.classification import *
# app = Flask(__name__)
# model = pickle.load(open('C:\Users\arjun\endml\rcf.pkl','rb'))
#model = load_model('Random Forest Classifier.pkl','rb')
model = load_model('Random Forest Classifier')
#model = pickle.load(open('Random Forest Classifier.pkl','rb'))

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/result.html",methods=['POST'])
def predict_placement():
    tenure = float(request.form.get('tenure'))
    nod = int(request.form.get('nod'))
    ss = int(request.form.get('ss'))
    complain = int(request.form.get('complain'))
    dslo = float(request.form.get('dslo'))
    cba = int(request.form.get('cba'))
    

# ['Tenure','NumberOfDeviceRegistered','SatisfactionScore', 'Complain','DaySinceLastOrder','CashbackAmount']

    # prediction
    # result = model.predict(np.array([tenure,nod,ss,complain,dslo,cba]).reshape(1,6))
    val = model.predict(pd.DataFrame([(tenure,nod,ss,complain,dslo,cba)],columns=['Tenure','NumberOfDeviceRegistered','SatisfactionScore', 'Complain','DaySinceLastOrder','CashbackAmount']))
    
    result = int(val[0])
    #return 'hello'
    if result == 1:
        result = 'Churn'
    else:
        result = 'Not Churn'

    return render_template('result.html',result=result)
    #return result


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
