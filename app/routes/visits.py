from flask import Blueprint, request, jsonify

visits_bp = Blueprint('visits', __name__)

# Mock database
database = {}
visit_id_counter = 1

@visits_bp.route('/visits', methods=['POST'])
def create_visit():
    global visit_id_counter
    data = request.json
    database[visit_id_counter] = data
    visit_id_counter += 1
    return jsonify({'visit_id': visit_id_counter - 1}), 201

@visits_bp.route('/visits/<int:visit_id>', methods=['GET'])
def get_visit(visit_id):
    visit = database.get(visit_id)
    if visit:
        return jsonify(visit), 200
    return jsonify({'message': 'Visit not found'}), 404

@visits_bp.route('/visits/<int:visit_id>', methods=['PUT'])
def update_visit(visit_id):
    data = request.json
    if visit_id in database:
        database[visit_id].update(data)
        return jsonify({'message': 'Visit updated'}), 200
    return jsonify({'message': 'Visit not found'}), 404

@visits_bp.route('/visits/<int:visit_id>', methods=['DELETE'])
def delete_visit(visit_id):
    if visit_id in database:
        del database[visit_id]
        return jsonify({'message': 'Visit deleted'}), 200
    return jsonify({'message': 'Visit not found'}), 404
