import os
import json
from flask import Flask, render_template        #std imprting flask class and render template so we can start to use html seperatley form code

app = Flask(__name__)                           #std    creating an instance of the class with the variable name app 

#defining our index file 
@app.route("/")                                 # std deocrator when we browse to the route "/" triggers the function below index
def index():
    return render_template("index.html")        # std  It expects index.html to be in a templates folder 


@app.route("/about")                                 # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def about():
    thorindata =[]                                #empty array to hold values when json file is read in  
    with open("/data/company.json", "r") as json_data:    #std to open the json file
        thorindata = json.load(json_data)               #std to assignt he json data to our array

    return render_template("about.html", page_title="About", company_data_from_json=throrindata)        #companyvar is creating a new variable to hold the json values that we cna pass through   


@app.route("/contact")                                 # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def contact():
    return render_template("contact.html", page_title="contact")        

@app.route("/careers")                                 # std deocrator and routes--- when we browse to the route "/about" triggers the function below about 
def careers():
    return render_template("careers.html", page_title="careers")  


if __name__ =="__main__":                       #std 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)                                  # NOTE debug = True should never be set to True in Prodcution 
    
