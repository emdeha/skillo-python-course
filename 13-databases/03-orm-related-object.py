from sqlalchemy import String, create_engine, insert, Integer, select
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from sqlalchemy.testing.schema import Table, Column

metadata_obj = MetaData()

employee_table = Table(
    "employee",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("age", Integer),
)


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]

    def __repr__(self) -> str:
        return f"Employee(id={self.id!r}, name={self.name!r}, age={self.age!r})"


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata_obj.create_all(engine)
with engine.connect() as conn:
    insert_employee_stmt = insert(Employee).values(name="A Test", age=30)
    conn.execute(insert_employee_stmt)
    select_employee_stmt = select(Employee)
    print(conn.execute(select_employee_stmt).first())
    # for row in conn.execute(select_employee_stmt):
    #     print(row)
