from flask import Flask, render_template
from controllers import users_bp
from auth import auth_bp, login_manager
from database import engine, Base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dificil'  # Usando uma chave secreta para o login

# Inicializando o login_manager
login_manager.init_app(app)

# Registrando Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

# Criando as tabelas no banco de dados (caso não existam)
with app.app_context():
    Base.metadata.create_all(bind=engine)

# Rota inicial
@app.route('/')
def index():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)
