from engine import engine
from tables import UsersTable
statement = UsersTable.insert().values(
    first_name='Karan', last_name="Test")
# UsersTable.insert()
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()
