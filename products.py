import requests
import os
import json
import pika
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
        json_username = name
        json_email =  email            
        payload = json.dumps({"username": json_username, "email":json_email }, indent=4)
        headers = { 'Content-Type': 'application/json'}
        credentials = pika.PlainCredentials('username','password')
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost',credentials=credentials, port=5672)
        )
        channel = connection.channel()
        channel.exchange_declare('exchange_usuario', durable=True, exchange_type='topic')
        channel.queue_declare(queue= 'usuario')
        channel.queue_bind(exchange='exchange_usuario', queue='usuario', routing_key='usuario')

    #message= 'hello consumer fila C!!!!!'
        message = payload 
        channel.basic_publish(exchange='exchange_usuario', routing_key='usuario', body= message)
        channel.close()    

        return { "name": name,"email": email }, 201
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the user."}, 500
##fim do teste

 
    
#Enviando valores para o rabbitMQ


# Conexão com o RabbitMQ

##Fim do processo envia os dados para o rabbitmq    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)

