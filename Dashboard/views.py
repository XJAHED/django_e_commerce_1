from django.shortcuts import render

# Create your views here.

def CustomAdmin(request):
    context ={}
    return render(request, "html/dashboard/admin.html", context)