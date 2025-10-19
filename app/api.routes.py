from flask import Blueprint, jsonify ,request
from .models import Cliente,Atendimento,Servico,Profissional, db

api_bp= Blueprint('api',__name__,url_prefix='/api')


@api_bp.route('/cadastrar-cliente', methods=['POST'])
def create_cliente():
    dados = request.get_json()
    if not dados or 'usuario' not in dados:
        return jsonify({'erro': 'O campo usuario é obrigatorio'}), 400

    novo_cliente = Cliente(
        nome_usuario=dados['usuario'],
        telefone=dados.get('telefone'),
        cpf=dados.get('cpf'),
        done=dados.get('concluida', False)
    )
    db.session.add(novo_cliente)
    db.session.commit()
@api_bp.route('/consultar-clientes',methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    clientes_list = [
        {'id': cliente.id, 'usuario': cliente.nome_usuario, 'telefone': cliente.telefone, 'cpf': cliente.cpf,
         'concluido': cliente.done}
        for cliente in clientes
    ]
    return jsonify(clientes_list)
    
    

    
@api_bp.route('/excluir-cliente/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensagem': f'Cliente {cliente_id} excluído com sucesso.'}), 200

@api_bp.route('/fazer-atendimento', methods=['POST'])
def create_atendimento():
    dados = request.get_json()
    if not dados or not 'profissional_id'in dados:
        return jsonify({'erro': 'O campo titulo é obrigatorio'}),400
    
    novo_atendimento=Atendimento(
        cliente_id=dados.get('cliente_id'),
        servico_id=dados.get('servico_id'),
        observacoes=dados.get('descricao',''),
        done=dados.get('concluida',False),
        data=dados.get('data'),
        profissional_id=dados.get('profissional_id')
    )
    db.session.add(novo_atendimento)
    db.session.commit()

    return jsonify({'id':novo_atendimento.id,'profissional_id':novo_atendimento.profissional_id}),201
@api_bp.route('/consultar-atendimentos',methods=['GET'])
def get_atendimentos():
    atendimentos = Atendimento.query.all()
    atendimentos_list = [
        {'id': atendimento.id, 'profissional_id': atendimento.profissional_id, 'cliente_id': atendimento.cliente_id,
         'servico_id': atendimento.servico_id, 'data': atendimento.data, 'observacoes': atendimento.observacoes,
         'concluido': atendimento.done}
        for atendimento in atendimentos
    ]
    return jsonify(atendimentos_list)
    
@api_bp.route('/excluir-atendimento/<int:atendimento_id>', methods=['DELETE'])
def delete_atendimento(atendimento_id):
    atendimento = Atendimento.query.get_or_404(atendimento_id)
    db.session.delete(atendimento)
    db.session.commit()
    return jsonify({'mensagem': f'Atendimento {atendimento_id} excluído com sucesso.'}), 200
@api_bp.route('/cadastrar-servico', methods=['POST'])
def create_servico():
    dados = request.get_json()
    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'O campo titulo é obrigatorio'}), 400

    novo_servico = Servico(
        nome=dados['nome'],
        descricao=dados.get('descricao', ''),
        done=dados.get('concluida', False),
        valor=dados.get('valor')
    )

    db.session.add(novo_servico)
    db.session.commit()

    return jsonify({'id': novo_servico.id, 'titulo': novo_servico.title}), 201
@api_bp.route('/consultar-servicos',methods=['GET'])
def get_servicos():
    servicos = Servico.query.all()
    servicos_list = [
        {'id': servico.id, 'nome': servico.nome, 'descricao': servico.descricao, 'valor': servico.valor,
         'concluido': servico.done}
        for servico in servicos
    ]
    return jsonify(servicos_list)
    
    
@api_bp.route('/excluir-servico/<int:servico_id>', methods=['DELETE'])
def delete_servico(servico_id):
    servico = Servico.query.get_or_404(servico_id)
    db.session.delete(servico)
    db.session.commit()
    return jsonify({'mensagem': f'Servico {servico_id} excluído com sucesso.'}), 200

@api_bp.route('/cadastro-profissional', methods=['POST'])
def cadastrar_profissional():
    dados = request.get_json()
    if not dados or 'nome_profissional' not in dados:
        return jsonify({'erro': 'O campo nome_profissional é obrigatorio'}),400
    novo_profissional=Profissional(
        nome_profissional=dados['nome_profissional'],
        cpf=dados.get('cpf'),
        email=dados.get('email'),
        senha=dados.get('senha'),
        telefone=dados.get('telefone'),
        endereco=dados.get('endereco'),
        numero=dados.get('numero'),
        cep=dados.get('cep'),
        cidade=dados.get('cidade'),
        sexo=dados.get('sexo'),
        salario=dados.get('salario'),
        observacoes=dados.get('observacoes','')
    )
    db.session.add(novo_profissional)
    db.session.commit()
    
   
    return jsonify({'mensagem':'Usuário cadastrado com sucesso!'}),201
@api_bp.route('/fazer-login-profissioal', methods=['POST'])
def fazer_login_profissional():
    dados = request.get_json()
    if not dados or 'email' not in dados or 'senha' not in dados:
        return jsonify({'erro': 'Os campos email e senha são obrigatórios'}),400
    
    profissional = Profissional.query.filter_by(email=dados['email']).first()
    if profissional and profissional.senha == dados['senha']:
        return jsonify({'mensagem':'Login realizado com sucesso!','profissional_id':profissional.id}),200
    else:
        return jsonify({'erro':'Email ou senha inválidos!'}),401
@api_bp.route('/logout', methods=['POST'])
def fazer_logout():
    return jsonify({'mensagem':'Logout realizado com sucesso!'}),200
@api_bp.route('/perfil-profissional/<int:profissional_id>', methods=['GET'])
def perfil_profissional(profissional_id):
    profissional = Profissional.query.get_or_404(profissional_id)
    perfil = {
        'id': profissional.id,
        'nome_profissional': profissional.nome_profissional,
        'cpf': profissional.cpf,
        'email': profissional.email,
        'telefone': profissional.telefone,
        'endereco': profissional.endereco,
        'numero': profissional.numero,
        'cep': profissional.cep,
        'cidade': profissional.cidade,
        'sexo': profissional.sexo,
        'salario': str(profissional.salario),
        'observacoes': profissional.observacoes
    }
    return jsonify(perfil)
@api_bp.route('/excluir-profissional/<int:profissional_id>', methods=['DELETE'])
def delete_profissional(profissional_id):
    profissional = Profissional.query.get_or_404(profissional_id)
    db.session.delete(profissional)
    db.session.commit()
    return jsonify({'mensagem': f'Profissional {profissional_id} excluído com sucesso.'}), 200


    
    


