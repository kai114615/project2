from django.db import models, connection
from django.db.utils import DatabaseError

# Create your models here.
class Category:
    def all():

        # 第二步 SQL語法
        sql = 'SELECT * FROM category'
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                categories = cursor.fetchall()
                return categories
        except DatabaseError as e:
            print(f"讀取資料錯誤: {e}")
            return None
        


    def single():
        pass

    def create():
        pass

    def update():
        pass

    def delete():
        pass