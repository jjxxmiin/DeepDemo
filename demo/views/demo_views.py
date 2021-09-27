from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..forms import DemoForm
from ..models import Demo


@login_required(login_url='common:login')
def demo_create(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            demo = form.save(commit=False)
            demo.author = request.user
            demo.photo = request.FILES['photo']
            demo.create_date = timezone.now()
            demo.save()
            return redirect('demo:index')

    else:
        form = DemoForm()
    context = {'form': form}
    return render(request, 'demo/demo_form.html', context)


@login_required(login_url='common:login')
def demo_modify(request, demo_id):
    demo = get_object_or_404(Demo, pk=demo_id)
    if request.user != demo.author:
        messages.error