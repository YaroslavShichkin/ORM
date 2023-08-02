import sqlalchemy, psycopg2
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:123456789@localhost:5432/books"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Толстой')
publisher3 = Publisher(name='Достоевсский')
session.add_all([publisher1, publisher2, publisher3])
session.commit()


book1 = Book(title='Капитанская дочка', id_publisher=1)
book2 = Book(title='Евгений Онегин', id_publisher=1)
book3 = Book(title='Война и мир', id_publisher=2)
book4 = Book(title='Анна Каренина', id_publisher=2)
book5 = Book(title='Бесы', id_publisher=3)
book6 = Book(title='Идиот', id_publisher=3)
session.add_all([book1, book2, book3, book4, book5, book6])
session.commit()


shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
session.add_all([shop1, shop2])
session.commit()


stock1 = Stock(id_book=1, id_shop=1, count=10)
stock2 = Stock(id_book=1, id_shop=2, count=20)
stock3 = Stock(id_book=2, id_shop=1, count=5)
stock4 = Stock(id_book=2, id_shop=2, count=15)
stock5 = Stock(id_book=3, id_shop=1, count=15)
stock6 = Stock(id_book=3, id_shop=2, count=10)
stock7 = Stock(id_book=4, id_shop=2, count=5)
stock8 = Stock(id_book=5, id_shop=1, count=10)
stock9 = Stock(id_book=5, id_shop=2, count=20)
stock10 = Stock(id_book=6, id_shop=1, count=20)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10])
session.commit()


sale1 = Sale(price=300, date_sale='11.12.2022', id_stock=1, count=2)
sale2 = Sale(price=450, date_sale='13.12.2022', id_stock=3, count=1)
sale3 = Sale(price=250, date_sale='13.12.2022', id_stock=7, count=1)
sale4 = Sale(price=300, date_sale='14.12.2022', id_stock=8, count=2)
sale5 = Sale(price=350, date_sale='15.12.2022', id_stock=3, count=1)
sale6 = Sale(price=450, date_sale='15.12.2022', id_stock=2, count=1)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6])
session.commit()

for c in session.query(Publisher).join(Book.publisher).filter(Book.title == 'Война и мир').all():
    print(c)

session.close()