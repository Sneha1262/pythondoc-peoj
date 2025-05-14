from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory DB
data = {}

# CREATE
@app.route('/item', methods=['POST'])
def create_item():
    item_id = request.form['id']
    name = request.form['name']
    data[item_id] = name
    return jsonify({"msg": "Item created", "id": item_id}), 201

# READ
@app.route('/item/<item_id>', methods=['GET'])
def read_item(item_id):
    if item_id in data:
        return jsonify({item_id: data[item_id]})
    return jsonify({"error": "Item not found"}), 404

# UPDATE
@app.route('/item/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data:
        name = request.form['name']
        data[item_id] = name
        return jsonify({"msg": "Item updated"})
    return jsonify({"error": "Item not found"}), 404

# DELETE
@app.route('/item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data:
        del data[item_id]
        return jsonify({"msg": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
