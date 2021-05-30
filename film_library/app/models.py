from django.db import models


class Person(models.Model):
    first_name = models.CharField('имя', max_length=200)
    last_name = models.CharField('фамилия', max_length=200)
    birth_date = models.DateField('дата рождения')
    photo_url = models.CharField('ссылка на фото', max_length=200)

    def __str__(self):
        return self.first_name.__str__() + ' ' + self.last_name.__str__()


class Genre(models.Model):
    genre_name = models.CharField('название жанра', max_length=200)


class Film(models.Model):
    film_name = models.CharField('название фильма', max_length=200)
    pub_date = models.DateField('дата выхода')
    box_office = models.IntegerField('кассовые сборы')
    producer = models.ForeignKey(Person, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.film_name


