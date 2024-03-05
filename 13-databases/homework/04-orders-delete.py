from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    conn.execute(text('''CREATE TABLE IF NOT EXISTS Orders
        (Id INT PRIMARY KEY NOT NULL,
        DatePlaced TEXT);'''))

    conn.execute(text('''
        INSERT INTO Orders
        VALUES (1, date("2024-01-01T00:00:00Z")),
               (2, date("2023-01-01T00:00:00Z")),
               (3, date("2022-12-01T00:00:00Z"));
    '''))
    conn.commit()

    result = conn.execute(text("SELECT * FROM Orders WHERE DatePlaced < date(\"2023-01-01T00:00:00Z\")"))
    for row in result:
        print(f"ProductName: {row.Id} DatePlaced: {row.DatePlaced}")
