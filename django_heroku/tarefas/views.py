from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_heroku.tarefas.forms import TarefaNovaForm
from django.urls import reverse
from django_heroku.tarefas.models import Tarefa

# Create your views here.
def home(request):
    tarefas_pendentes = Tarefa.objects.filter(feita=False)
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False)
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    
    tarefas_pendentes = Tarefa.objects.filter(feita=False)
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})
