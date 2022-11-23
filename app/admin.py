from django.contrib import admin
from app.models import AwsInstance

# Register your models here.

@admin.action(description="Destroy Instance")
def destroyInstance(model,request,querySet):
    print(querySet)

@admin.action(description="Stop Instance")
def stopInstance(model,request,querySet):
    print(querySet)

@admin.action(description="Start Instance")
def startInstance(model,request,querySet):
    print(querySet)   

class AwsAdmin(admin.ModelAdmin):
    list_display = ("instance_name","get_user","expiry_time")
    model = AwsInstance
    actions = [destroyInstance,stopInstance,startInstance]
    def get_user(self,obj):
        return obj.user.email

    

    get_user.short_description = 'User'

admin.site.register(AwsInstance,AwsAdmin)