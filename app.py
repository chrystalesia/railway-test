from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
db_port = os.getenv('DB_PORT')

# Initialize MySQL database connection
def init_mysql_connection():
      return mysql.connector.connect(
         host=db_host,
         user=db_user,
         password=db_password,
         database=db_database,
         port=db_port
      )

# CRUD operations

# Example: Create operation
@app.route('/user/', methods=['POST'])
def add_user():
      conn = init_mysql_connection()
      cur = conn.cursor()
      name = request.form['name']
      email = request.form['email']
      cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
      conn.commit()
      conn.close()
      return jsonify(message="User added successfully"), 201

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
      return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
      app.run(debug=True,port=os.getenv('PORT'))
