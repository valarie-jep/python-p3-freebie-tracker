#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear old data if any (optional)
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()

    # Create companies
    c1 = Company(name='TechCorp', founding_year=2001)
    c2 = Company(name='SoftWorks', founding_year=1998)

    # Create devs
    d1 = Dev(name='Alice')
    d2 = Dev(name='Bob')

    # Add all to session
    session.add_all([c1, c2, d1, d2])
    session.commit()

    # Create freebies with relationships
    f1 = Freebie(item_name='T-Shirt', value=20, company=c1, dev=d1)
    f2 = Freebie(item_name='Coffee Mug', value=10, company=c2, dev=d2)
    f3 = Freebie(item_name='Sticker Pack', value=5, company=c1, dev=d2)

    session.add_all([f1, f2, f3])
    session.commit()

    print("Database seeded successfully!")

