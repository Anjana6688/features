@app.route('/products/<int:product_id>', methods=['GET'])

def get_products(product_id):

    # Read

@app.route('/products/<int:product_id>', methods=['PUT'])

def update_products(product_id):

    # Update

@app.route('/products/<int:product_id>', methods=['DELETE'])

def delete_products(product_id):

    # Delete

@app.route('/products', methods=['GET'])

def list_products():

    # List All

@app.route('/products', methods=['GET'])

def search_by_name():

    # List by Name

@app.route('/products', methods=['GET'])

def search_by_category():

    # List by Category

@app.route('/products', methods=['GET'])

def search_by_availability():

    # List by Availability
 
