from flask import Blueprint, jsonify ,request
from .models import Task,Cliente,Atendimento, db

api_bp= Blueprint('api',__name__,url_prefix='/api')
# @api_bp.route('/tarefas',methods=['GET'])
# def get_taferas():
#     tarefas= Task.quere.all()
#     tarefas_list =[
#         {'id':task.id, 'titulo':task.title, 'descricao':task.description,
#           'concluido': task.done}
#     for task in tarefas
#     ]
#     return jsonify(tarefas_list)

@api_bp.route('/cadastrar-cliente', methods=['POST'])
def create_cliente():
    dados = request.get_json()
    if not dados or not 'titulo'in dados:
        return jsonify({'erro': 'O campo titulo é obrigatorio'}),400
    
    novo_cliente=Cliente(
        title=dados['titulo'],
        description=dados.get('descricao',''),
        done=dados.get('conckuida',False)
    )
    db.session.add(novo_cliente)
    db.session.commit()
@api_bp.route('/consultar-clientes',methods=['GET'])
def get_clientes():
    clientes= Cliente.quere.all()   
    clientes_list =[
        {'id':cliente.id, 'titulo':cliente.title, 'descricao':cliente.description,
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
    if not dados or not 'titulo'in dados:
        return jsonify({'erro': 'O campo titulo é obrigatorio'}),400
    
    novo_atendimento=Atendimento(
        title=dados['titulo'],
        description=dados.get('descricao',''),
        done=dados.get('conckuida',False)
    )
    db.session.add(novo_atendimento)
    db.session.commit()

    return jsonify({'id':novo_atendimento.id,'titulo':novo_atendimento.title}),201
@api_bp.route('/consultar-atendimentos',methods=['GET'])
def get_atendimentos():
    atendimentos= Atendimento.quere.all()  '' 
    atendimentos_list =[
        {'id':atendimento.id, 'titulo':atendimento.title, 'descricao':atendimento.description,
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
    if not dados or not 'titulo'in dados:
        return jsonify({'erro': 'O campo titulo é obrigatorio'}),400
    
    novo_servico=Servico(
        title=dados['titulo'],
        description=dados.get('descricao',''),
        done=dados.get('conckuida',False)
    )
    db.session.add(novo_servico)
    db.session.commit()

    return jsonify({'id':novo_servico.id,'titulo':novo_servico.title}),201
@api_bp.route('/consultar-servicos',methods=['GET'])
def get_servicos():
    servicos= Servico.quere.all()   
    servicos_list =[
        {'id':servico.id, 'titulo':servico.title, 'descricao':servico.description,
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

@api_bp.route('/cadastro-usuario', methods=['POST'])
def cadastro_usuario():
    dados = request.get_json()
    usuario=dados.get('usuario')
    email=dados.get('email')
    senha=dados.get('senha')
   
    return jsonify({'mensagem':'Usuário cadastrado com sucesso!'}),201
@api_bp.route('/fazar-login', methods=['POST'])
def fazer_login():
    dados = request.get_json()
    usuario=dados.get('usuario')
    senha=dados.get('senha')
   
    return jsonify({'mensagem':'Login realizado com sucesso!'}),200 




# def create_tarefa():
#     dados = request.get_json()
#     if not dados or not 'titulo'in dados:
#         return jsonify({'erro': 'O campo titulo é obrigatorio'}),400
    
#     nova_tarefa=Task(
#         title=dados['titulo'],
#         description=dados.get('descricao',''),
#         done=dados.get('conckuida',False)
#     )
#     db.session.add(nova_tarefa)
#     db.session.commit()

#     return jsonify({'id':nova_tarefa.id,'titulo':nova_tarefa.title}),201
# @api_bp.route('/update/<int:task_id>')
# def update_tarefas(id):
#     tarefa = Task.query.get_or_404(id)
#     dados=request.get_json()
    
#     tarefa.title=dados.get('titulo', tarefa.tite)
#     tarefa.description= dados.get('descricao', tarefa.description)
#     tarefa.done=dados.get('concluida',tarefa.done)
    
    
#     db.session.commit()           
#     return jsonify({'id':tarefa.id,'titulo':tarefa.title,'concluida':tarefa.done})
