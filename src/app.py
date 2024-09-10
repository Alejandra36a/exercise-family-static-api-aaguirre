"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():
    # Llamar al método desde la instancia
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(members), 200

@app.route('/member', methods=['POST']) #AGREGO INF
def add_member():
    #obtengo los datos del nuevo miembro dsd la solicitud 
    nuevo_member = request.json
    #valido que los datos esten usando un condicional: 
    if not nuevo_member:
        return ({"error":"Datos no encontrados"}), 400
    #agrego al nuevo miembro sino entra en la condicion anterior 
    jackson_family.add_member(nuevo_member)
    
    return jsonify({"mensaje": "Miembro agregado exitosamente"}), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_id_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member)

@app.route('/member/<int:id>', methods=['DELETE'])
def del_member(id):
    delete = jackson_family.delete_member(id)
    return jsonify(delete)






# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
