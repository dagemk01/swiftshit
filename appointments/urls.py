from django.urls import path
from .views import AppointmentListView, AppointmentCreateView, AppointmentDetailView, AppointmentCreatedView, AppointmentUpdateView, AppointmentDeleteView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_home'),
    path('<int:arg1>/', AppointmentListView.as_view(), name='appointment_home'),
    path('<int:pk>/new/', AppointmentCreateView.as_view(), name='appointment_new'),
    path('<int:pk>/detail/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('success/', AppointmentCreatedView.as_view(), name='appointment_created')
]
