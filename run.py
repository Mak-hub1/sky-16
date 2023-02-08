import prettytable
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.dao import database
from app.api.views import api_blueprint
from app.dao.app_dao import AppDAO


app = Flask(__name__)
app.register_blueprint(api_blueprint)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found_404(error: Exception) -> str:
    '''Catch 404 error'''
    print(error)
    return render_template("404.html")


@app.errorhandler(500)
def not_found_500(error: Exception) -> str:
    '''Catch 500 error'''
    print(error)
    return render_template("500.html")


def debug_method():
    session = database.db.session()
    cursor = session.execute(f"SELECT * from {database.User.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {database.Order.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {database.Offer.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)


appDAO = AppDAO()

if __name__ == '__main__':
    database.setup_database()
    app.run(debug=True)


