@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    product = Product(**data)
    product.save()
    return jsonify(product.to_dict()), 201
