from django.shortcuts import render
from .models import Student
def profile(request):
    student = student.objects.first()
    return render(request, 'students/profile.html',{'student':student})

