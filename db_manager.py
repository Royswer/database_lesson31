from sqlalchemy import Integer, String, Boolean, Date, Text, create_engine, ForeignKey, insert, select, update, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from db_models import Base, User, Posts, Albums, Comments, Photos

class DB:
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite+pysqlite:///{db_path}")
    
    def create_db(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, id, name, username, phone):
        with Session(self.engine) as session:
            q = insert(User).values(id = id, name = name, username = username, phone = phone).prefix_with('OR IGNORE')
            session.execute(q)
            session.commit()
    
    def add_posts(self, id, user_id, title, body):
        with Session(self.engine) as session:
            q = insert(Posts).values(id = id, userId = user_id, title = title, body = body)
            session.execute(q)
            session.commit()
    
    def add_users(self, users: list[dict]):
        with Session(self.engine) as session:
            q = insert(User).prefix_with('OR IGNORE')
            session.execute(q, users)
            session.commit()

#Тесты:
if __name__ == '__main__':
    db_manager = DB('test.db')
    db_manager.add_users([{
        'name': 'NekiTest',
        'username': 'Royswer',
        'phone': '12345'
    },{
        'name': 'RobTest',
        'username': 'Rob',
        'phone': '123467'
    }])
# db_manager.add_user('Robert', 'Rob', '123')

