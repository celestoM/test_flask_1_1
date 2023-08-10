rom flask import Flask,request

app = Flask(__name__)

@app.route("/init", methods=["GET"])
def init():
    return {"payload":"welcome to my project3"}

@app.route("/init/:<content>", methods=["GET"])
def read(content):
    if content=="alfa":
        return {"payload":content}
    else:
        return "No Existe" 

if __name__ == "__Main__":
    app.run(debug=True)
