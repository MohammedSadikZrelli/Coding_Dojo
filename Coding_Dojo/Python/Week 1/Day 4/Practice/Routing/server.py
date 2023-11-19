from flask import Flask

app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')          
def dojo():
    return 'Dojo!' 

@app.route('/say/<name>')          
def Hi(name):
    return f"Hello {name}"

@app.route('/repeat/<int:id>/<name>')          
def repeat(id,name):
    return f"{name} " * id 

@app.errorhandler(404) 
def non_existant_route(error):
   return "Sorry! No response. Try again"


if __name__=="__main__":  
    app.run(debug=True)