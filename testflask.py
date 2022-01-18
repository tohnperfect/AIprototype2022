from flask import Flask

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

    
if __name__ == "__main__":
    app.run(host='0.0.0.0')#host='0.0.0.0'