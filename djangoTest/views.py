from django.shortcuts import render, redirect
from .models import Board
from .forms import AddWork
from django.contrib.auth.decorators import login_required
import itertools
from django.shortcuts import get_object_or_404

def index(request):
    to_do = Board.objects.filter(category='to do')
    in_progress = Board.objects.filter(category='in progress')
    done = Board.objects.filter(category='done')
    works = list(range(max(len(to_do),len(in_progress),len(done))))
    zipped_list = itertools.zip_longest(works, to_do, in_progress, done)
    context = {
        'zipped_list' : zipped_list,
        'to_do' : to_do,
        'in_progress': in_progress,
        'done': done,
    }
    return render(request, 'djangoTest/index.html', context)


@login_required
def add_work(request):
    form = AddWork(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()


    def success_url(self):
        return redirect('/')

    context = {
        'form':form,
        }
    return render(request, 'djangoTest/add_work.html', context)

@login_required
def work_update(request, pk, template_name='djangoTest/work_update.html'):
    work = get_object_or_404(Board, pk=pk)
    form = AddWork(request.POST or None, instance=work)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form, 'id':pk,})


@login_required
def work_delete(request, pk, template_name='djangoTest/work_delete.html'):
    work= get_object_or_404(Board, pk=pk)
    if request.method=='POST':
        work.delete()
        return redirect('/')
    return render(request, template_name, {'object':work})