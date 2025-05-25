from sqlalchemy import Integer, String, Boolean, Date, Text, create_engine, ForeignKey, insert, select, update, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class DB:
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite+pysqlite:///{db_path}")
    
    def create_db(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, id, name, username, phone):
        with Session(self.engine) as session:
            user = insert(User).values(id = id, name = name, username = username, phone = phone)
            session.execute(user)
            session.commit()


db_manager = DB('test.db')
db_manager.create_db()
db_manager.add_user('Robert', 'Rob', '123')

# with Session(engine) as session:
#     Robert = insert(User).values(name = 'Robert', username = 'Rob', phone = '123')
#     Neki = insert(User).values(name = 'Neki', username = 'Neki', phone = '456')
#     session.execute(Robert)
#     session.execute(Neki)
#     session.commit()

# with Session(engine) as session:
#     query = select(User.name, User.phone).where(User.id < 4)
#     result = session.execute(query)
#     print(result)
#     for row in result:
#         print(row[0])

# with Session(engine) as session:
#     del_ = delete(User).where(User.id == 3)
#     session.execute(del_)
#     session.commit() 

# with Session(engine) as session:
#     update_ = update(User).values(username = 'Royswer').where(User.username == 'Neki')
#     session.execute(update_)
#     session.commit()

# with Session(engine) as session:
#     ins = insert(Posts).values(userId = 2, title = 'Good bye', body = 'bye')
#     session.execute(ins)
#     session.commit()

# with Session(engine) as session:
#     select_ = select(User.name, User.id, Posts.userId)\
#         .join(Posts, User.id == Posts.userId)\
#         .where()\
#         .group_by()\
#         .order_by()\
#         .limit()
#     result = session.execute(select_)
#     for row in result:
#         print(row)