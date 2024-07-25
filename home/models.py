from django.db import models, connection

# Create your models here.


class Sakila:
    def country():
        with connection.cursor() as cursor:
            cursor.execute('SELECT country_id, country FROM country')
            country = cursor.fetchall()
            return country

    def categories():
        with connection.cursor() as cursor:
            cursor.execute('select category_id, name from category')
            categories = cursor.fetchall()
            return categories

    def cities(id=1):
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT city_id, city FROM sakila.city where country_id={id}')
            cities = cursor.fetchall()
            return cities