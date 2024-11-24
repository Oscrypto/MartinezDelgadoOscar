from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
database = {}

# Agregar
@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.json
    if 'id' not in data or 'nombre' not in data:
        return jsonify({'error': 'Faltan datos'}), 400
    database[data['id']] = data['nombre']
    return jsonify({'mensaje': 'Registro agregado', 'data': data})

# Buscar
@app.route('/buscar/<id>', methods=['GET'])
def buscar(id):
    if id in database:
        return jsonify({'id': id, 'nombre': database[id]})
    return jsonify({'error': 'Registro no encontrado'}), 404

# Actualizar
@app.route('/actualizar/<id>', methods=['PUT'])
def actualizar(id):
    if id not in database:
        return jsonify({'error': 'Registro no encontrado'}), 404
    data = request.json
    if 'nombre' not in data:
        return jsonify({'error': 'Faltan datos'}), 400
    database[id] = data['nombre']
    return jsonify({'mensaje': 'Registro actualizado', 'id': id, 'nombre': data['nombre']})

# Eliminar
@app.route('/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    if id in database:
        del database[id]
        return jsonify({'mensaje': 'Registro eliminado', 'id': id})
    return jsonify({'error': 'Registro no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
