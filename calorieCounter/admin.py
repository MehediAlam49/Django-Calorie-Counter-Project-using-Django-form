from django.contrib import admin
from calorieCounter.models import *

# Register your models here.
admin.site.register([
    User,
    BasicInfoModel,
    ConsumedCalories,
])