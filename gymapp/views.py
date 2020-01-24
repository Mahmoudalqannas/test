from django.shortcuts import render, HttpResponse
from gymapp.models import Customers, Subscription, VisitCustomer
from gymapp.forms import CustomersForm, SubscriptionForm, VisitCustomerForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy


class CustomersView(CreateView):
    model = Customers
    template_name = 'customer.html'
    success_url = reverse_lazy ( 'sign_up_customer')
    fields = '__all__'

class SubscriptionView(CreateView):
    model = Subscription
    template_name = 'subscribtions.html'
    success_url = reverse_lazy ('sign_up_subscribtion')
    fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super (SubscriptionView , self).get_context_data(**kwargs)
        context['var']= Subscription.objects.all()
        return context


class VisitCustomerView(CreateView):
    model = VisitCustomer
    template_name = 'visit.html'
    success_url = reverse_lazy ('visit_customer')
    fields = '__all__'


def default_veiw(request):
    return render(request,"base.html")

# Create your views here.
