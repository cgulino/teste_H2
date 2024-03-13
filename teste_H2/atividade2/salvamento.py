from sqlalchemy import create_engine

def salvar(grouped):
    # Definindo o caminho do banco de dados SQLite
    database_path = "h2club.mysql"

    # Criar engine para SQLite
    engine_sqlite = create_engine(f"mysql:///{database_path}")

    # Salvar dados consolidados no SQLite
    grouped.to_sql('consolidated_data', engine_sqlite, if_exists='append', index=False)
