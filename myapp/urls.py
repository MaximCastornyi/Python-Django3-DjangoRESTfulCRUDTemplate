from django.urls import include, path, re_path
from .views import EmployeeRUDView, EmployeeView


urlpatterns = [
    # update, delete
    re_path(r'^api/employees/(?P<pk>[0-9]+)$', EmployeeRUDView.as_view(),  name='employee_rud'),
    # get all ad create
    path('api/employees/', EmployeeView.as_view(), name='employee_view')
]