from flask import Flask
from routes import blueprints  # Importando todos os Blueprints da pasta routes

app = Flask(__name__)

# Registro de Blueprints
for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
