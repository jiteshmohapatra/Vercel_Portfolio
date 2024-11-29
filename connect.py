from flask import Flask,render_template #flask is module but this Flask is a class
app = Flask(__name__)

@app.route("/goto")
def hello1():
    return render_template("portfolio.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080, debug=True)


