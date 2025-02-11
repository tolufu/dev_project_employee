from django.urls import path
from .import views

app_name = "employee"

urlpatterns = [
    path("", views.index,name="index"), # /employee のときだけviews.indexが呼ばれる
    path("detail/<int:pk>", views.detail, name="detail"),

    path("info_add/", views.add, name="add"), # /employee/add
    path("info_update/<int:pk>", views.update, name="update"),
    path("info_delete/<int:pk>", views.delete, name="delete"),

    path("training_add/<int:pk>/training/", views.train_add_update, name="train_add"), # /employee/add
    path("training_update/<int:pk>/training/<str:training_id>", views.train_add_update, name="train_update"), # /employee/add
    path("training_delete/<int:pk>/training/<str:training_id>", views.train_delete, name="train_delete"),

    path("skill_add/<int:pk>/skill/", views.skill_add_update, name="skill_add"), # /employee/add
    path("skill_update/<int:pk>/skill/<str:skill_id>", views.skill_add_update, name="skill_update"), # /employee/add
    path("skill_delete/<int:pk>/skill/<str:skill_id>", views.skill_delete, name="skill_delete"),
]
