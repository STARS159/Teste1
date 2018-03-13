from django.db import models

# Create your models here.

class Autor(models.Model):
    curriculo = models.CharField(max_length=100)

    def _str_(self):
      return self.curriculo


class EventoCientifico(models.Model):
    issn = models.CharField(max_length=100)
    
    def _str_(self):
      return self.issn

class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100)

    def _str_(self):
      return self.cnpj

class PessoaFisica(models.Model):
    cpf = models.CharField(max_length=100)

    def _str_(self):
      return self.cpf

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    juridica = models.ForeignKey(PessoaJuridica, on_delete=models.CASCADE, null=True, blank=True)
    fisica = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
      return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    eventoPrincipal = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=100)
    logotipo = models.CharField(max_length=100)
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    def _str_(self):
      return self.nome

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    evento = models.OneToOneField(EventoCientifico, on_delete=models.CASCADE)

    def _str_(self):
      return self.titulo