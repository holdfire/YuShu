from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# mvc模式中的model层
# 使用sqlalchemy将下面的模型映射到sql中去
# flask对此做了一个封装，名为Flask_SQLAlchemy
# code first让我们专注于业务模型的设计，而不是专注数据库的设计
class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    image = Column(String(50))

    # code first关注数据库相关的数据表如何创建
    # ORM 对象关系映射：还包括数据的删除、查询等
    def sample(self):
        pass


