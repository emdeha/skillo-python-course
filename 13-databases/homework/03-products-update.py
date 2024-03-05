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
               (1, "Laptop Mitsubishi XS200", 999.99, 3, 3, 2);
    '''))
    conn.commit()

    conn.execute(text("UPDATE Products SET UnitPrice = UnitPrice * 1.1 WHERE CategoryId = 3"))
    conn.commit()

    result = conn.execute(text("SELECT * FROM Products"))
    for row in result:
        print(f"ProductName: {row.ProductName} UnitPrice: {row.UnitPrice} CategoryId: {row.CategoryId}")
