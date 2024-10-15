"""
Zachery D'Andrea
UHID #2306246
October 15th, 2024
Project Sprint 1


API to interact with the investor table, stock table, bond table, stocktransaction table, and bond transaction table in my
database using SQL and Python


I used the sql.py and cred.py files from previous homework assignments to access my sql database and reused functions
to set up the CRUD application for my 5 tables


All tables have been tested within the Postman App, and work correctly.


The CRUD Applications are complete and ready for use when I begin the next sprint for the project.


"""


# Imports flask
import flask
from flask import jsonify, request


# Ensure 'sql' module is available
from sql import DBconnector, execute_read_query, execute_read_ID_query, execute_update_query, execute_post_query
from cred import myCreds


app = flask.Flask(__name__)
app.config['DEBUG'] = True


# Establishes database connection
connection = DBconnector(myCreds.hostname, myCreds.username, myCreds.password, myCreds.database)


# GET all from Investor
@app.route('/api/investor', methods=['GET'])
def get_items_all_investor():
    sql = "SELECT * FROM investor"
    investor = execute_read_query(connection, sql)
    return jsonify(investor), 200


# GET Investor by ID
@app.route('/api/investor/<int:id>', methods=['GET'])
def get_items_id_investor(id):
    sql = "SELECT * FROM investor WHERE id =%s"
    params = (id,)
    investor = execute_read_ID_query(connection, sql, params)
    return jsonify(investor), 200 if investor else 404


# GET all from Bond
@app.route('/api/bond', methods=['GET'])
def get_items_all_bond():
    sql = "SELECT * FROM bond"
    bond = execute_read_query(connection, sql)
    return jsonify(bond), 200


# GET Bond by ID
@app.route('/api/bond/<int:id>', methods=['GET'])
def get_items_id_bond(id):
    sql = "SELECT * FROM bond WHERE id =%s"
    params = (id,)
    bond = execute_read_ID_query(connection, sql, params)
    return jsonify(bond), 200 if bond else 404


# GET all from Stock
@app.route('/api/stock', methods=['GET'])
def get_items_all_stock():
    sql = "SELECT * FROM stock"
    stock = execute_read_query(connection, sql)
    return jsonify(stock), 200


# GET Stock by ID
@app.route('/api/stock/<int:id>', methods=['GET'])
def get_items_id_stock(id):
    sql = "SELECT * FROM stock WHERE id =%s"
    params = (id,)
    stock = execute_read_ID_query(connection, sql, params)
    return jsonify(stock), 200 if stock else 404


# POST Investor
@app.route('/api/investor', methods=['POST'])
def add_items_investor():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']


    sql = f"INSERT INTO investor (firstname, lastname) VALUES ('{firstname}', '{lastname}')"
    execute_post_query(connection, sql)
    return jsonify({'message' : 'Item added successfully'}), 201


# POST Stock
@app.route('/api/stock', methods=['POST'])
def add_items_stock():
    data = request.get_json()
    stockname = data['stockname']
    abbreviation = data['abbreviation']
    currentprice = data['currentprice']


    sql = f"INSERT INTO stock (stockname, abbreviation, currentprice) VALUES ('{stockname}', '{abbreviation}', '{currentprice}')"
    execute_post_query(connection, sql)
    return jsonify({'message' : 'Item added successfully'}), 201


# POST Bond
@app.route('/api/bond', methods=['POST'])
def add_items_bond():
    data = request.get_json()
    bondname = data['bondname']
    abbreviation = data['abbreviation']
    currentprice = data['currentprice']


    sql = f"INSERT INTO bond (bondname, abbreviation, currentprice) VALUES ('{bondname}', '{abbreviation}', '{currentprice}')"
    execute_post_query(connection, sql)
    return jsonify({'message' : 'Item added successfully'}), 201


# PUT Investor
@app.route('/api/investor/<int:id>', methods=['PUT'])
def update_investor(id):
    data = request.get_json()
    sql = f"UPDATE investor SET firstname = %s, lastname = %s WHERE id = %s"
    params = (data['firstname'], data['lastname'], id)
    execute_update_query(connection, sql, params)
    return jsonify({'message' : 'Investor updated successfully'}), 200


# PUT Bond
@app.route('/api/bond/<int:id>', methods=['PUT'])
def update_bond(id):
    data = request.get_json()
    sql = "UPDATE bond SET bondname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"
    params = (data['bondname'], data['abbreviation'], data['currentprice'], id)
    execute_update_query(connection, sql, params)
    return jsonify({'message' : 'Bond updated successfully'}), 200


# PUT Stock
@app.route('/api/stock/<int:id>', methods=['PUT'])
def update_stock(id):
    data = request.get_json()
    sql = "UPDATE stock SET stockname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"
    params = (data['stockname'], data['abbreviation'], data['currentprice'], id)
    execute_update_query(connection, sql, params)
    return jsonify({'message' : 'Stock updatesd successfully'}), 200


# DELETE Investor
@app.route('/api/investor/<int:id>', methods=['DELETE'])
def delete_investor(id):
    sql = "DELETE FROM investor WHERE id = %s"
    params = (id,)
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Investor deleted successfully'}), 200


# DELETE Bond
@app.route('/api/bond/<int:id>', methods=['DELETE'])
def delete_bond(id):
    sql = "DELETE FROM bond WHERE id = %s"
    params = (id,)
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Bond deleted successfully'}), 200


# DELETE Stock
@app.route('/api/stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    sql = "DELETE FROM stock WHERE id = %s"
    params = (id,)
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Stock deleted successfully'}), 200


# POST Stock Transcation
@app.route('/api/stocktransaction', methods=['POST'])
def create_stock_transaction():
    data = request.get_json()
    sql = "INSERT INTO stocktransaction (investorid, stockid, quantity) VALUES (%s, %s, %s)"
    params = (data['investorid'], data['stockid'], data['quantity'])
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Stock transaction created successfully'}), 201


# GET Stock Transaction
@app.route('/api/stocktransaction', methods=['GET'])
def get_stock_transaction():
    sql = "SELECT * FROM stocktransaction"
    transactions = execute_read_query(connection, sql)
    return jsonify(transactions), 200


# DELETE Stock Transaction
@app.route('/api/stocktransaction/<int:id>', methods=['DELETE'])
def delete_stock_transaction(id):
    sql = "DELETE FROM stocktransaction WHERE id = %s"
    params = (id,)
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Stock transaction deleted successfully'}), 200


# POST Boond Transaction
@app.route('/api/bondtransaction', methods=['POST'])
def create_bond_transaction():
    data = request.get_json()
    sql = "INSERT INTO bondtransaction (investorid, bondid, quantity) VALUES (%s, %s, %s)"
    params = (data['investorid'], data['bondid'], data['quantity'])
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Bond transaction created successfully'}), 201


# GET Bond Transaction
@app.route('/api/bondtransaction', methods=['GET'])
def get_bond_transactions():
    sql = "SELECT * FROM bondtransaction"
    transactions = execute_read_query(connection, sql)
    return jsonify(transactions), 200


# DELETE Bond Transaction
@app.route('/api/bondtransaction/<int:id>', methods=['DELETE'])
def delete_bond_transaction(id):
    sql = "DELETE FROM bondtransaction WHERE id = %s"
    params = (id,)
    execute_update_query(connection, sql, params)
    return jsonify({'message': 'Bond transaction deleted successfully'}), 200


if __name__ == '__main__':
    app.run()
