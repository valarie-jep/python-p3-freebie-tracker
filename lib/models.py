from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship(
        'Freebie',
        back_populates='company',
        overlaps='devs,companies,freebies'
    )
    devs = relationship(
        'Dev',
        secondary='freebies',
        back_populates='companies',
        overlaps='freebies,company'
    )

    def __repr__(self):
        return f'<Company {self.name}>'


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship(
        'Freebie',
        back_populates='dev',
        overlaps='companies,devs,freebies'
    )
    companies = relationship(
        'Company',
        secondary='freebies',
        back_populates='devs',
        overlaps='freebies,dev'
    )

    def __repr__(self):
        return f'<Dev {self.name}>'


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship(
        'Company',
        back_populates='freebies',
        overlaps='devs,companies'
    )
    dev = relationship(
        'Dev',
        back_populates='freebies',
        overlaps='devs,companies'
    )

    def __repr__(self):
        return f'<Freebie {self.item_name} worth ${self.value}>'

