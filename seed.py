from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    print("Clearing database...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()
    
    print("Seeding heroes...")
    heroes = [
        
    ]
    db.session.add_all(heroes)
    
    print("Seeding powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    db.session.add_all(powers)
    db.session.commit()
    
    print("Seeding hero powers...")
    hero_powers = [
        HeroPower(hero_id=1, power_id=2, strength="Strong"),
        HeroPower(hero_id=2, power_id=1, strength="Average"),
        HeroPower(hero_id=3, power_id=3, strength="Weak"),
        HeroPower(hero_id=4, power_id=2, strength="Strong"),
        HeroPower(hero_id=5, power_id=1, strength="Strong"),
        HeroPower(hero_id=6, power_id=2, strength="Average"),
        HeroPower(hero_id=7, power_id=1, strength="Strong"),
        HeroPower(hero_id=8, power_id=3, strength="Average"),
        HeroPower(hero_id=9, power_id=4, strength="Weak"),
        HeroPower(hero_id=10, power_id=1, strength="Average")
    ]
    db.session.add_all(hero_powers)
    db.session.commit()
    
    print("Database seeded successfully!")
