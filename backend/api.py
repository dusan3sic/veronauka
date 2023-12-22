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
            # Note: Added OUT parameter for the inserted ID
            cursor.execute("CALL ubaciOsobu(%s, %s, %s, %s, %s, %s, %s, @inserted_id)",
                           (data['ime'], data['prezime'], data['zanimanje'], data['mestoRodjenja'], data['godinaRodjenja'], data['drzavljanstvo'], data['imePrezimeRoditelji']))
            
            # Execute a query to retrieve the value of @inserted_id
            cursor.execute("SELECT @inserted_id AS id")
            result = cursor.fetchone()
            inserted_id = result['id']
        
        connection.commit()
        connection.close()

        # Use app.logger.info() for logging
        app.logger.info(f'Inserted ID: {inserted_id}')

        return jsonify({'id': inserted_id})
    except Exception as e:
        # Use app.logger.error() for logging
        app.logger.error(f'Error: {str(e)}')
        return jsonify({'id': None, 'error': str(e)})


# Insert data into Brak table
@app.route('/insert_brak', methods=['POST'])
def insert_brak():
    try:
        data = request.get_json()
        connection = get_db()
        with connection.cursor() as cursor:
            cursor.execute("CALL sklopiBrak(%s, %s, %s, %s, %s, %s, %s)",
                           (data['idOsobe1'], data['idOsobe2'], data['brakSklopljen'], data['brakPoRedu'], data['mestoVencanja'], data['koJeVencao'], data['svedoci']))
        
        connection.commit()
        connection.close()
        return jsonify({'success': True, 'message': 'Brak inserted successfully'})
    except Exception as e:
        app.logger.info(e)
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
