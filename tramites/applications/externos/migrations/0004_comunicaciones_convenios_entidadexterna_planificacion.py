# Generated by Django 3.0.6 on 2020-12-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('externos', '0003_auto_20201223_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entidad', models.CharField(max_length=250, verbose_name='Entidad')),
            ],
        ),
        migrations.CreateModel(
            name='planificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.PositiveIntegerField(verbose_name='Numero')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('guianro', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tramite Nro')),
                ('categoria', models.CharField(choices=[('1', 'MEMORANDO'), ('2', 'INFORME TECNICO'), ('3', 'TRAMITE EXTERNO'), ('4', 'OFICIO')], default='1', max_length=1, verbose_name='Categoria')),
                ('referencia', models.CharField(max_length=200, verbose_name='Referencia')),
                ('asunto', models.TextField(max_length=500, verbose_name='Asunto')),
                ('remitente', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remitente')),
                ('destinatario', models.CharField(max_length=250, verbose_name='Destinatario')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('atendido', models.BooleanField(default=False, verbose_name='Atendido')),
                ('departamento', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Origen', to='externos.Dependencias')),
                ('departamentof', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Destino', to='externos.Dependencias')),
            ],
            options={
                'verbose_name': 'Planificacion',
                'verbose_name_plural': 'Planificacion',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='convenios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.PositiveIntegerField(verbose_name='Numero')),
                ('institucion', models.CharField(max_length=350, verbose_name='Institucion')),
                ('convenio', models.CharField(max_length=450, verbose_name='Convenio')),
                ('objeto', models.TextField(verbose_name='Objeto')),
                ('plazo', models.PositiveIntegerField(verbose_name='Plazo')),
                ('fechainicio', models.DateField(verbose_name='Fecha Inicio')),
                ('fechafinal', models.DateField(verbose_name='Fecha Final')),
                ('cumplimiento', models.CharField(choices=[('1', 'EN EJECUCION'), ('2', 'POR FINALIZAR'), ('3', 'FINALIZADO'), ('4', 'RETRASADO')], default='1', max_length=1, verbose_name='Cumplimiento')),
                ('encargado', models.CharField(max_length=520, verbose_name='Encargado')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('dependencia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='externos.Dependencias')),
            ],
            options={
                'verbose_name': 'Convenios',
                'verbose_name_plural': 'Convenios',
                'ordering': ['-fechainicio'],
            },
        ),
        migrations.CreateModel(
            name='Comunicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4, verbose_name='Numero')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('medios', models.CharField(choices=[('1', 'Quipux'), ('2', 'Correo'), ('3', 'Otro')], default='1', max_length=1, verbose_name='Medio')),
                ('remite', models.CharField(max_length=350, verbose_name='Remitente')),
                ('asunto', models.CharField(max_length=350, verbose_name='Asunto')),
                ('contestado', models.CharField(max_length=10, verbose_name='Contestado por Oficio Nro')),
                ('observacion', models.TextField(verbose_name='Observacion')),
                ('entidad', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='externos.EntidadExterna')),
            ],
            options={
                'verbose_name': 'Comunicaciones',
                'verbose_name_plural': 'Comunicaciones',
                'ordering': ['-fecha'],
            },
        ),
    ]
