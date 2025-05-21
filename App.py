from flask import Flask,render_template
app= Flask(__name__)
@app.route('/') ## decorator
def index():
    fruits=["apple","orange","grapes","lemon"]
    return render_template("index.html",items = fruits)



@app.route('/users') 
def users():
    users=["hanna","albuu","ammu"]
    return render_template("users.html",users=users)
if __name__ =='__main__':
    app.run(debug = True)
   