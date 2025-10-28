from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'SET-HERE-HOST'
app.config['MYSQL_USER'] = 'SET-USER'
app.config['MYSQL_PASSWORD'] = 'SET-USER'
app.config['MYSQL_DATABASE'] = 'SET-DATABASE-NAME'

mydb = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DATABASE']
)


def execute_query(query, params=None):
    cursor = mydb.cursor()
    mydb.commit()
    cursor.execute(query, params)
    return cursor


def index(nameTable):
    curses = mydb.cursor()
    curses.execute(f"SELECT * FROM {nameTable}")
    result = curses.fetchall()
    return jsonify(result)


def show(nameTable, id):
    cursor = execute_query(f" SELECT * FROM {nameTable} WHERE id  = %s", (id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': f'{nameTable.upper()} not found'}), 404


def delete(nameTable, id):
    execute_query(f"DELETE FROM {nameTable} WHERE id = %s", (id,))
    return jsonify({'message': f'{nameTable.upper()} delete successfully'})


# manager operator
#manager
@app.route('/manager/login', methods=['POST'])
def get_manager():
    data = request.get_json()
    email = data['email']
    password = data['password']
    cursor = execute_query('SELECT * FROM manager WHERE email = %s', (email,))
    manager = cursor.fetchone()

    if manager:
        if password == manager[3]:
            return jsonify({'message': 'Walecome to back', 'login' : True})
        else:
            return jsonify({'message': f'password not true', 'login' : False}), 403
    else:
        return jsonify({'message': f'account not found'}), 404


@app.route('/manager/register', methods=['POST'])
def add_manager():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    execute_query('INSERT INTO manager (name, email, password) VALUES (%s, %s, %s)',(name, email, password))
    return jsonify({'message': 'Manager added successfully'}), 201

# driver CRUD
@app.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = index("driver")
    return drivers


@app.route('/driver', methods=['POST'])
def add_driver():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    plateNumber = data['plateNumber']
    description = data['description']
    execute_query(
        "INSERT INTO driver (fName, lName, plateNumber, description) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, plateNumber, description))
    return jsonify({'message': 'Driver added successfully'}), 201


@app.route('/driver/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    plateNumber = data['plateNumber']
    description = data['description']
    execute_query("UPDATE driver SET fName = %s, lName = %s, plateNumber = %s, description = %s WHERE id = %s",
                  (first_name, last_name, plateNumber, description, driver_id))
    return jsonify({'message': 'Driver updated successfully'})


@app.route('/driver/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    result = delete("driver", driver_id)
    return result


# guide
@app.route('/guides', methods=['GET'])
def get_guides():
    guides = index("guide")
    return guides


@app.route('/guide', methods=['POST'])
def add_guide():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    address = data['address']
    mobile = data['mobile']
    description = data['description']
    execute_query(
        "INSERT INTO guide (fName, lName, address, mobile, description) VALUES (%s, %s, %s, %s, %s)",
        (first_name, last_name, address, mobile, description))
    return jsonify({'message': 'Guide added successfully'}), 201


@app.route('/guide/<int:guide_id>', methods=['PUT'])
def update_guide(guide_id):
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    address = data['address']
    mobile = data['mobile']
    description = data['description']
    execute_query(
        "UPDATE guide SET fName = %s, lName = %s, address = %s, mobile = %s, description = %s WHERE id = %s",
        (first_name, last_name, address, mobile, description, guide_id))
    return jsonify({'message': 'Guide updated successfully'})


@app.route('/guide/<int:guide_id>', methods=['DELETE'])
def delete_guide(guide_id):
    result = delete("guide", guide_id)
    return result


# program
@app.route('/programs', methods=['GET'])
def get_programs():
    programs = index("program")
    return programs


@app.route('/program', methods=['POST'])
def add_program():
    data = request.get_json()
    type = data['type']
    name = data['name']
    description = data['description']
    execute_query(
        "INSERT INTO program (type, name, description) VALUES (%s, %s, %s)",
        (type, name, description))
    return jsonify({'message': 'Program added successfully'}), 201


@app.route('/program/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    data = request.get_json()
    type = data['type']
    name = data['name']
    description = data['description']
    execute_query(
        "UPDATE program SET type = %s, name = %s, description= %s WHERE id = %s",
        (type, name, description, program_id))
    return jsonify({'message': 'Program update successfully'}), 201


@app.route('/program/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    result = delete("program", program_id)
    return result


# tour
@app.route('/tours', methods=['GET'])
def get_tours():
    tours = index("tour")
    return tours


@app.route('/tour/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    tour = show("tour", tour_id)
    return tour

@app.route('/tour/history', methods=['POST'])
def history_tour():
    data = request.get_json()
    startDate = data['startDate']
    endDate = data['endDate']
    cursor = execute_query('SELECT * FROM `tour` WHERE startDate >= %s and endDate <= %s',(startDate,endDate))
    tour = cursor.fetchall()
    return jsonify(tour)

@app.route('/tour', methods=['POST'])
def add_tour():
    data = request.get_json()
    guide_id = data['guide_id']
    driver_id = data['driver_id']
    program_id = data['program_id']
    price = data['price']
    number = data['number']
    startDate = data['startDate']
    endDate = data['endDate']
    execute_query(
        "INSERT INTO tour(guide_id, driver_id, program_id, price, number, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (guide_id, driver_id, program_id, price, number, startDate, endDate))
    return jsonify({'message': 'Tour added successfully'}), 201


@app.route('/tour/<int:tour_id>', methods=['PUT'])
def update_tour(tour_id):
    data = request.get_json()
    guide_id = data['guide_id']
    driver_id = data['driver_id']
    program_id = data['program_id']
    price = data['price']
    number = data['number']
    startDate = data['startDate']
    endDate = data['endDate']
    execute_query(
        "UPDATE tour SET guide_id = %s, driver_id = %s, program_id = %s, price = %s, number = %s, startDate = %s, endDate = %s WHERE id = %s",
        (guide_id, driver_id, program_id, price, number, startDate, endDate, tour_id))
    return jsonify({'message': 'Tour updated successfully'})


@app.route('/tour/<int:tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    result = delete("tour", tour_id)
    return result

#tourist
@app.route('/tourists', methods=['GET'])
def get_tourists():
    tourists = index("tourist")
    return tourists


@app.route('/tourist/<int:tourist_id>', methods=['GET'])
def get_tourist(tourist_id):
    tourist = show("tourist", tourist_id)
    return tourist

@app.route('/tourist/login', methods=['POST'])
def login_tourist():
    data = request.get_json()
    email = data['email']
    password = data['password']
    cursor = execute_query('SELECT email, password FROM tourist WHERE email = %s', (email,))
    tourist = cursor.fetchone()
    if tourist:
        if password == tourist[1]:
            return jsonify({'message': 'Walecome to back', 'login': True})
        else:
            return jsonify({'message': f'password not true', 'login': False}), 403
    else:
        return jsonify({'message': f'account not found'}), 404

@app.route('/tourist/register', methods=['POST'])
def add_tourist():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    nationality = data['nationality']
    email = data['email']
    password = data['password']
    execute_query(
        "INSERT INTO tourist (fName, lName, nationality, email, password) VALUES (%s, %s, %s, %s, %s)",
        (first_name, last_name, nationality, email, password))
    return jsonify({'message': 'Tourist added successfully'}), 201


@app.route('/tourist/<int:tourist_id>', methods=['PUT'])
def update_tourist(tourist_id):
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    nationality = data['nationality']
    email = data['email']
    password = data['password']
    execute_query("UPDATE tourist SET fName = %s, lName = %s, nationality = %s,  email = %s, password = %s WHERE id = %s",
                  (first_name, last_name, nationality, email, password, tourist_id))
    return jsonify({'message': 'Tourist updated successfully'})


@app.route('/tourist/<int:tourist_id>', methods=['DELETE'])
def delete_tourist(tourist_id):
    result = delete("tourist", tourist_id)
    return result


if __name__ == '__main__':
    app.run(debug=True)

