from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name) 