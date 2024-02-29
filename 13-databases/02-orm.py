from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    conn.execute(text('''CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);'''))

    conn.execute(text('INSERT INTO COMPANY VALUES (1, "A Test", 30, "asdf", 1000)'))
    conn.execute(text('INSERT INTO COMPANY VALUES (2, "B Test", 20, "asdf", 1000)'))
    conn.execute(text('INSERT INTO COMPANY VALUES (3, "C Test", 35, "asdf", 1000)'))
    conn.execute(text('INSERT INTO COMPANY VALUES (4, "D Test", 23, "asdf", 1000)'))
    conn.execute(text('INSERT INTO COMPANY VALUES (5, "E Test", 33, "asdf", 1000)'))
    conn.commit()

    result = conn.execute(text("SELECT NAME, AGE FROM COMPANY"))
    for row in result:
        print(f"Name: {row.NAME}  Age: {row.AGE}")
