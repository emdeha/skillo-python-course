from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    conn.execute(text('''CREATE TABLE IF NOT EXISTS EMPLOYEES
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        SALARY REAL);'''))

    conn.execute(text('INSERT INTO EMPLOYEES VALUES (1, "A Test", 2000)'))
    conn.execute(text('INSERT INTO EMPLOYEES VALUES (2, "B Test", 1000)'))
    conn.execute(text('INSERT INTO EMPLOYEES VALUES (3, "C Test", 4000)'))
    conn.execute(text('INSERT INTO EMPLOYEES VALUES (4, "D Test", 1000)'))
    conn.execute(text('INSERT INTO EMPLOYEES VALUES (5, "E Test", 500)'))
    conn.commit()

    result = conn.execute(text("SELECT NAME, SALARY FROM EMPLOYEES ORDER BY SALARY"))
    for row in result:
        print(f"Name: {row.NAME}  Salary: {row.SALARY}")
