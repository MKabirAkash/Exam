from django.contrib import admin
from .models import Employees
from .models import Gadgets,GotGadgetPermission




admin.site.register(Employees)
admin.site.register(Gadgets)
admin.site.register(GotGadgetPermission)
