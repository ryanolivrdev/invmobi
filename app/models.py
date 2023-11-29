from datetime import datetime
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = generate_password_hash(password)
        self.name = name

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Scenario(db.Model):
    __tablename__ = "scenarios"
    id = db.Column(db.Integer, primary_key=True)
    property_valuation = db.Column(db.Float, nullable=False)
    financing_rate = db.Column(db.Float, nullable=False)


def get_scenario(scenario_tag):
    return Scenario.query.get(int(scenario_tag))


class historic(db.Model):
    __tablename__ = "historic"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey(
        "scenarios.id"), nullable=False)
    valor_aluguel_imovel = db.Column(db.Float, nullable=False)
    valor_compra_imovel = db.Column(db.Float, nullable=False)
    entrada_imovel = db.Column(db.Float, nullable=False)
    tempo_imovel = db.Column(db.Integer, nullable=False)
    soma_aluguel = db.Column(db.Float, nullable=False)
    total_pago_pela_compra = db.Column(db.Float, nullable=False)
    compensar_aluguel = db.Column(db.Integer, nullable=False)
    opcao = db.Column(db.String(255), nullable=False)
    somatorio_aluguel = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id, scenario_id, valor_aluguel_imovel, valor_compra_imovel, entrada_imovel,
                 tempo_imovel, soma_aluguel, total_pago_pela_compra, compensar_aluguel, opcao,
                 somatorio_aluguel,
                 ):
        self.user_id = user_id
        self.scenario_id = scenario_id
        self.valor_aluguel_imovel = valor_aluguel_imovel,
        self.valor_compra_imovel = valor_compra_imovel,
        self.entrada_imovel = entrada_imovel,
        self.tempo_imovel = tempo_imovel,
        self.soma_aluguel = soma_aluguel,
        self.total_pago_pela_compra = total_pago_pela_compra,
        self.compensar_aluguel = compensar_aluguel,
        self.opcao = opcao,
        self.somatorio_aluguel = somatorio_aluguel
  

