from django.db import models

# class LeaveType(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=2054,blank=True,null=True)
#     no_of_leaves = models.DecimalField(default=0)

class LeaveRequest(models.Model):
    LEAVE_TYPES = (
        ('Credit Leave', 'Credit Leave'),
        ('Personal Leave', 'Personal Leave'),
        ('Sick Leave', 'Sick Leave'),
    )
    leave_type = models.CharField(max_length=200, choices=LEAVE_TYPES)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    description = models.CharField(max_length=2054,blank=True,null=True)
    No_of_Leaves=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.leave_type



