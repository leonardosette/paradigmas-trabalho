from flask import Blueprint, jsonify, request
from models.hero import Hero
from utils.battle_simulator import BattleSimulator
from config import SessionLocal

battle_bp = Blueprint('battle', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@battle_bp.route('/battle', methods=['POST'])
def start_battle():
    db = next(get_db())
    data = request.get_json()
    hero1 = db.query(Hero).filter(Hero.hero_id == data['hero1_id']).first()
    hero2 = db.query(Hero).filter(Hero.hero_id == data['hero2_id']).first()

    if not hero1 or not hero2:
        return jsonify({"error": "Um ou ambos os heróis não foram encontrados"}), 404

    result = BattleSimulator.simulate_battle(hero1, hero2)
    db.commit()  # Atualiza as vitórias e derrotas no banco de dados
    return jsonify(result)
