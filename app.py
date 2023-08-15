from flask import Flask,request

app = Flask(__name__)

@app.route("/inicio", methods=["GET"])
def inicio():
    return {"payload":"welcome to my project3"}

@app.route("/read/:<content>", methods=["GET"])
def read(content):
    return {"payload":content}

@app.route("/create/:<content>", methods=["POST"])
def create(content):
    return {"payload":content}

@app.route("/init/:<content>", methods=["GET"])
def init(content):
    if content=="echo":
        return {"payload":content}
    else:
        return "No Existe" 

if __name__ == "__Main__":
    app.run(debug=True)