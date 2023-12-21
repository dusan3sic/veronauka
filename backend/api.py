from flask import Flask, request, jsonify
import pymysql
from pymysql.cursors import DictCursor
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# MariaDB Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'knjigaVencanih'

# Function to create a MySQL connection
def get_db():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=DictCursor
    )

# Insert data into Osoba table
@app.route('/insert_osoba', methods=['POST'])
def insert_osoba():
    try:
        data = request.get_json()
        connection = get_db()
        with connection.cursor() as cursor:
            cursor.execute("CALL ubaciOsobu(%s, %s, %s, %s, %s, %s, %s)",
                           (data['ime'], data['prezime'], data['zanimanje'], data['mestoRodjenja'], data['godinaRodjenja'], data['drzavljanstvo'], data['imePrezimeRoditelji']))
            result = cursor.fetchone()
            # inserted_id = result['inserted_id']
        
        connection.commit()
        connection.close()
        print(2)
        return jsonify({'id': result})
    except Exception as e:
        print(1)
        return jsonify({'id': None, 'error': e})


# Insert data into Brak table
@app.route('/insert_brak', methods=['POST'])
def insert_brak():
    try:
        data = request.get_json()
        connection = get_db()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Brak (idOsobe1, idOsobe2, brakSklopljen, brakPoRedu, mestoVencanja, koJeVencao, svedoci) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (data['idOsobe1'], data['idOsobe2'], data['brakSklopljen'], data['brakPoRedu'], data['mestoVencanja'], data['koJeVencao'], data['svedoci']))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Brak inserted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)