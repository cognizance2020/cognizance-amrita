from django.db import models
from django.contrib.auth.models import Group

class Member(models.Model):
    ROLE = (
        ('Member','Member'),
        ('Administrator','Administrator')
    )

    group_names = []

    query_set = Group.objects.all()

    for g in query_set:
        group_names.append((g.name,g.name))
    
    group_names = tuple(group_names)

    fullname = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True, choices=ROLE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    github_username = models.CharField(max_length=50, null=True)
    discord_handle = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class Achievement(models.Model):

    title = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=1000, null=True)
    achievers = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True)
    date = models.DateField(null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    

class Task(models.Model):
    #title,desc, goal, author, content, zipfile, submission link, deadline, starting_time, max_score, group

    members = Member.objects.all()

    auth_names = []

    for m in members:
        auth_names.append((m.fullname,m.fullname))
    
    auth_names = tuple(auth_names)

    query_set = Group.objects.all()

    group_names = []

    for g in query_set:
        group_names.append((g.name,g.name))
    
    group_names = tuple(group_names)

    title = models.CharField(max_length=200, null=True)
    goal = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=200, null=True, choices=auth_names)
    content = models.TextField(max_length=2000, null=True)
    deadline = models.DateTimeField(null=True)
    starting_time = models.DateTimeField(null=True)
    max_score = models.FloatField(null=True)
    group = models.CharField(max_length=200, null=True, choices=group_names)
    resource_file = models.FileField(null=True)
    submission_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
    
class Submission(models.Model):

    members = Member.objects.all()

    auth_names = []

    for m in members:
        auth_names.append((m.fullname,m.fullname))
    
    auth_names = tuple(auth_names)

    task_id = models.IntegerField(null=True)
    fullname = models.CharField(max_length=200, null=True)
    score = models.FloatField(max_length=50, null=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    submission_file = models.FileField(null=True)
    submission_text = models.CharField(max_length=500, null=True)
    evaluator = models.CharField(choices=auth_names, max_length=200, null=True)
    feedback = models.CharField(max_length=500, null=True)
    

    def __str__(self):
        return self.fullname
    
