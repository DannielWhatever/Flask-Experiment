from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index(user=None, passwd=None): # podriamos separar cada if... if (POST){ if(user and paass}, else dale ;D
	try: # 
		if(request.method=='POST'):
			if (request.form['user']=='leo' and request.form['passwd'] == '1313'): # user and pass validos
				return render_template('/hello.html',name=request.form['user'])
			else: # error en usuario y pass
				return render_template('/login.html',error='Usuario invalido')		
		else: # error en method , técnicamente no es un error este
			return render_template('/login.html') 
	except: 
		return render_template('/login.html',error='Error wtf-chan en un try XD')

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template('/hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
	return "User %s" % (username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % (post_id)
	
@app.route('/test')
def test():
	return str(request.form)

if __name__ == "__main__":
	app.run(debug=True)