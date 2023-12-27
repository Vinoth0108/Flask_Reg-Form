from flask import Flask , render_template,request,redirect
app = Flask( __name__ )

@app.route("/")
def index( ):
    return render_template("register.html")
@app.route("/register", methods=['POST','GET'])

def register( ):
 
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        address = request.form.get('address')
        contact = request.form.get('contact')
 
        return render_template("result.html" , name=name , age=age , city=city , address=address , contact=contact)
if __name__ == "__main__":
    app.run(debug=True)
