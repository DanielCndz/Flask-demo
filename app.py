from flask import Flask,  render_template, request

app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)

@app.route('/')

def index():
	return render_template("index.html")

@app.route('/user', methods=["POST"])
def usuario():
	nombre=request.form.get("nombre")
	apellido=request.form.get("apellido")
	edad=request.form.get("edad")
	email=request.form.get("email")
	return render_template("user.html",	nombre=nombre,
		apellido=apellido,
		edad=edad,
		email=email)



