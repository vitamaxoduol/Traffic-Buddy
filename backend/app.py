from ext import db, app
from register_routes import register_routes
from config import Config




if __name__ == '__main__':
    with app.app_context():
        register_routes(app, db)
        db.create_all()
        app.run(port=8010, debug=True)