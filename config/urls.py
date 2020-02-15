from django.contrib import admin
from django.urls import path, include
import viewcrud.views
import viewcrud.urls
# import classcrud.views
# import classcrud.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name="welcome"),
    path('funccrud/', include('viewcrud.views')),
    # path('classcrud/', include('classcrud.views')),
]
