@given("the following products")
def step_impl(context):
    for row in context.table:
        ProductFactory(name=row["name"], category=row["category"], price=row["price"], availability=row["availability"])
