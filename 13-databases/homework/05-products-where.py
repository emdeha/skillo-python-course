from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    conn.execute(text('''CREATE TABLE IF NOT EXISTS Products
        (Id INT PRIMARY KEY NOT NULL,
        ProductName TEXT NOT NULL,
        UnitPrice REAL,
        SupplierId INT,
        QuantityPerUnit REAL,
        CategoryId INT);'''))

    conn.execute(text('''
        INSERT INTO Products
        VALUES (3, "Laptop Acer", 999.99, 3, 3, 3),
               (4, "Laptop HP", 999.99, 3, 3, 2),
               (2, "Laptop Dell", 999.99, 3, 3, 2),
               (5, "Mouse", 39.99, 3, 3, 2),
               (6, "Headphones", 19.99, 3, 3, 2),
               (7, "Keyboard", 30.99, 3, 3, 2),
               (1, "Laptop Mitsubishi XS200", 999.99, 3, 3, 2);
    '''))
    conn.commit()

    result = conn.execute(text("SELECT ProductName, UnitPrice FROM Products WHERE UnitPrice < 50"))
    for row in result:
        print(f"ProductName: {row.ProductName} UnitPrice: {row.UnitPrice}")
