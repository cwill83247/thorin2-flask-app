import os
import json
from flask import Flask, render_template, request, flash        #std imprting flask class and render template and request library so we can start to use html seperatley form code
if os.path.exists("env.py"):
    import env                                  #importing env.py so can be used     

app = Flask(__name__)                           #std    creating an instance of the class with the variable name app 
app.secret_key = os.environ.get("SECRET_KEY")   #getting key from env.py

#defining our index file 
@app.route("/")                                 # std deocrator when we browse to the route "/" triggers the function below index
def index():
    return render_template("index.html")        # std  It expects index.html to be in a templates folder 


@app.route("/about")                                 # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def about():
    cwdata =[]                                #empty array to hold values when json file is read in  
    with open("data/company.json", "r") as json_data:    #std to open the json file
        cwdata = json.load(json_data)               #std to assign the json data to our array

    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3], company_data_from_json=cwdata)        #creating a new variable to hold the json values that we can pass through  to html page  

@app.route("/about/<member_name>")            # creating route <member_name> is a variable to hold the url value that gets passed to it
def about_member(member_name):              # creating function "about_member"   and our view we are passing in membername from the url above.which relates to the character..
    member = {}
    with open("data/company.json", "r") as json_data:    #std to open the json file
        chrisdata = json.load(json_data)               #std to assign the json data to our array
        for obj in chrisdata:                           #loop through chris data
            if obj["url"] == member_name:               # if the membername passed in from the url matches the url in our json file
                member = obj                            # if condition above is met its a match effectivley so return the data using template as per below    
    return render_template("member.html", member=member)   #??? lost with the member=member  1st member is one being passed to the member.html file  2nd member is from here the member variable. unsure how other one fits in..       

                                                     
@app.route("/contact", methods=["GET", "POST"])              #methods = so page will accept GET and POST requests,   # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received the message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="contact")       

@app.route("/careers")                                 # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def careers():
    return render_template("careers.html", page_title="careers")  


if __name__ =="__main__":                       #std 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)                                  # NOTE debug = True should never be set to True in Prodcution 
    
