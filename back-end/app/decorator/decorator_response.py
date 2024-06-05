from flask import jsonify, make_response

def standard_response(func):
    def wrapper(*args, **kwargs):
        # Chamada do método original
        result = func(*args, **kwargs)

        # Verifica se o resultado é uma tupla (payload, status)
        payload = result

        # Verifica se o payload é serializável
        if isinstance(payload, (dict, list)):
            # Retorna uma resposta JSON com os dados do payload e o código de status
            response = jsonify({'message': 'Teste', 'payload': payload, 'success': True})
        else:
            # Se o payload não for serializável, converte-o para string
            response = jsonify({'message': 'Teste', 'payload': str(payload), 'success': True})

        return response

    return wrapper
