from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from demo90 import User, Base

sqlite_engine1 = create_engine('sqlite:///c:\\Users\\Admin\\sqlalchemy.db', echo=True)
print([User.__tablename__, User.__table__])
Base.metadata.create_all(sqlite_engine1)

SqliteSession = sessionmaker(bind=sqlite_engine1)
session1 = SqliteSession()
user1 = User(name='Mark', fullname="Mark Ho",password='mark password')
user2 = User(name='Tim', fullname='Tim Chen',password='tim password')
session1.add(user2)
session1.add(user1)
session1.commit()

session2 = SqliteSession()
all_user = session2.query(User)
for user in all_user:
    print user
session2.commit()

session3 = SqliteSession()
user_to_modify = session3.query(User).filter_by(name="Tim").first()
print("[b]current dirty list:",[session3.dirty])
user_to_modify.fullname="TIM CHEN!"
print("[a]current dirty list:",[session3.dirty])
user3 = User(name='James', fullname='James Liu',password='whatever')
print("[b]new list", session3.new)
session3.add_all([user3])
print("[a]new list", session3.new)
session3.commit()
