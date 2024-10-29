from flask import Blueprint, jsonify, request
from models.mission import Mission
from config import SessionLocal

mission_bp = Blueprint('missions', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@mission_bp.route('/missions', methods=['POST'])
def create_mission():
    db = next(get_db())
    data = request.get_json()
    new_mission = Mission(**data)
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)
    return jsonify({"message": "Missão criada com sucesso!", "missao": new_mission.nome_missao})

@mission_bp.route('/missions', methods=['GET'])
def list_missions():
    db = next(get_db())
    missions = db.query(Mission).all()
    return jsonify([{"nome_missao": mission.nome_missao, "nivel_dificuldade": mission.nivel_dificuldade, "resultado": mission.resultado} for mission in missions])

@mission_bp.route('/missions/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    db = next(get_db())
    data = request.get_json()
    mission = db.query(Mission).filter(Mission.mission_id == mission_id).first()
    if not mission:
        return jsonify({"error": "Missão não encontrada"}), 404
    for key, value in data.items():
        setattr(mission, key, value)
    db.commit()
    return jsonify({"message": "Missão atualizada com sucesso!"})

@mission_bp.route('/missions/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    db = next(get_db())
    mission = db.query(Mission).filter(Mission.mission_id == mission_id).first()
    if not mission:
        return jsonify({"error": "Missão não encontrada"}), 404
    db.delete(mission)
    db.commit()
    return jsonify({"message": "Missão removida com sucesso!"})
