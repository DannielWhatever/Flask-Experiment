from flask import *

lista = [["leo", "1313","Nada se olvida..."],["belu","123","Desde los edificios..."]]

def getUser(name):
	for user in lista:
		if user[0]==name:
			return user
	return []

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index(user=None, passwd=None):
	lista = [["leo", "1313","Nada se olvida..."],["belu","123","Desde los edificios..."]]

	if(request.method=='POST'):
		for user in lista: # se obtienen todos los campos.. entonces: user[0]: name
			if(request.form['user']==user[0]):
				if(request.form['passwd'] == user[1]):
					#return render_template('/hello.html',user=user) # tratemos de vver si jinja acepta el objeto completo
					resp = make_response(redirect(url_for('users',username=user[0])))
					resp.set_cookie('username', 'leo')
					return resp
				else: # error en usuario y pass
					return render_template('/login.html',error='Usuario invalido')
		return render_template('/login.html',error='Usuario no existe')
	else: # error en method , técnicamente no es un error este
		return render_template('/login.html')

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template('/hello.html', name=name)

@app.route('/users/<username>')
def users(username):
	if(username == request.cookies.get('username')):
		return render_template('/hello.html', user=getUser(username))
	else:
		return "Fuera!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % (post_id)
	
@app.route('/test')
def test():
	return str(request.form)

if __name__ == "__main__":
	app.run(debug=True)
