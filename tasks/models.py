from django.db import models
from users.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')
    #assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateField()
    due_date = models.DateField()
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)


    def __str__(self):
        return self.task_name
