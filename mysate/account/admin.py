from django.contrib import admin
from .models import UserBase, Invitation

admin.site.register(UserBase)
admin.site.register(Invitation)
