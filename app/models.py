from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(14), nullable=False)
    nome_usuario = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(19), nullable=False)

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(300), nullable=False)
    descricao = db.Column(db.String(300))
    valor = db.Column(db.DECIMAL(10,2), nullable=False)

class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    observacoes = db.Column(db.String(300), nullable=False)

class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(14), nullable=False)
    nome_profissional = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(19), nullable=False)
    endereco = db.Column(db.String(60), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    salario = db.Column(db.DECIMAL(10,2), nullable=False)
    observacoes = db.Column(db.String(300), nullable=False)
   