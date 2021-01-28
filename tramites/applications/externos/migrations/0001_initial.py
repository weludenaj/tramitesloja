# Generated by Django 3.0.6 on 2021-01-19 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerocontrato', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contrato Nro')),
                ('administrador', models.CharField(default='No asignado', max_length=250, verbose_name='Administrador')),
                ('nombredelcontrato', models.TextField(verbose_name='Nombre del Contrato')),
                ('contratista', models.TextField(blank=True, null=True, verbose_name='Contratista')),
                ('fechainicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('fechafinal', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')),
                ('memosend', models.TextField(blank=True, null=True, verbose_name='Memos Enviados')),
                ('memoreceived', models.TextField(blank=True, null=True, verbose_name='Memos Recibidos')),
            ],
            options={
                'verbose_name': 'Administrador de Contratos',
                'verbose_name_plural': 'Administrador de Contratos',
                'ordering': ['administrador'],
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='contraloria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secuencia', models.PositiveIntegerField(default=0)),
                ('fechaingreso', models.DateField(verbose_name='Fecha')),
                ('memorando', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nro Memo/Oficio')),
                ('recomendacion', models.TextField(verbose_name='Recomendación')),
                ('dependencia', models.CharField(max_length=50, verbose_name='Dirigido a ')),
                ('funcionario', models.TextField(verbose_name='Funcionario')),
                ('contestacion', models.TextField(blank=True, null=True, verbose_name='Remitente')),
                ('seguimiento', models.TextField(blank=True, null=True, verbose_name='Seguimiento realizado')),
                ('fechalastupdate', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('concluido', models.BooleanField(default=False, verbose_name='Atendido')),
                ('documentos', models.FileField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Exámenes de contraloria',
                'verbose_name_plural': 'Exámenes de Contraloria',
                'ordering': ['-fechaingreso'],
            },
        ),
        migrations.CreateModel(
            name='Dependencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True, verbose_name='Dependencia')),
            ],
            options={
                'verbose_name': 'Dependencia',
                'verbose_name_plural': 'Dependencias',
                'ordering': ['nombre'],
                'unique_together': {('nombre',)},
            },
        ),
        migrations.CreateModel(
            name='EntidadExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entidad', models.CharField(max_length=250, verbose_name='Entidad')),
            ],
        ),
        migrations.CreateModel(
            name='oficiosenviados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numoficio', models.PositiveIntegerField()),
                ('institucion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nombre Institución')),
                ('destinatario', models.CharField(blank=True, max_length=500, null=True, verbose_name='Destinatario')),
                ('asunto', models.TextField(blank=True, null=True, verbose_name='Asunto')),
                ('detalle', models.TextField(blank=True, null=True, verbose_name='Detalle')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha Emitido')),
                ('anexos', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Oficios',
                'verbose_name_plural': 'Oficios Enviados',
                'ordering': ['-numoficio'],
            },
        ),
        migrations.CreateModel(
            name='ordenanzas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4, verbose_name='Numero')),
                ('ordenanza', models.TextField(verbose_name='Ordenanza')),
                ('suscrita', models.DateField(verbose_name='Suscrita el')),
                ('primerdebate', models.DateField(null=True, verbose_name='Primer Debate')),
                ('segundodebate', models.DateField(null=True, verbose_name='Segundo Debate')),
                ('sancionada', models.DateField(null=True, verbose_name='Sancionada')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('registro', models.TextField(null=True, verbose_name='Registro Oficial')),
            ],
            options={
                'verbose_name': 'Ordenanza',
                'verbose_name_plural': 'Ordenanzas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='resoluciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolucion', models.CharField(max_length=30, verbose_name='Resolucion Nro')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('detalle', models.TextField(verbose_name='Detalle')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
            ],
            options={
                'verbose_name': 'Resoluciones de Alcaldia',
                'verbose_name_plural': 'Resoluciones',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='rexternos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaingreso', models.DateField(verbose_name='Fecha')),
                ('guianro', models.CharField(max_length=20, verbose_name='Tramite Nro')),
                ('usuario', models.CharField(max_length=200, verbose_name='Usuario')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('oficio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero Oficio')),
                ('fechaentrega', models.DateField(blank=True, null=True, verbose_name='Fecha Entrega')),
                ('enviadoa', models.TextField(blank=True, max_length=350, null=True, verbose_name='Enviado a')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('atendido', models.BooleanField(default=False, verbose_name='Atendido')),
                ('documentos', models.FileField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Tramite',
                'verbose_name_plural': 'Tramites Externos',
                'ordering': ['-fechaingreso'],
            },
        ),
        migrations.CreateModel(
            name='SecretariaG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('tramite', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tramite/Oficio/Memo')),
                ('remite', models.CharField(max_length=250, verbose_name='Remite')),
                ('detalle', models.TextField(default='Ingrese Detalle', verbose_name='Detalle')),
                ('sumilla', models.CharField(max_length=250, verbose_name='Sumilla')),
                ('observacion', models.TextField(verbose_name='Observacion')),
            ],
            options={
                'verbose_name': 'Ingresos Secretaria General',
                'verbose_name_plural': 'Ingresos Secretaria General',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='tramitesdigitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaingreso', models.DateField(verbose_name='Fecha de Ingreso')),
                ('registrado', models.CharField(choices=[('AC', 'Angela Calva'), ('DZ', 'Doda Zhuma'), ('LC', 'Lina Castillo'), ('PV', 'Paulina Villavicencio'), ('ST', 'Stalin Tapia'), ('EU', 'Escoja Usuario')], default='EU', max_length=2, verbose_name='Registrado por')),
                ('identificacion', models.CharField(blank=True, max_length=13, null=True, verbose_name='Identificacion')),
                ('correo', models.EmailField(blank=True, max_length=254, verbose_name='Correo Electrónico')),
                ('usuario', models.CharField(max_length=300, verbose_name='Usuario')),
                ('tramite', models.CharField(choices=[('Con', 'Consulta'), ('CeA', 'Certificado de Avaluos'), ('CLi', 'Certificado de Línea de Fábrica'), ('Cus', 'Certificado de Uso de Suelo'), ('Cvi', 'Certificado de viabilidad'), ('Eav', 'Entrega de Areas Verdes y Márgenes de protección de rios, quebradas y lagunas'), ('Liq', 'Liquidación de la sociedad conyugal y capitulaciones matrimoniales'), ('Pex', 'Particiones Extrajudiciales'), ('Pju', 'Particiones Judiciales'), ('Pom', 'Permiso de obra menor cerramientos, aceras, bordillos, desbanques y muros'), ('Po1', 'Permiso de obra menor contrapiso, pintado de fachadas, cambio de cubierta solo material'), ('Ppl', 'Pre-revisión de planos'), ('Pph', 'Pre-revisión de planos para propiedad horizontal'), ('Psp', 'Pre-revisión de planos para subdivición de predios'), ('Ppu', 'Pre-revisión de planos para urbanización'), ('Sol', 'Solicitudes'), ('Var', 'Varios'), ('Ing', 'Escoja trámite'), ('Inv', 'Invitacion'), ('Apl', 'Aprobación de Planos'), ('Tdo', 'Traspaso de dominio'), ('Dph', 'Declaratoria de propiedad horizontal'), ('Caa', 'Certificado de Areas y Alicuotas'), ('Nli', 'Nueva Linderación'), ('Fap', 'Factibilidad de Agua Potable'), ('Den', 'Denuncias'), ('Apo', 'Acometida Agua Potable'), ('Inf', 'Informar'), ('Aud', 'Solicita Audiencia')], default='Ing', max_length=100, verbose_name='Tramite a realizar')),
                ('ceropapeles', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cero Papeles')),
                ('enviadoa', models.CharField(choices=[('Al', 'Alcaldia'), ('Av', 'Avaluos'), ('Ch', 'Comisaria de Higiene'), ('Cs', 'Comunicación Social'), ('Hi', 'Higiene'), ('Ju', 'Junta de Desarrollo Urbano'), ('Or', 'Ornato'), ('Pl', 'Planificación'), ('Rc', 'Regulación y Control'), ('Um', 'Umapal'), ('Ci', 'Centro Histórico'), ('Ot', 'Otra'), ('Ad', 'Administrativo')], default='Otra', max_length=100, verbose_name='Enviado a')),
                ('estado', models.CharField(choices=[('In', 'Ingresado'), ('Pe', 'Pendiente'), ('Ot', 'Otro')], default='Ingresado', max_length=30, verbose_name='Estado')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
            ],
            options={
                'verbose_name': 'Trámites Digitales',
                'verbose_name_plural': 'Trámites Digitales',
                'ordering': ['-fechaingreso'],
            },
        ),
        migrations.CreateModel(
            name='planificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.PositiveIntegerField(verbose_name='Numero')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('guianro', models.CharField(blank=True, max_length=40, null=True, verbose_name='Tramite Nro')),
                ('categoria', models.CharField(choices=[('1', 'MEMORANDO'), ('2', 'INFORME TECNICO'), ('3', 'TRAMITE EXTERNO'), ('4', 'OFICIO'), ('5', 'COPIA'), ('6', 'S/D'), ('7', 'TRAMITE INTERNO')], default='1', max_length=1, verbose_name='Categoria')),
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
            name='Oficioindice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numoficio', models.CharField(blank=True, max_length=10, null=True, verbose_name='Oficio Nro')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('destinatario', models.CharField(blank=True, max_length=450, null=True, verbose_name='Destinatario')),
                ('dpto', models.CharField(max_length=350, verbose_name='Departamento')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Asunto')),
                ('detalle', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('destino', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='externos.Ciudad')),
                ('origen', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='externos.Dependencias')),
            ],
            options={
                'verbose_name': 'Indice de Oficios',
                'verbose_name_plural': 'Indice de Oficios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MemorandoAlcaldia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummemorando', models.CharField(blank=True, max_length=15, null=True, verbose_name='Memorando')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('dirigidoa', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirigido A')),
                ('asunto', models.CharField(blank=True, max_length=150, null=True, verbose_name='Asunto')),
                ('contenido', models.TextField(blank=True, null=True, verbose_name='Contenido')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('dependencia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='externos.Dependencias')),
            ],
            options={
                'verbose_name': 'Memorandos de Alcaldia',
                'verbose_name_plural': 'Memorandos de Alcaldia',
                'ordering': ['-nummemorando'],
            },
        ),
        migrations.CreateModel(
            name='convenios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.PositiveIntegerField(verbose_name='Numero')),
                ('tipoinstituto', models.CharField(choices=[('1', 'MUNICIPIOS'), ('2', 'GAD PARROQUIALES'), ('3', 'MINISTERIOS'), ('4', 'VARIAS INSTITUCIONES'), ('5', 'CARTAS COMPROMISOS'), ('6', 'ASOCIACIONES, SINDICATOS, BARRIOS'), ('7', 'PRESTAMOS-CREDITOS')], default='1', max_length=1, verbose_name='Tipo Institucion')),
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
                ('contestado', models.CharField(max_length=20, verbose_name='Contestado por Oficio Nro')),
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
