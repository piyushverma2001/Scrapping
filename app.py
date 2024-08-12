from flask import Flask, jsonify, request
import scrapper

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to the Paris Olympics 2024!"

# def get_items():
#     return scapper.json_value()

# print(scapper.json_value())

# @app.route('/items', methods=['GET'])
# def get_items_endpoint():
#     items = get_items()
#     return items

@app.route('/medals', methods=['GET'])
def get_medals():
    
    return jsonify(scrapper.medals())
    # data_list = []
    # for i in range(len(scrapper.country_names)):
    #     data = {
    #         'Country': scrapper.country_names[i],
    #         'Medals': {
    #             'Gold': scrapper.medals_chunk[i][0],
    #             'Silver': scrapper.medals_chunk[i][1],
    #             'Bronze': scrapper.medals_chunk[i][2]
    #         },
    #         'Total Medals': scrapper.total_medals[i]
    #     }
    #     data_list.append(data)
    # return jsonify(data_list)


# # GET item by ID
# @app.route('/items/<int:item_id>', methods=['GET'])
# def get_item(item_id):
#     item = next((item for item in data if item["id"] == item_id), None)
#     if item:
#         return jsonify(item)
#     else:
#         return jsonify({"message": "Item not found"}), 404

# # POST a new item
# @app.route('/items', methods=['POST'])
# def create_item():
#     new_item = request.get_json()
#     new_item['id'] = data[-1]['id'] + 1 if data else 1
#     data.append(new_item)
#     return jsonify(new_item), 201

# # PUT (update) an item
# @app.route('/items/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     item = next((item for item in data if item["id"] == item_id), None)
#     if item:
#         updates = request.get_json()
#         item.update(updates)
#         return jsonify(item)
#     else:
#         return jsonify({"message": "Item not found"}), 404

# # DELETE an item
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     global data
#     data = [item for item in data if item["id"] != item_id]
#     return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=40119)
