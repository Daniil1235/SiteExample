from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("", views.index, name="home"),
                  path("create/", views.create, name="create"),
                  path("tasks/<int:id>", views.detail_view, name="detail_view"),
                  path("tasks/<int:pk>/update", views.TaskUpdateView.as_view(), name="task_update"),
                  path("tasks/<int:pk>/delete", views.TaskDeleteView.as_view(), name="task_delete"),
                  path("register", views.register_request, name="register")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
