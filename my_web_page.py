import flask
from flask import Flask,render_template

mywebpage = Flask(__name__) # flask class object

@mywebpage.route("/")     #using the routing method like a /home /contacts /about

def my_welcome_page():
    return render_template("index.html")
    
@mywebpage.route("/about")     #using the routing method like a /home /contacts /about

def my_about_page():
    return render_template("about.html")

@mywebpage.route("/contact")

def my_contact_page():
    return render_template("contact.html")

@mywebpage.errorhandler(404)

def my_error_page(err):
    return render_template("error.html")

@mywebpage.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404
    
    
if __name__=="__main__":
    mywebpage.run(host="127.0.0.2",port=5001,debug=True)
