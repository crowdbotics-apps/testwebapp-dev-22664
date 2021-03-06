from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()


class Testing(models.Model):
    "Generated Model"
    test = models.BigIntegerField()


class Testtt(models.Model):
    "Generated Model"
    testt = models.BinaryField()


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()


class CustomText(models.Model):
    "Generated Model"
    titleTest = models.CharField(
        blank=True,
        max_length=150,
    )
    name = models.BinaryField(
        null=True,
        blank=True,
    )
    test = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_test",
    )
    emp = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_emp",
    )
    subpage = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_subpage",
    )
    descriptiontest = models.TextField(
        null=True,
        blank=True,
    )
