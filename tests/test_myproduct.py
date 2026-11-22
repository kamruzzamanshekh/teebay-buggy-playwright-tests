def test_delete_product(my_products):
    my_products.move_to_my_products()
    my_products.delete_product("Update_title")