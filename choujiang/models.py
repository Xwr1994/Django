from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    card_id = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.english_name + " " + str(self.card_id)


class People_first(models.Model):
    name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    card_id = models.IntegerField()


class People_second(models.Model):
    name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    card_id = models.IntegerField()


class People_third(models.Model):
    name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    card_id = models.IntegerField()

