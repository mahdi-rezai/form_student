from django.shortcuts import render, redirect
from .forms import StudentForm , StudentLoginForm
from django.db.models import Q
from .models import Student
from django.contrib import messages
from django.shortcuts import get_object_or_404

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'form/home.html', {'form': form})

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(major__icontains=query)
        )
    else:
        students = Student.objects.all()
    return render(request, 'form/student_list.html', {'students': students})

def student_login(request):
    form = StudentLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(first_name=first_name, password=password)
                messages.success(request, f"خوش آمدید {student.first_name}!")
                return redirect('edit_student', pk=student.pk)  # ریدایرکت به صفحه ویرایش
            except Student.DoesNotExist:
                messages.error(request, "نام یا رمز اشتباه است.")
    return render(request, 'form/student_login.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "اطلاعات با موفقیت ویرایش شد.")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'form/edit_student.html', {'form': form, 'student': student})