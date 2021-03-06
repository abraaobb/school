from django.db import models


# Create your models here.
class Course(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=40,
        null=False
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'course'
        managed = True
