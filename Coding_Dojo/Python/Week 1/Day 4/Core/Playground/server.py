from flask import Flask,render_template 
app = Flask(__name__)    
@app.route('/play')          
def play():
    return render_template('play.html',x=3)  
@app.route('/play/<int:name>/')          
def playsev(name):
    return render_template('play.html',x=name) 
@app.route('/play/<int:x>/<color>')          
def coulor(x, color):
    return render_template('play.html', color=color, x=x)
if __name__=="__main__":   
    app.run(debug=True) 

