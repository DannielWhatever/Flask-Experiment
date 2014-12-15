from flask import Flask
from flask import render_template
# El constructor es Flask :3
app = Flask(__name__)

@app.route("/") # es un decorador. La aplicacion está escuchando la la url "/"
def index():
	return "HOME :3"

@app.route("/hello") # es un decorador. La aplicacion está escuchando la la url "/"
@app.route("/hello/<name>") # una funcion atiende a dos url :OOOO!!!!
def hello(name=None): # el atributo por defecto es nulo, por lo que se puede invocar la funcion sin la variabla :3 
					  # (por eso se puede hacer lo de mas arriba)
	return render_template('/hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
	return "User %s" % (username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % (post_id)

if __name__ == "__main__":
	# Î  Esto se ejecutará SSI es el archivo principal el que se usa
	# Si importamos esto en otro archivo esta linea no se va a ejecutar.
	app.run(debug=True) # constructor de Flask, es como instanciar en java :3, app es una instancia de la clase Flask y uno de los métodos es run().
