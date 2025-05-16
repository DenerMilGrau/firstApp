#importar biblioteca.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean, DateTime

#importar session e sessionmaker.
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

#configurar a conexão de banco.
engine = create_engine('sqlite:///base_estoque.sqlite3')

#gerenciar sessao com banco de dados.
local_session = sessionmaker(bind=engine)

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, index=True)
    profissao = Column(String, nullable=False, index=True)
    salario = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except:
            db_session.rollback()
            raise

    def serialize_pessoa(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'profissao': self.profissao,
        }
class Livro(Base):
    __tablename__ = 'livro'
    id_livro = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except:
            db_session.rollback()
            raise

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()