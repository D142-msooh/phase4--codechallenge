from flask import Flask, request, jsonify
try:
    from flask_migrate import Migrate
except Exception:
    class Migrate:
        def __init__(self, *args, **kwargs):
            pass

try:
    from flask_mail import Mail, Message
except Exception:
    class Mail:
        def __init__(self, *args, **kwargs):
            pass
        

    class Message:
        def __init__(self, subject=None, recipients=None, body=None):
            self.subject = subject
            self.recipients = recipients or []
            self.body = body
from models import db, Hero, Power, HeroPower
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers'))), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict(only=('id', 'name', 'description')) for power in powers]), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    try:
        if 'description' in data:
            power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data.get('strength'),
            hero_id=data.get('hero_id'),
            power_id=data.get('power_id')
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict(only=('id', 'hero_id', 'power_id', 'strength', 'hero', 'power'))), 201
    except (ValueError, KeyError) as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    try:
        msg = Message(
            subject=data.get('subject', 'Test Email'),
            recipients=[data.get('recipient')],
            body=data.get('body', 'This is a test email from Flask Superheroes API')
        )
        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)
