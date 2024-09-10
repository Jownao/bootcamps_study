from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # Importa exceções do SQLAlchemy

from desafio import Fornecedor, Produto
# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.

Base = declarative_base()

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")
