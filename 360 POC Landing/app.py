from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
 

@app.route('/')
def hello_world():
    return render_template('index.html')

 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()