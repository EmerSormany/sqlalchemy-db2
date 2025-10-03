from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, Numeric
from sqlalchemy.orm import declarative_base

# criando conexão com banco de dados
engine = create_engine("sqlite:///db.db", echo=True)

Base = declarative_base()

# Mapeando tabela
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    preco = Column(Numeric(10, 2))
    nome = Column(String(100), nullable=False)
    em_estoque = Column(Boolean, default=True)

Base.metadata.create_all(engine)

# with engine.connect() as connection:
#     result = connection.execute('Select 1')
#     print(result.all())


