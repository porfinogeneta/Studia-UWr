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

product4 = Product(
    name='Incredible Gadget',
    price=49.99,
    company_name='InnoTech Solutions',
    city_name='Techtopia',
    street='Progress Avenue',
    number=123,
    product_state="available"
)

product5 = Product(
    name='Smart Widget Pro',
    price=39.99,
    company_name='TechGenius Co.',
    city_name='Innovation City',
    street='Tech Boulevard',
    number=55,
    product_state="available"
)

product6 = Product(
    name='Future Gizmo X',
    price=59.99,
    company_name='NextGen Innovations',
    city_name='Tech Haven',
    street='Future Lane',
    number=88,
    product_state="sold_out"
)

product7 = Product(
    name='Ultimate Tech Device',
    price=79.99,
    company_name='FutureTech Industries',
    city_name='Innovateville',
    street='Tech Square',
    number=7,
    product_state="available"
)

product8 = Product(
    name='Nano Widget Mini',
    price=14.99,
    company_name='MicroTech Solutions',
    city_name='Nano City',
    street='Tiny Lane',
    number=5,
    product_state="available"
)

product9 = Product(
    name='Innovative Gizmo Plus',
    price=49.99,
    company_name='Innovation Innovators',
    city_name='Techtopolis',
    street='Future Street',
    number=22,
    product_state="not_available"
)

product10 = Product(
    name='Smart Tech Companion',
    price=69.99,
    company_name='TechBuddy Corp',
    city_name='InnoHub',
    street='Progressive Street',
    number=101,
    product_state="available"
)

product11 = Product(
    name='Gadget Mastermind',
    price=89.99,
    company_name='TechMinds Unlimited',
    city_name='InnoSphere',
    street='Tech Genius Avenue',
    number=77,
    product_state="available"
)

product12 = Product(
    name='Futuristic Widget XL',
    price=99.99,
    company_name='InnoFutures Inc.',
    city_name='Techtopolis',
    street='Future Boulevard',
    number=333,
    product_state="sold_out"
)

product13 = Product(
    name='NanoTech Wonder',
    price=19.99,
    company_name='NanoInnovate Labs',
    city_name='Nano City',
    street='Quantum Street',
    number=11,
    product_state="not_available"
)


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

product21 = Product(
    name='Another Gizmo',
    price=9.99,
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
session.add_all([
    product1, product2, product21,
    product4, product5, product6,
    product7, product8, product9,
    product10, product11, product12,
    product13
])
session.commit()
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
# products = session.query(Product).all()
# print(products)

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

from sqlalchemy import or_, and_

def filter_results(query, filters, model):
    for column_name, condition in filters.items():
        column = getattr(model, column_name, None)
        if column is not None:
            if isinstance(condition, tuple) and len(condition) == 2:
                # sortowanie po liczbach
                operator, value = condition
                if operator == "gt":
                    query = query.filter(column > value)
                elif operator == "lt":
                    query = query.filter(column < value)
                elif operator == "eq":
                    query = query.filter(column == value)
                # Add more custom operators as needed
            else:
                # sortowanie po stringach
                query = query.filter(column.ilike(f"%{condition}%"))
    return query.all()

# Example usage:
filters = {"name": "plus", "price": ('gt', 20)}
filtered_products = filter_results(session.query(Product), filters, Product)
# print(filtered_products)


def sort_results(query, model, sort_by=None):
    for column_name, order in sort_by.items():
        column = getattr(model, column_name, None)
        if column is not None:
            if order == "asc":
                query = query.order_by(column.asc())
            elif order == "desc":
                query = query.order_by(column.desc())

    return query.all()

sorting = {"price": "desc", "name": "desc"}  # Sort by price in ascending order and name in descending order
sorted_products = sort_results(session.query(Product), Product, sorting)
# print(sorted_products)

def paginate_query(query, page, per_page):
    if page < 1:
        page = 1

    offset = (page - 1) * per_page
    paginated_query = query.offset(offset).limit(per_page)
    return paginated_query.all()

page_number = 4
items_per_page = 2
paginated_results = paginate_query(session.query(Product), page=page_number, per_page=items_per_page)
print(paginated_results)


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
