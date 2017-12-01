from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo():
    return render_template('dojos.html')

@app.route('/process', methods=["POST"])
def dojos():
    print "this is a post route"
    return redirect('/')



app.run(debug=True)