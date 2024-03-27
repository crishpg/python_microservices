import requests
import os
from flask import Flask, jsonify, abort, request, make_response, url_for
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

##Inicio do teste
@app.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    try:
        #session = Session()
        #new_user = User(name=name)
        #session.add(new_user)
        #session.commit()

        #return {"id": new_user.id, "name": new_user.name, "message": f"User {name} created."}, 201
        return { "name": name,"email": email }, 201
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the user."}, 500
##fim do teste


#@app.route("/")
#def home():
#    return "Hello, this is a Flask Microservice"
BASE_URL = "https://dummyjson.com"
@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code != 200:
        return jsonify({'error': response.json()['message']}), response.status_code
    products = []
    for product in response.json()['products']:
        product_data = {
            'id': product['id'],
            'title': product['title'],
            'brand': product['brand'],
            'price': product['price'],
            'description': product['description']
        }
        products.append(product_data)
    return jsonify({'data': products}), 200 if products else 204
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)

