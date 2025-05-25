from sqlalchemy import Integer, String, Boolean, Date, Text, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(100))

class Posts(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    userId: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(1000))
    body: Mapped[str] = mapped_column(String(1000))

class Photos(Base):
    __tablename__ = "photos"
    id: Mapped[int] = mapped_column(primary_key=True)
    albumId: Mapped[int] = mapped_column
    title: Mapped[str] = mapped_column(String(3000))
    url: Mapped[str] = mapped_column(String(1000))
    thumbnailUrl: Mapped[str] = mapped_column(String(1000))

class Comments(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    postId: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    name: Mapped[str] = mapped_column(String(3000))
    email: Mapped[str] = mapped_column(String(3000))
    body: Mapped[str] = mapped_column(String(3000))

class Albums(Base):
    __tablename__ = "albums"
    id: Mapped[int] = mapped_column(primary_key=True)
    userId: Mapped[int] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str] = mapped_column(String(3000))
    
engine = create_engine("sqlite+pysqlite:///users.db")
Base.metadata.create_all(engine)