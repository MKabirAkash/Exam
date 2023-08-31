from django.contrib import admin
from .models import Employees
from .models import Gadgets,GotGadgetPermission,Gadgettrackinfo




admin.site.register(Employees)
admin.site.register(Gadgets)
admin.site.register(GotGadgetPermission)
admin.site.register(Gadgettrackinfo)