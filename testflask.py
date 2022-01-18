from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")  
def home():
    return "Hello, World!"

@app.route("/name")  
def hellotohn():
    return "Hello, Tohn!"

##api
@app.route('/request',methods=['POST'])
def request_detail():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage)
    
    json_data = json.dumps({'y': 'received!'})
    return json_data
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)#host='0.0.0.0'
