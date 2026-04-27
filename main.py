import sqlite3
import pandas as pd

def main():
    print("=== MiniLog - Análise de Entregas ===\n")

    conn = sqlite3.connect('database.db')

    df = pd.read_sql_query("SELECT * FROM entregas", conn)

    # Converter datas
    df['data_envio'] = pd.to_datetime(df['data_envio'])
    df['data_entrega'] = pd.to_datetime(df['data_entrega'])

    # Calcular tempo de entrega
    df['tempo_entrega'] = (df['data_entrega'] - df['data_envio']).dt.days

    print("📦 Dados:")
    print(df)

    # Total
    print(f"\nTotal de entregas: {len(df)}")

    # Atrasos (> 3 dias)
    atrasadas = df[df['tempo_entrega'] > 3]
    print(f"Entregas atrasadas: {len(atrasadas)}")

    # Média
    media = df['tempo_entrega'].mean()
    print(f"Tempo médio: {media:.2f} dias")

    # Por cidade
    cidade = df.groupby('cidade')['tempo_entrega'].mean()
    print("\nTempo médio por cidade:")
    print(cidade)

    conn.close()

if __name__ == "__main__":
    main()