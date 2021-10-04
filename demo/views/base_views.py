from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Demo

def index(request):
    page = request.GET.get('page', '1')

    demo_list = Demo.objects.order_by('-create_date')

    # page
    paginator = Paginator(demo_list, 12)
    page_obj = paginator.get_page(page)

    context = {'demo_list': page_obj}

    return render(request, 'demo/demo_list.html', context)

def detail(request, demo_id):
    demo = get_object_or_404(Demo, pk=demo_id)
    context = {'demo': demo}
    return render(request, 'demo/demo_detail.html', context)