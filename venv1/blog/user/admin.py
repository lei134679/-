from django.contrib import admin
from .models import *


admin.site.register(Users)
admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(Comment)
