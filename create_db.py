import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS entregas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    cidade TEXT,
    data_envio TEXT,
    data_entrega TEXT
)
''')

dados = [
    ('Ricardo', 'São Paulo', '2026-04-01', '2026-04-03'),
    ('Maria', 'Rio de Janeiro', '2026-04-02', '2026-04-06'),
    ('Pedro', 'Belo Horizonte', '2026-04-03', '2026-04-05'),
    ('Beatriz', 'Curitiba', '2026-04-04', '2026-04-10'),
    ('Lucas', 'São Paulo', '2026-04-05', '2026-04-07')
]

cursor.executemany('''
INSERT INTO entregas (cliente, cidade, data_envio, data_entrega)
VALUES (?, ?, ?, ?)
''', dados)

conn.commit()
conn.close()

print("Banco criado com sucesso!")