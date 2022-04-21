from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_operator     = models.BooleanField(default=False)

    def is_admin(self):
        if self.groups.filter(name='Admin').exists():
            return True
        else:
            return False
    def is_Operator(self):
        if self.groups.filter(name='Operator').exists():
            return True
        else:
            return False
    def is_super_admin(self):
        if self.groups.filter(name='SuperAdmin').exists():
            return True
        else:
            return False
    def is_supervisor(self):
        if self.groups.filter(name='Supervisor').exists():
            return True
        else:
            return False
    def is_approver(self):
        if self.groups.filter(name='Approver').exists():
            return True
        else:
            return False

