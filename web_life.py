from bottle import route, run, get, post, request
import life_game
@route('/goodbye')
def goodbye():
	return "goodbye"

@route('/life')
def life():
	life_game
	
@get('/login')
def login_form():
	return '''<form method="POST" action="/login"> <input name="name" type="text" />
                <input name="password" type="password" />
                <input type="submit" />
              </form>'''
@post('/login')
def login_submit():
	name = request.forms.get('name')
	password = request.forms.get('password')
	if check_login(name, password):
		return "<p>Your login was correct</p>"
	else:
		return "<p>Login failed</p>"



run(host='localhost', port=8080, debug=True)
