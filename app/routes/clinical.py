from flask import Blueprint, request, jsonify

clinical = Blueprint('clinical', __name__)

# Sample data storage (in-memory for demonstration)
vital_signs = []
conditions = []
heart_failures = []
treatments = []
scores = []

# Vital Signs
@clinical.route('/vital_signs', methods=['POST'])
def create_vital_sign():
    data = request.json
    vital_signs.append(data)
    return jsonify(data), 201

@clinical.route('/vital_signs', methods=['GET'])
def get_vital_signs():
    return jsonify(vital_signs), 200

@clinical.route('/vital_signs/<int:id>', methods=['PUT'])
def update_vital_sign(id):
    data = request.json
    vital_signs[id] = data
    return jsonify(data), 200

@clinical.route('/vital_signs/<int:id>', methods=['DELETE'])
def delete_vital_sign(id):
    vital_signs.pop(id)
    return '', 204

# Conditions
@clinical.route('/conditions', methods=['POST'])
def create_condition():
    data = request.json
    conditions.append(data)
    return jsonify(data), 201

@clinical.route('/conditions', methods=['GET'])
def get_conditions():
    return jsonify(conditions), 200

@clinical.route('/conditions/<int:id>', methods=['PUT'])
def update_condition(id):
    data = request.json
    conditions[id] = data
    return jsonify(data), 200

@clinical.route('/conditions/<int:id>', methods=['DELETE'])
def delete_condition(id):
    conditions.pop(id)
    return '', 204

# Heart Failures
@clinical.route('/heart_failures', methods=['POST'])
def create_heart_failure():
    data = request.json
    heart_failures.append(data)
    return jsonify(data), 201

@clinical.route('/heart_failures', methods=['GET'])
def get_heart_failures():
    return jsonify(heart_failures), 200

@clinical.route('/heart_failures/<int:id>', methods=['PUT'])
def update_heart_failure(id):
    data = request.json
    heart_failures[id] = data
    return jsonify(data), 200

@clinical.route('/heart_failures/<int:id>', methods=['DELETE'])
def delete_heart_failure(id):
    heart_failures.pop(id)
    return '', 204

# Treatments
@clinical.route('/treatments', methods=['POST'])
def create_treatment():
    data = request.json
    treatments.append(data)
    return jsonify(data), 201

@clinical.route('/treatments', methods=['GET'])
def get_treatments():
    return jsonify(treatments), 200

@clinical.route('/treatments/<int:id>', methods=['PUT'])
def update_treatment(id):
    data = request.json
    treatments[id] = data
    return jsonify(data), 200

@clinical.route('/treatments/<int:id>', methods=['DELETE'])
def delete_treatment(id):
    treatments.pop(id)
    return '', 204

# Scores
@clinical.route('/scores', methods=['POST'])
def create_score():
    data = request.json
    scores.append(data)
    return jsonify(data), 201

@clinical.route('/scores', methods=['GET'])
def get_scores():
    return jsonify(scores), 200

@clinical.route('/scores/<int:id>', methods=['PUT'])
def update_score(id):
    data = request.json
    scores[id] = data
    return jsonify(data), 200

@clinical.route('/scores/<int:id>', methods=['DELETE'])
def delete_score(id):
    scores.pop(id)
    return '', 204
