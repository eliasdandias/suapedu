from django.shortcuts import render
from . models  import*

def cidade(request):
    cidade = {
         'pessoas':Cidade.objects.all()
    }
    
    return render(request,'consulta/cidade.html', cidade)

def pessoas(request):
    pessoas = {
         'pessoas':Pessoas.objects.all()
    }
    
    return render(request,'consulta/pessoas.html', pessoas)

def matricula(request):
    matricula = {
         'matriculas':Matricula.objects.all()
    }
    
    return render(request,'consulta/matricula.html', matricula)

def curso(request):
    curso = {
        'curso':Cursos.objects.all()
    }
    
    return render(request,'consulta/curso.html',curso)

def instituicao(request):
    Instituicao_de_ensino = {
        'Instituicao_de_ensino': Instituicao_de_ensino.objects.all()
    }
    
    return render(request, 'consulta/Instituicao_de_ensino.html', Instituicao_de_ensino)

def ocupacao(request):
    ocupacao = {
        'ocupacao': Ocupacao.objects.all()
    }
    
    return render(request, 'consulta/ocupacao.html', ocupacao)