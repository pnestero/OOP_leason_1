from src.category import Category
from src.products import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product (name="Банан", description="Чтобы съесть", price=123.12, quantity=2)
    message = capsys.readouterr()
    assert message.out.split() == ['Product(Банан,', 'Чтобы', 'съесть,', '123.12,', '2)']

    Category(name="Телевизор",
             description="Samsung",
             init_products=[Product(name="Банан",
             description="Чтобы съесть",
             price=123.12,
             quantity=2)])
    message = capsys.readouterr()
    assert message.out.split() == ['Product(Банан,', 'Чтобы', 'съесть,', '123.12,', '2)']

    Smartphone(name="Samsung Galaxy C23 Ultra",
               description="256GB, Серый цвет, 200MP камера",
               price=180000.0,
               quantity=5,
               efficiency=500,
               model="Galaxy",
               memory="16 GB",
               color="red")
    message = capsys.readouterr()
    assert message.out.split() == ['Smartphone(Samsung', 'Galaxy', 'C23', 'Ultra,', '256GB,', 'Серый', 'цвет,',
 '200MP',
 'камера,',
 '180000.0,',
 '5)']