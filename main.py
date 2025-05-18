from sqlalchemy import Integer, String, Boolean, Date, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(100))
 


engine = create_engine("sqlite+pysqlite:///users.db")
Base.metadata.create_all(engine)