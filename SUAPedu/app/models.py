from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    UF = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.UF}'


class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.pai} {self.mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade}'
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Instituicao_de_ensino (models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone}'
    
class Areas_do_saber(models.Model):
        nome = models.CharField(max_length=50)

        def __str__(self):
            return self.nome

class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.DecimalField(max_digits=5,decimal_places=2)
    duracao_meses = models.CharField(max_length=50)
    area_saber = models.ForeignKey(Areas_do_saber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao_de_ensino, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_emprestimo} {self.livro} {self.leitor} {self.data_devolucao}'
    

class Periodos(models.Model):
    periodo = models.CharField(max_length=50)
    
    def __str__(self):
            return self.periodo
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    area_saber = models.ForeignKey(Areas_do_saber, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.area_saber}'

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao_de_ensino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    area_saber = models.ForeignKey(Areas_do_saber, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.area_saber} {self.data_inicio} {self.data_previsao_termino}'

class Avalicoes(models.Model):
    descricao = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'

class Frequencias(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.numero_faltas}'

class Turmas(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.periodo}'

class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=50)
    data = models.DateField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.data} {self.curso} {self.disciplina} {self.pessoa}'

class Disciplinas_por_cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.DecimalField(max_digits=5,decimal_places=2)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.curso} {self.periodo}'

class Tipos_de_avaliacao(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
            return self.tipo

