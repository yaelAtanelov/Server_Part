from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = 'Ya14022@L'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)



@app.route('/')
def biginner():
    return redirect(url_for('homePage'))


@app.route('/homePage')
def homePage():
    return render_template('homePage.html', )


@app.route('/ContactMe')
def ContactMe():
    return render_template('ContactMe.html', )

@app.route('/songsRout')
def assignment3_1Rout():
    return redirect('/songs')


@app.route('/songs')
def assignment3_1():
    my_name = 'Yael'
    my_age= -23.6
    my_songs = ['Feeling Me', 'Fuck you by CeeLo Green ', '21 Guns', 'Plot Twist', 'September Song', 'Bruises']
    return render_template('assignment3_1.html', my_name=my_name,
                           my_age=my_age,
                           my_songs=my_songs)


users_catalog = {
    'User_1': {'id': '318601212', 'email': 'ytzhaky@co.il', 'firstname': 'yael', 'lastname': 'itzhaky', 'fav_song':'Wild West', 'password': '1234'},
    'User_2': {'id': '318233457', 'email': 'ytzhaky1@co.il', 'firstname': 'tali', 'lastname': 'atanelov', 'fav_song': 'Do I Wanna Know?', 'password': '3354'},
    'User_3': {'id': '318606669', 'email': 'atanelov@post.bgu.com',  'firstname': 'avi', 'lastname': 'atanelov', 'fav_song': 'ZikI Ziki', 'password': '1255'},
    'User_4': {'id': '323406217', 'email': 'shoham@gimal.com',  'firstname': 'shoham', 'lastname': 'harif', 'fav_song': 'Mi Zot', 'password': '7893'},
    'User_5': {'id': '318611117', 'email': 'salsa@co.il',  'firstname': 'yarden', 'lastname': 'sallllsa', 'fav_song': 'Salsa song', 'password': '5555'},
    'User_6': {'id': '318698646', 'email': 'maximilan@co.il',  'firstname': 'shacham', 'lastname': 'tal', 'fav_song': 'shalosh Banot', 'password': '1998'}
}


@app.route('/RegisterCatalog')
def assignment3_2():
    if 'user_id' in request.args:
        user_id = request.args['user_id']
        user_email = request.args['user_email']
        if not user_id:
            return render_template('assignment3_2.html',
                                   users_catalog=users_catalog,
                                   message='Please fill in all the fields ')
        if not user_email:
            return render_template('assignment3_2.html',
                                   users_catalog=users_catalog,
                                   message='Please fill in all the fields ')
        for key in users_catalog:
            if user_id.__eq__(users_catalog[key]['id']):
                if user_email.__eq__(users_catalog[key]['email']):
                    return render_template('assignment3_2.html',
                                           user_num=key,
                                           user_name=users_catalog[key]['firstname'],
                                           last_name=users_catalog[key]['lastname'],
                                           user_email=user_email,
                                           user_song=users_catalog[key]['fav_song'])
                else:
                    return render_template('assignment3_2.html',
                                           message='Wrong email, please try again')
        return render_template('assignment3_2.html',
                                   message='User not found, please try again ')
    else:
        return render_template('assignment3_2.html',
                           users_catalog=users_catalog)



@app.route('/RegisterCatalog', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        email = request.form['Email']
        id = request.form['ID']
        fav_song = request.form['Fav_Song']
        password = request.form['password']
        for key in users_catalog:
            if id.__eq__(users_catalog[key]['id']):
                return render_template('assignment3_2.html',
                                       registration_message='Your ID is in the system!')
            if email.__eq__(users_catalog[key]['email']):
                return render_template('assignment3_2.html',
                                       registration_message='Your Email is in the system!')

        user_num = "User_{}".format(len(users_catalog)+1)
        print(user_num)
        users_catalog[user_num] = {'id': id, 'email': email, 'firstname': firstname, 'lastname': lastname, 'fav_song': fav_song, 'password': password}
        session['username'] = firstname
        session['logedin'] = True
        return render_template('assignment3_2.html',
                                       registration_message='Congratulations! Youre in the system! What would you like to do now?',
                                       user_name = firstname,
                                       users_catalog=users_catalog)
    return render_template('assignment3_2.html', )

@app.route('/logout')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect('/RegisterCatalog')


if __name__ == '__main__':
    app.run()
