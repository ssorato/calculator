from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET','POST'])
def result():
    if request.method == 'POST':
      n1 = request.form.get("number1", type=int)
      n2 = request.form.get("number2", type=int)
      operation = request.form.get("operation")
      if(operation == '+'):
        resp = requests.post(os.environ['API_URL'] + "/sum",
        data={"number1": n1, "number2": n2})
        apiresp = resp.json()
        result = apiresp['result']
      elif(operation == '-'):
        resp = requests.post(os.environ['API_URL'] + "/subtract",
        data={"number1": n1, "number2": n2})
        apiresp = resp.json()
        result = apiresp['result']
      else:
          result = 'invalid operator'
      return render_template('index.html', result=result, number1=n1, number2=n2, oper=operation)
    else:
      return render_template('index.html', result=0, number1=0, number2=0, oper="+")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80) # Run outsite !!!
