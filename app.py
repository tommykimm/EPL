from datetime import date, datetime
from flask import Flask, render_template,  redirect, url_for, request
from flask_mysqldb import MySQL
import mysql.connector
from mysqlx import SqlStatement
from PIL import Image
import pymysql

app= Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'practice'
mysql = MySQL(app)

class Database:
# constructing different methods inside class of 'database'
#main
    def __init__(self):
        host = "127.0.0.1"
        user = 'root'
        password = '12345'
        db = 'practice'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()



#main table
    def list_products8(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_8, practice.seasons.years,row_number() over(order by points_8 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '20/21' order by practice.points.points_8 desc;")                            
        result = self.cur.fetchall()
        return result

    def list_winners8(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 0,3;")
        winner = self.cur.fetchall()
        return winner

#header
    def dropdown(self):
        self.cur.execute("SELECT * FROM practice.seasons LIMIT 3,9")
        dropdown=self.cur.fetchall()
        return dropdown

#picture
    def images(self):
        self.cur.execute("SELECT practice.standings.id, practice.standings.seasons, practice.standings.teams, practice.Images.Photo FROM practice.standings join practice.Images ON practice.standings.teams = practice.Images.id where practice.standings.seasons= '8';")
        images=self.cur.fetchall()
        return images 

#comment
    def comment(self, teams_id):
        self.cur.execute("SELECT * from practice.comment WHERE practice.comment.id='"+teams_id+"';")
        comment= self.cur.fetchall()
        return comment

#title
    def title(self, teams_id):
        self.cur.execute("SELECT * from practice.teams WHERE practice.teams.id='"+teams_id+"';")
        title= self.cur.fetchall()
        return title

#colors 
    def colors(self, teams_id):
        self.cur.execute("SELECT * from practice.images2 WHERE practice.images2.id='"+teams_id+"';")
        colors= self.cur.fetchall()
        return colors


#display
    def display(self):
        self.cur.execute("SELECT practice.standings.id, practice.standings.seasons, practice.standings.teams,practice.images2.link from practice.standings join practice.images2 on practice.standings.teams = practice.images2.id where practice.standings.seasons='8';")
        display= self.cur.fetchall()
        return display

#season7
    def list_products7(self, seasons_id, seasons_date):
        # self.seasons_id = seasons_id
        # self.seasons_date = seasons_date
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_"+seasons_id+" AS points, practice.seasons.years, row_number() over(order by points_"+seasons_id+" desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '"+seasons_date+"' order by practice.points.points_"+seasons_id+" desc;")
        result = self.cur.fetchall()
        return result

    def list_winners7(self, seasons_id):
        self.cur.execute("SELECT practice.winners1.id, practice.winners1.seasons, practice.seasons.years2, practice.teams.teams from practice.winners1 join practice.seasons ON practice.winners1.seasons2 = practice.seasons.id join practice.teams ON practice.winners1.winners = practice.teams.id where practice.winners1.seasons='"+seasons_id+"'")
        winner = self.cur.fetchall()
        return winner

    def pictures(self, seasons_id):
        self.cur.execute("SELECT practice.standings.id, practice.standings.seasons, practice.standings.teams, practice.Images.Photo FROM practice.standings join practice.Images ON practice.standings.teams = practice.Images.id where practice.standings.seasons= '"+seasons_id+"';")
        picture = self.cur.fetchall()
        return picture

#arsenal
    def arsenal(self, team_id):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.id = '"+team_id+"' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def arsenalscorers(self, team_id):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.id ='"+team_id+"' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#comment
    def comments(self, id, id_2, comment):
        self.cur.execute("INSERT INTO practice.astonvilla(id, comment_"+id+") VALUES ("+id_2+", "+comment+"))")

#astonvilla
    def astonvilla_comment2(self,id):
        self.cur.execute("SELECT practice.astonvilla.comment_"+id+" FROM practice.astonvilla")
        result = self.cur.fetchall()
        return result

#astonvilla
def astonvilla_comment(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT practice.astonvilla.comment_"+id+" FROM practice.astonvilla")
    rows = cur.fetchall()
    return rows


@app.route('/')
def index():
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)

#teams page
def arsenal_comment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM arsenal")
    rows = cur.fetchall()
    return rows

@app.route('/teams',methods=['GET', 'POST'])
def arsenals():
    id = request.args.get('id')
    id2 = request.args.get('id')

    def arsenal1(id):
        db = Database()
        products = db.arsenal(id)
        return products

    def arsenalscorers1(id):
        db = Database()
        products = db.arsenalscorers(id)
        return products

    def index(id, id2):
        if request.method == "POST":
            details = request.form
            id = len(astonvilla_comment(id))+1
            comment = details['comment']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO astonvilla(id, comment_"+str(id2)+") VALUES (%s, %s)", (str(id), comment))
            mysql.connection.commit()
            cur.close()
            return 'success'
    
    def commentdata(id):
        db= Database()
        products= db.astonvilla_comment2(id)
        return products

    def textbox(id):
        db=Database()
        products= db.comment(id)
        return products

    def titles(id):
        db = Database()
        products = db.title(id)
        return products
  
    def design(id):
        db = Database()
        products = db.colors(id)
        return products

    res = arsenal1(id)
    win = arsenalscorers1(id)
    value = index(id, id2)
    all_text = astonvilla_comment(id)
    hello= textbox(id)
    title= titles(id)
    designs= design(id)
    data= commentdata(id)
    # color = commentbox(id_1,id_2,comment)

    return render_template("teams.jinja" , data = data, designs= designs, title= title, hello = hello, value= value, all_text= all_text, result = res,  winners= win, ) 


#homepage
@app.route('/homepage')
def homepage():
    def db_query8():
        db = Database()
        products = db.list_products8()
        return products

    def db_query8_1():
        db = Database()
        products = db.list_winners8()
        return products

    def dropdown1():
        db = Database()
        products = db.dropdown()
        return products

    def image():
        db = Database()
        products = db.images()
        return products

    def displayport():
        db=Database()
        products = db.display()
        return products

    res = db_query8()
    win = db_query8_1()
    drop = dropdown1()
    images= image()
    display = displayport()
    return render_template("index.jinja" , display=display, result = res, winner = win, dropdown=drop, images=images, seasons='20/21', team="Manchester City") 


#seasons page
@app.route('/seasonspage')
def product7():
    id = request.args.get('id')
    years = request.args.get('years')
    
    def db_query7(id,years):
        db = Database()
        products = db.list_products7(id, years)
        return products

    def db_query7_1(id):
        db = Database()
        products = db.list_winners7(id)
        return products

    def dropdown1():
        db = Database()
        products = db.dropdown()
        return products

    def display_image(id):
        db=Database()
        products= db.pictures(id)
        return products

    res = db_query7(id,years)
    win = db_query7_1(id)
    drop= dropdown1()
    image= display_image(id)

    return render_template("seasons.jinja" ,result= res, winner= win ,seasons=years, dropdown=drop, image= image)





