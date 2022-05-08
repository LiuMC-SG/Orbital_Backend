from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class ModuleCondensed(models.Model):
    key = models.TextField(primary_key=True)
    moduleCode = models.TextField()
    title = models.TextField()
    semesters = ArrayField(models.IntegerField())

    def __str__(self):
        return self.key


class Module(models.Model):
    key = models.TextField(primary_key=True)
    acadYear = models.TextField()
    preclusion = models.TextField(null=True, blank=True)
    description = models.TextField()
    title = models.TextField()
    department = models.TextField()
    faculty = models.TextField()
    workload = models.TextField(null=True, blank=True)
    prerequisite = models.TextField(null=True, blank=True)
    moduleCredit = models.TextField()
    moduleCode = models.TextField()
    semesterData = ArrayField(models.JSONField())
    prereqTree = models.JSONField(null=True, blank=True)
    fulfillRequirements = ArrayField(models.TextField(), null=True, blank=True)

    def __str__(self):
        return self.key
