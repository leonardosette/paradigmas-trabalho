from flask import Blueprint, jsonify, request
from models.crime import Crime
from config import SessionLocal

crime_bp = Blueprint('crimes', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@crime_bp.route('/crimes', methods=['POST'])
def create_crime():
    db = next(get_db())
    data = request.get_json()
    new_crime = Crime(**data)
    db.add(new_crime)
    db.commit()
    db.refresh(new_crime)
    return jsonify({"message": "Crime registrado com sucesso!", "crime": new_crime.nome_crime})

@crime_bp.route('/crimes', methods=['GET'])
def list_crimes():
    db = next(get_db())
    crimes = db.query(Crime).all()
    return jsonify([{"nome_crime": crime.nome_crime, "data_crime": crime.data_crime, "severidade": crime.severidade} for crime in crimes])

@crime_bp.route('/crimes/<int:crime_id>', methods=['PUT'])
def update_crime(crime_id):
    db = next(get_db())
    data = request.get_json()
    crime = db.query(Crime).filter(Crime.crime_id == crime_id).first()
    if not crime:
        return jsonify({"error": "Crime não encontrado"}), 404
    for key, value in data.items():
        setattr(crime, key, value)
    db.commit()
    return jsonify({"message": "Crime atualizado com sucesso!"})

@crime_bp.route('/crimes/<int:crime_id>', methods=['DELETE'])
def delete_crime(crime_id):
    db = next(get_db())
    crime = db.query(Crime).filter(Crime.crime_id == crime_id).first()
    if not crime:
        return jsonify({"error": "Crime não encontrado"}), 404
    db.delete(crime)
    db.commit()
    return jsonify({"message": "Crime removido com sucesso!"})
