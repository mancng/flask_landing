#-------------------------------------------
# Landing Page Assignment
#-------------------------------------------

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

app.run(debug=True)


#-------------------------------------------
# What's My Name Assignment
#-------------------------------------------

# from flask import Flask, render_template, redirect, request
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('dojos.html')

# @app.route('/process', methods=["POST"])
# def dojos():
#     my_data = request.form['name']
#     print my_data
#     return redirect('/')

# app.run(debug=True)