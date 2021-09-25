from django.shortcuts import render, get_object_or_404
from ..models import Demo

def index(request):
    demo_list = Demo.objects.all()
    context = {'demo_list': demo_list}
    return render(request, 'demo/demo_list.html', context)

def detail(request, demo_id):
    print(demo_id)
    demo = get_object_or_404(Demo, pk=demo_id)
    context = {'demo': demo}
    return render(request, 'demo/demo_detail.html', context)