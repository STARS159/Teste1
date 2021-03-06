# Generated by Django 2.0.2 on 2018-03-13 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test.Autor'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='fisica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test.PessoaFisica'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='juridica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test.PessoaJuridica'),
        ),
    ]
