from django.contrib import admin
from .models import Users, Messages, Histories, Plans # Account, AdminAccount

# Register your models here.

admin.site.register(Users)
admin.site.register(Messages)
admin.site.register(Histories)
admin.site.register(Plans)
# admin.site.register(Account)
# admin.site.register(AdminAccount)
