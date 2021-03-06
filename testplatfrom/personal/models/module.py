from django.db import models
from personal.models.project import Project

class Module(models.Model):
    """模块表"""
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null = False)
    describe = models.TextField(default ="")
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name