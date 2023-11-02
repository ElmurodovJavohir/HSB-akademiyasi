from sqlalchemy import MetaData, Table, Column, Integer, String
meta = MetaData()

UsersTable = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(128)),
    Column('last_name', String(128)),
)
