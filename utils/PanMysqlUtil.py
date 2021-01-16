# coding=utf-8
#
#  Mysql util
#
# Created by Jason Pan on 2021-01-16 21:44:52
# Copyright © 2021 Jason Pan. All rights reserved.
#

if __name__ == '__main__':
    print("mysql")

host_name="106.13.206.58"
port="3306"
db_name="springcloud"
user_name="root"
password="521666"

# 创建连接
from sqlalchemy.dialects.mysql import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine, Column, Integer, String
engine = create_engine("mysql://" + user_name + ":" + password + "@" + host_name + ":" + port + "/" + db_name,
                       echo=True)

# 创建数据库表类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  name = Column(String(64), unique=True)
  email = Column(String(64))
  def __init__(self, name, email):
    self.name = name
    self.email = email

# 生成数据库表
# Base.metadata.create_all(engine)

#
# Base.metadata.delete_all(engine)

# 创建session
from sqlalchemy.orm import sessionmaker
DbSession = sessionmaker(bind=engine)
session = DbSession()

# 新增用户
# add_user = Users("test", "test123@qq.com")
# session.add(add_user)
# session.commit()

# 查询所有
query_users = session.query(Users).order_by(Users.name.asc()).all()
for e in query_users:
  print(e.name)

# 单条数据查询
# query_users = session.query(Users).filter_by(id = 3).first()
# print(query_users.name)

# 更新：1.直接更新
# session.query(Users).filter_by(id=3).update({'name': "Jack"})
# session.commit()

# 更新：2.查出来，再更新
# update_users = session.query(Users).filter_by(id=3).first()
# if update_users:
#   update_users.name = "Bruce Lee"
#   session.add(update_users)
#   session.commit()
# else:
#   print("更新失败")

# 删除
# delete_users = session.query(Users).filter(Users.id == 1).first()
# if delete_users:
#   session.delete(delete_users)
#   session.commit()
# else:
#   print("删除用户不存在！")

# 删除：2.直接删除，推荐此方法
# session.query(Users).filter(Users.id == 1).delete()
# session.commit()

# 最后关闭 session
session.close()

