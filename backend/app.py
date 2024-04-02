from ext import Flask, jsonify, request, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic_buddy.db'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)