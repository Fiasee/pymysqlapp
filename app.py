from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='.')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bob'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['fname']
        favcolor = details['fcolor']
        pets = details['fpets']
        cur = mysql.connection.cursor()
        cur.execute("SELECT name FROM MyUsers WHERE name=%s", (name, ))
        result = cur.fetchone()
        if result is not None:
            return 'failed: name already exists'
        else:
            cur.execute("INSERT INTO MyUsers(name, favcolor, pets) VALUES (%s, %s, %s)", (name, favcolor, pets))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()