from django.db import models

class LeaveRequest(models.Model):
    LEAVE_TYPES = (
        ('Credit Leave', 'Credit Leave'),
        ('Personal Leave', 'Personal Leave'),
        ('Sick Leave', 'Sick Leave'),
    )
    leave_type = models.CharField(max_length=200, choices=LEAVE_TYPES)
    from_date = models.DateField("start-date")
    to_date = models.DateField("to-date")
    reason = models.TextField()
