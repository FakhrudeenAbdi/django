from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)



from .models import Post, Editor

admin.site.register(Editor)
