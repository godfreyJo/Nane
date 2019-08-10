from django.shortcuts import render

def customer_list(request):
    return render(request, 'property/customer_list.html', {})


