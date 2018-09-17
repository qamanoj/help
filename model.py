from django.db import models


class UserRegister(models.Model):
    firstname             = models.CharField(max_length=60)
    lastname              = models.CharField(max_length=60)
    number                = models.IntegerField()
    email                 = models.CharField(max_length=60)
    password              = models.CharField(max_length=60)
    user_ip               = models.CharField(max_length=60)
    user_register_time    = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user_last_login_time  = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return 'user register'
