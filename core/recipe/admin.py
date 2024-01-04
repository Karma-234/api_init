from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserRecipe)
admin.site.register(Favorites)
admin.site.register(OtherUser)
