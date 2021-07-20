#IMPORTANT: Make sure that 2 blank lines separate each function to keep it PEP8 compliant.

import os #From the standard Python library
from flask import Flask, render_template #Import Flask class after installing Flask in terminal, template renders HTML code from server

app = Flask(__name__)
"""
Create instance of Flask class and store it in variable called "app".
The first argument of the Flask class is the name of the application's module - our package.
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files. 
"""

@app.route("/")
def index():
    """
    Use route decorator (also called pie-notation) to tell Flask what URL should trigger the index() 
    function. (Decorators wrap functions)
    When we go to the "/" on the top-level of our domain, it returns the template from our index() 
    function. 
    The route decorator binds the index() function to itself, so that whenever that root is called, 
    the function (or the view) is called.
    """
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    """
    "__main:__" is the name of the default mode in Python. This is the first one that we run, 
    so if this has not been imported, which it won't be, then it's going to be run directly.
    Then we want to run our app using the arguments that we've passing inside of this statement:

    We're using the os module (line 1) from the standard library to get the 'IP' environment variable
    if it exists, but set a default value if it's not found.

    Casting "PORT" it as an integer and set that default to "5000", which is a common port used 
    by Flask.

    **IMPORTANT**:
    Have "debug = True" only when testing this application in development mode.
    Change it to "debug = False" before submitting the project.
    """
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #
        debug = True #Allows us to easily debug code during the development stage
    )
    