import enum
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, composite, relationship
from datetime import datetime
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.dialects.postgresql import ARRAY


# ORM that enables one to define a column that is composed of multiple individual columns, to jest Component
# Step 1: Define the Product model
Base = declarative_base()

# stany produktu - dostępny, wyprzedany, przeceniony, niedostępny
class ProductStates(enum.Enum):
    AVAILABLE = "available"
    NOT_AVAILABLE = "not_available"
    SOLD_OUT = "sold_out"
    DISCOUNTED = "discounted"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # ENUM, chcemy używać wartości pól, stąd ta lambda (inaczej używalibyśmy nazw pól)
    product_state = Column(Enum(ProductStates, values_callable=lambda x: [str(member.value) for member in ProductStates]))


    # COMPONENT
    # dane do pola z wieloma parametrami
    company_name  = Column(String, nullable=False)
    city_name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    company_address = composite(
        lambda name,city,street,number: f"{name} {city} {street} {number}",company_name,city_name,street,number)

    # COLLECTION
    transaction_id = Column(Integer, ForeignKey('transactions.id'))


    def __repr__(self):
        return f"<Product(name='{self.name}', price='{self.price}'>"

# ASSOCIATION
# relacja między sklepem a produktem jest relacja jeden do wielu, jeden produkt może być w wielu sklepach
class Store(Base):

    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    ceo = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product")


# transakcja zawiera kolekcję produktów
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    products = relationship("Product", backref="transactions", order_by="Product.id", collection_class=ordering_list('id'))




# Replace 'sqlite:///example.db' with your actual database connection string
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# dodawanie do bazy
# person = Product("Juice", 12.02, "My favorite")
# session.add(person)

product1 = Product(
    name='Awesome Widget',
    price=19.99,
    company_name='ABC Electronics',
    city_name='Techville',
    street='Innovation Street',
    number=42,
    product_state="sold_out" # "sold_outtttt" da na błąd
)

product2 = Product(
    name='Super Gizmo',
    price=29.99,
    company_name='XYZ Innovations',
    city_name='Innovatown',
    street='Tech Street',
    number=99,
    product_state="available"
)

product3 = Product(
    name='Widget Gadget',
    price=30.01,
    company_name='Elon',
    city_name='Wroclaw',
    street='Jane Street',
    number=99,
    product_state="not_available"
)

transaction1 = Transaction(
    name='Jan',
    surname='Kowalski',
)

store1 = Store(
    name="Piotr i Paweł",
    ceo="Nowak",
    product=product1
)
store2 = Store(
    name="Chata Polska",
    ceo="Cieśla",
    product=product1
)

# DODAWANIE REKORDÓW
# dodanie do listy produktów w transakcji produktów
# COLLECTIONS
# transaction1.products.append(product1)
# transaction1.products.append(product2)
# session.add_all([product1, product2, transaction1])
# ASSOCIATIONS
# session.add_all([product1, product2, transaction1, store1, store2])
# session.commit() # dodanie do bazy danych

# TYPY KOLEKCJI
# np. ordered_list

# pobieranie z bazy
# print(product1.ratings)
products = session.query(Product).all()
print(products)

# 3 pierwsze podpunkty (bez HiLow)
# # Print the records
# for product in products:
#     # print(f"Product Name: {product.name}, Price: {product.price}")
#     print(f"Company Full Address:{product.company_address}")
#     print(f"Company Full Address:{product.product_state.value}")

# COLLECTIONS
# res = session.query(Transaction).filter(Transaction.name == 'Jan').first()
# for product in res.products:
#     print(product.name)

# ASSOCIATIONS
# many to one
# res = session.query(Store).all()
# for r in res:
#     print(r.product)


# methods:
def getById(id, table_name):
    tb_name = table_name.lower()
    if tb_name == 'products':
        return session.query(Product).filter(Product.id == id).first()
    elif tb_name == 'transactions':
        return session.query(Transaction).filter(Transaction.id == id).first()
    elif tb_name == 'stores':
        return session.query(Store).filter(Store.id == id).first()

# print(getById(1, 'products').name)


def findAll(table_name):
    tb_name = table_name.lower()
    if tb_name == 'products':
        return session.query(Product).all()
    elif tb_name == 'transactions':
        return session.query(Transaction).all()
    elif tb_name == 'stores':
        return session.query(Store).all()

# for i in findAll('transactions'):
#     print(i.name)





import argparse

# POLECENIA
# python3 main.py - -findAll - -table_name transactions
# python3 main.py --getById --id 1 --table_name products

def main():
    parser = argparse.ArgumentParser(description="Execute database queries")

    parser.add_argument('--getById', action='store_true', help='Get entry by ID')
    parser.add_argument('--findAll', action='store_true', help='Get all entries')
    parser.add_argument('--id', type=int, help='ID of the entry')
    parser.add_argument('--table_name', type=str, help='Table name (products, transactions, stores)')

    args = parser.parse_args()

    if args.getById:
        if args.id is not None and args.table_name is not None:
            result = getById(args.id, args.table_name)
            print(result)
        else:
            print("Error: Both --id and --table_name are required for getById.")

    elif args.findAll:
        if args.table_name is not None:
            result = findAll(args.table_name)
            print(result)
        else:
            print("Error: --table_name is required for findAll.")

    else:
        print("Error: Choose either --getById or --findAll.")

if __name__ == "__main__":
    main()
