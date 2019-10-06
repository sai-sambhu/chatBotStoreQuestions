from django.contrib import admin

# Register your models here.
from basic_app.models import ChatBotAdmin
from basic_app.models import QandAModel

admin.site.register([ChatBotAdmin,QandAModel])
