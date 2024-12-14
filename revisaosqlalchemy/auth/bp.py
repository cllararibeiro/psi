from flask_login import LoginManager, login_user, logout_user
from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.user import User
from database import session
from werkzeug.security import check_password_hash

auth_bp = Blueprint(name="auth", import_name=__name__, url_prefix='/auth', template_folder='templates')

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter(User.id == user_id).first()

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome=nome, email=email, senha=senha)
        session.add(user)
        session.commit()
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        user = session.query(User).filter(User.email == email).first()
        
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('users.index'))
        else:
            flash('Credenciais inválidas, tente novamente.')
        
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
