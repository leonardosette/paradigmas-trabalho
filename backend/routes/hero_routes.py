from flask import Blueprint, jsonify, request
from models.hero import Hero
from config import SessionLocal

hero_bp = Blueprint('heroes', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@hero_bp.route('/heroes', methods=['POST'])
def create_hero():
    db = next(get_db())
    data = request.get_json()
    new_hero = Hero(**data)
    db.add(new_hero)
    db.commit()
    db.refresh(new_hero)
    return jsonify({"message": "Herói criado com sucesso!", "heroi": new_hero.nome_heroi})

@hero_bp.route('/heroes', methods=['GET'])
def list_heroes():
    db = next(get_db())
    heroes = db.query(Hero).all()
    return jsonify([{"nome_real": hero.nome_real, "nome_heroi": hero.nome_heroi, "status": hero.status} for hero in heroes])

@hero_bp.route('/heroes/<int:hero_id>', methods=['PUT'])
def update_hero(hero_id):
    db = next(get_db())
    data = request.get_json()
    hero = db.query(Hero).filter(Hero.hero_id == hero_id).first()
    if not hero:
        return jsonify({"error": "Herói não encontrado"}), 404
    for key, value in data.items():
        setattr(hero, key, value)
    db.commit()
    return jsonify({"message": "Herói atualizado com sucesso!"})

@hero_bp.route('/heroes/<int:hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    db = next(get_db())
    hero = db.query(Hero).filter(Hero.hero_id == hero_id).first()
    if not hero:
        return jsonify({"error": "Herói não encontrado"}), 404
    db.delete(hero)
    db.commit()
    return jsonify({"message": "Herói removido com sucesso!"})
