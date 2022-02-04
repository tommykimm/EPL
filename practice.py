from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'practice'

mysql = MySQL(app)

def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MyUsers")
    rows = cur.fetchall()    
    return rows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        comment = details['comment']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(name, comment) VALUES (%s, %s)", (name, comment))
        mysql.connection.commit()
        cur.close()

        all_text = get_data()
        # return 'success'
        print("-->\n", all_text)


    return render_template('practice1.html', all_text = all_text)
  

# @app.route('/action', methods =['GET'])
# def helloworld():
#     print("--------->!!!!!")
#     app.logger.warning('------------>!!!')

#     all_text = get_data()
#     print("--------->",all_text)
#     return render_template('practice1.html', all_text = all_text)
    

if __name__ == '__main__':
    app.run(debug=True)
