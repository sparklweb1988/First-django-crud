from django.shortcuts import get_object_or_404, redirect, render

from app.models import Info




def create(request):
    if request.method =='POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        new_list = Info(full_name=full_name,email=email,age=age)
        new_list.save()
        return redirect('index')
    list_info = Info.objects.all()
    return render(request, 'index.html',{'list_info':list_info})





def index(request):
    list = Info.objects.all()
    return render(request, 'index.html',{'list':list})





def update(request, id):
    list = get_object_or_404(Info, pk=id)
    if request.method=='POST':
       list.full_name = request.POST.get('full_name')
       list.email = request.POST.get('email')
       list.age = request.POST.get('age')
       list.save()
       return redirect('index')
    return render(request, 'update.html',{'list':list })




def delete(request, id):
    list = get_object_or_404(Info, pk=id)
    list.delete()
    return redirect('index')



