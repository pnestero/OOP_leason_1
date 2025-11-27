def test_category(tests1_category, tests2_category):
    # тесты для tests1_category
    assert tests1_category.name == "Телевизор"
    assert tests1_category.description == "Samsung"
    assert tests1_category.products == ["Kasper", "NLNK", "DDS"]
    assert len(tests1_category.products) == 3

    assert tests1_category.count_categories == 2
    assert tests1_category.count_products == 5

    # тесты для tests2_category
    assert tests2_category.name == "Телефон"
    assert tests2_category.description == "program developer"
    assert tests2_category.products == ["ICQ", "Vypres"]
    assert len(tests2_category.products) == 2

    assert tests2_category.count_categories == 2
    assert tests2_category.count_products == 5