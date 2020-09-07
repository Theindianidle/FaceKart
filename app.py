from flask import Flask, render_template
from main_algo import Main


app = Flask(__name__)
m = Main()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ads")
def ads():
    return render_template('ads.html')

if __name__ == "__main__":
    app.run(debug=True)