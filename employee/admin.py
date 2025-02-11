from django.contrib import admin
from .models import Employee, TrainingMaster, SkillMaster, EmployeeSkill, EmployeeTraining

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(TrainingMaster)
class TrainingAdmin(admin.ModelAdmin):
    pass

@admin.register(SkillMaster)
class SkillMasterAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeTraining)
class EmployeeTrainingAdmin(admin.ModelAdmin):
    pass