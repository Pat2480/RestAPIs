from flask import Flask, request, jsonify
import json

app = Flask(__name__)

countries = [
    {"id": "1","name":"Thailand","capital":"Bangkok"},
    {"id": "2","name":"Australia","capital":"Canberra"},
    {"id": "3","name":"USA","capital":"LA"},
]

def _find_next_id(id):
    data = [x for x in countries if x['id'] ==id]
    return data


#GET - REST API
@app.route('/country', methods=['GET'])
def get_countries():
    return jsonify(countries)

def country_is_valid(countries):
  for key in countries.keys():
    if key != 'name':
      return False
  return True
   

#GET = by ID
@app.route('/country/<id>', methods=['GET'])
def get_country_id(id):
    data = _find_next_id(id)
    return jsonify(data)

@app.route('/country', methods=['POST'])
def post_country():
    id = request.form.get('id')
    name = request.form.get('name')
    capital = request.form.get('capital')

    new_data = {
        "id": id,
        "name": name,
        "capital": capital
    }

    if (_find_next_id(id)):
        return{"error": "Bad Request"}, id
    else:
        countries.append(new_data)
        return jsonify(countries)

@app.route('/country/<id>', methods=["DELETE"])
def delete_country(id: int):

    data = _find_next_id(id)
    if not data:
        return {"error": "country does not exist."}, 404
    else:
        countries.remove(data[0])
        return "Country deleted successfully", 200

        


@app.route('/country/<id>', methods=["PUT"])
def update_country(id: int):
    data = _find_next_id(id)
    if data is None:
        return jsonify({'error': 'country does not exist.'}), 404

    updated_country = json.loads(request.data)
    if not country_is_valid(updated_country):
        return jsonify({'error': 'invalid country properties.'}), 400
    
    countries.update(updated_country)

    return jsonify(countries)
  

@app.route('/patch_country/<id>', methods=["PATCH"])
def patch_country(p_id):
    id = request.form.get('id')
    global countries
    name = request.form.get('name')
    capital = request.form.get('capital')

    data = _find_next_id(id)
    if not data:
        return {"error": "country does not exist."}, 404

    name.form.get('name')
    capital.form.get('capital')

    if name:
        data['name'] = name
    if capital:
        data['capital'] = capital
    return {"message": "Country updated successfully"}, 200





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)