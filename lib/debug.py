from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dev, Company, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# View all companies
print("\n--- Companies ---")
for company in session.query(Company).all():
    print(company)

# View all devs
print("\n--- Devs ---")
for dev in session.query(Dev).all():
    print(dev)

# View all freebies
print("\n--- Freebies ---")
for freebie in session.query(Freebie).all():
    print(freebie)

# View freebies belonging to the first company
print("\n--- Freebies by First Company ---")
first_company = session.query(Company).first()
print(f"{first_company.name}'s freebies: {first_company.freebies}")

# View companies associated with the first dev
print("\n--- Companies associated with First Dev ---")
first_dev = session.query(Dev).first()
print(f"{first_dev.name}'s companies: {first_dev.companies}")






