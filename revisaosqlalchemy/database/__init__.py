from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Criação do motor de conexão para o banco de dados
engine = create_engine('sqlite:///database.db', echo=True)

# Definição da base de todos os modelos
Base = declarative_base()

# Criação de uma sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()  # Usaremos a session diretamente
