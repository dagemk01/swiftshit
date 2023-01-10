from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Appointments
from accounts.models import CustomUser
from django.views.generic import ListView, CreateView, DetailView, TemplateView, DeleteView, UpdateView

from .forms import AppointmentsForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseNotAllowed
from mail.mailhelper import mail_helper, mailer

# Create your views here.

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointments
    template_name = 'apphome.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        elif request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return HttpResponseNotAllowed(['GET', 'POST'])

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        appt = Appointments.objects.get(pk=kwargs['arg1'])
        appt.confirmed = True
        appt.save()


        print("postt baby ")
        print(appt.confirmed)

        reciever = appt.email
        sub = "Appointment Has been confrimed by " + str(appt.salon)
        infosent = "Your appointment has been confrimed by! We are exited to have you!" 
        mailer(reciever, sub, infosent)
        


        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # Query the database for objects that match certain criteria
        return Appointments.objects.filter(salon=self.request.user)
'''    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["con"] = len(Appointments.objects.filter(salon=self.request.user, confirmed=True))
        context["notcon"] = len(Appointments.objects.filter(salon=self.request.user, confirmed=False))
        return context
'''  

class AppointmentCreateView(CreateView):
    model = Appointments
    template_name = 'appnew.html'
    form_class = AppointmentsForm
    success_url = reverse_lazy('appointment_created')

    def form_valid(self, form):
        form.instance.confirmed = False
        form.instance.salon = CustomUser.objects.get(pk=self.kwargs['pk'])

        reciever = form.instance.email
        sub = "New Appt Created at " + str(form.instance.salon )
        infosent = "Your appointment has been vreated. We will let you know when the appointment is confirmed."
        mailer(reciever, sub, infosent)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(pk=self.kwargs['pk'])
        context['business_name'] = user.business_name

        print (context['business_name'])

        return context


class AppointmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Appointments
    template_name = 'appdetail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.salon == self.request.user

class AppointmentCreatedView(TemplateView):
    template_name = 'appsuccess.html'


class AppointmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Appointments
    template_name = 'appdelete.html'
    success_url = reverse_lazy('appointment_home')

    def test_func(self):
        obj = self.get_object()
        return obj.salon == self.request.user

    


class AppointmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Appointments
    template_name = 'appupdate.html'
    fields = [
        'date',
        'time',
        'confirmed'
    ]
    
    def test_func(self):
        obj = self.get_object()
        return obj.salon == self.request.user
    
    def form_valid(self, form): 
        print ("Line: 106") # new
        app = Appointments.objects.get(pk=self.kwargs['pk'])
        if (form.instance.time != app.time):
            print ("Line: 108")
            reciever = app.email
            sub = "Your Appt has been edited"
            infosent = "the new time here: " + str(form.instance.time)
            print(reciever)
            print(sub)
            print("old appointment time was:" + str(app.time))
            print(infosent)
            #mail_helper(reciever, sub, infosent)
            mailer(reciever, sub, infosent)
        return super().form_valid(form)
    
