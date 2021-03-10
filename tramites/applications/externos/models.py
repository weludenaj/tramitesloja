from django.db import models

# Create your models here.
from .managers import ExternoManager

#from ckeditor.fields import RichTextField

# Create your models here.


class rexternos(models.Model):
    fechaingreso = models.DateField(
        null=False, blank=False, verbose_name="Fecha")
    guianro = models.CharField(
        max_length=20, verbose_name="Tramite Nro", null=False, blank=False, unique=False)
    usuario = models.CharField(
        max_length=200, verbose_name="Usuario", null=False, blank=False)
    descripcion = models.TextField(
        max_length=500, verbose_name="Descripcion", null=False, blank=False)
    oficio = models.CharField(
        max_length=50, verbose_name="Numero Oficio", null=True, blank=True)
    fechaentrega = models.DateField(
        null=True, blank=True, verbose_name="Fecha Entrega")
    enviadoa = models.TextField(
        null=True, blank=True, max_length=350, verbose_name="Enviado a")
    observacion = models.TextField(
        null=True, blank=True, verbose_name="Observacion")
    atendido = models.BooleanField('Atendido', default=False)
    documentos = models.FileField(upload_to='media', blank=True, null=True)

    objects = ExternoManager()

    class Meta:
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites Externos'
        ordering = ['-fechaingreso']
      ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Fecha %s Guia %s Usuario %s Descripcion %s Oficio %s Entregado %s Enviado a %s Observacion %s Atendido %s' % (self.fechaingreso, self.guianro, self.usuario, self.descripcion, self.oficio, self.fechaingreso, self.enviadoa, self.observacion, self.atendido)


class Administrador(models.Model):
    numerocontrato = models.CharField(
        verbose_name="Contrato Nro", max_length=50, null=True, blank=True)
    administrador = models.CharField(
        verbose_name="Administrador", max_length=250, default="No asignado")
    nombredelcontrato = models.TextField(verbose_name="Nombre del Contrato")
    contratista = models.TextField(
        verbose_name="Contratista", null=True, blank=True)
    fechainicio = models.DateField(
        verbose_name="Fecha de Inicio", null=True, blank=True)
    fechafinal = models.DateField(
        verbose_name="Fecha de Finalización", null=True, blank=True)
    memosend = models.TextField(
        verbose_name="Memos Enviados", null=True, blank=True)
    memoreceived = models.TextField(
        verbose_name="Memos Recibidos", null=True, blank=True)

    class Meta:
        verbose_name = 'Administrador de Contratos'
        verbose_name_plural = 'Administrador de Contratos'
        ordering = ['administrador']

    def __str__(self):
        return 'Administrador %s Contrato Nro %s Contrato %s Contratista %s Fecha Inicial %s FechaFinal %s Memo Enviado %s Memo Recibido %s' % (
            self.administrador, self.numerocontrato, self.nombredelcontrato, self.contratista, self.fechainicio, self.fechafinal, self.memosend, self.memoreceived)


class contraloria(models.Model):
    secuencia = models.PositiveIntegerField(default=0)
    fechaingreso = models.DateField(
        null=False, blank=False, verbose_name="Fecha")
    memorando = models.CharField(
        max_length=40, verbose_name="Nro Memo/Oficio", null=True, blank=True)
    recomendacion = models.TextField(
        null=False, blank=False, verbose_name="Recomendación")
    dependencia = models.CharField(max_length=50, verbose_name="Dirigido a ")
    funcionario = models.TextField(
        null=False, blank=False, verbose_name="Funcionario")
    contestacion = models.TextField(
        verbose_name="Remitente", null=True, blank=True)
    seguimiento = models.TextField(
        verbose_name="Seguimiento realizado", null=True, blank=True)
    fechalastupdate = models.DateField(null=True, blank=True)
    #dependencias = models.ManyToManyField(Dependencia)
    observacion = models.TextField(
        verbose_name="Observacion", null=True, blank=True)
    concluido = models.BooleanField('Atendido', default=False)
    documentos = models.FileField(upload_to='media', blank=True, null=True)

    class Meta:
        verbose_name = 'Exámenes de contraloria'
        verbose_name_plural = 'Exámenes de Contraloria'
        ordering = ['-fechaingreso']
      ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Secuencia %s Fecha %s Memorando %s Recomendacion %s Dependencias %s Funcionario %s Contestacion %s Seguimiento %s Observacion %s Concluido %s Documentos %s' % (self.secuencia, self.fechaingreso, self.memorando, self.recomendacion, self.dependencia, self.funcionario, self.contestacion, self.seguimiento, self.observacion, self.concluido, self.documentos)


class oficiosenviados(models.Model):
    numoficio = models.PositiveIntegerField()
    institucion = models.CharField(
        verbose_name="Nombre Institución", max_length=500, blank=True, null=True)
    destinatario = models.CharField(
        verbose_name="Destinatario", max_length=500, blank=True, null=True)
    asunto = models.TextField(verbose_name="Asunto", blank=True, null=True)
    detalle = models.TextField(verbose_name="Detalle", blank=True, null=True)
    fecha = models.DateField(
        verbose_name="Fecha Emitido", null=True, blank=True)
    anexos = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Oficios'
        verbose_name_plural = 'Oficios Enviados'
        ordering = ['-numoficio']

    def __str__(self):
        return 'Oficio %s Institución %s Destinatario %s Asunto %s Detalle %s Fecha %s Anexo %s' % (
            self.numoficio, self.institucion, self.destinatario, self.asunto, self.detalle, self.fecha, self.anexos)


class tramitesdigitales(models.Model):

    registrados = [
        ('AC', 'Angela Calva'),
        ('DZ', 'Doda Zhuma'),
        ('LC', 'Lina Castillo'),
        ('PV', 'Paulina Villavicencio'),
        ('ST', 'Stalin Tapia'),
        ('EU', 'Escoja Usuario'),
    ]

    dependencias = [
        ('Al', 'Alcaldia'),
        ('Av', 'Avaluos'),
        ('Ch', 'Comisaria de Higiene'),
        ('Cs', 'Comunicación Social'),
        ('Hi', 'Higiene'),
        ('Ju', 'Junta de Desarrollo Urbano'),
        ('Or', 'Ornato'),
        ('Pl', 'Planificación'),
        ('Rc', 'Regulación y Control'),
        ('Um', 'Umapal'),
        ('Ci', 'Centro Histórico'),
        ('Ot', 'Otra'),
        ('Ad', 'Administrativo'),

    ]

    estados = [
        ('In', 'Ingresado'),
        ('Pe', 'Pendiente'),
        ('Ot', 'Otro')
    ]

    tramites = [
        ('Con', 'Consulta'),
        ('CeA', 'Certificado de Avaluos'),
        ('CLi', 'Certificado de Línea de Fábrica'),
        ('Cus', 'Certificado de Uso de Suelo'),
        ('Cvi', 'Certificado de viabilidad'),
        ('Eav', 'Entrega de Areas Verdes y Márgenes de protección de rios, quebradas y lagunas'),
        ('Liq', 'Liquidación de la sociedad conyugal y capitulaciones matrimoniales'),
        ('Pex', 'Particiones Extrajudiciales'),
        ('Pju', 'Particiones Judiciales'),
        ('Pom', 'Permiso de obra menor cerramientos, aceras, bordillos, desbanques y muros'),
        ('Po1', 'Permiso de obra menor contrapiso, pintado de fachadas, cambio de cubierta solo material'),
        ('Ppl', 'Pre-revisión de planos'),
        ('Pph', 'Pre-revisión de planos para propiedad horizontal'),
        ('Psp', 'Pre-revisión de planos para subdivición de predios'),
        ('Ppu', 'Pre-revisión de planos para urbanización'),
        ('Sol', 'Solicitudes'),
        ('Var', 'Varios'),
        ('Ing', 'Escoja trámite'),
        ('Inv', 'Invitacion'),
        ('Apl', 'Aprobación de Planos'),
        ('Tdo', 'Traspaso de dominio'),
        ('Dph', 'Declaratoria de propiedad horizontal'),
        ('Caa', 'Certificado de Areas y Alicuotas'),
        ('Nli', 'Nueva Linderación'),
        ('Fap', 'Factibilidad de Agua Potable'),
        ('Den', 'Denuncias'),
        ('Apo', 'Acometida Agua Potable'),
        ('Inf', 'Informar'),
        ('Aud', 'Solicita Audiencia')

    ]

    fechaingreso = models.DateField(verbose_name="Fecha de Ingreso")
    registrado = models.CharField(
        verbose_name="Registrado por",
        max_length=2,
        choices=registrados,
        default='EU',
    )

    identificacion = models.CharField(
        verbose_name="Identificacion", max_length=13, blank=True, null=True)
    correo = models.EmailField(verbose_name="Correo Electrónico", blank=True)
    usuario = models.CharField(verbose_name="Usuario", max_length=300)
    tramite = models.CharField(
        verbose_name="Tramite a realizar",
        max_length=100,
        choices=tramites,
        default='Ing'

    )
    ceropapeles = models.CharField(
        verbose_name="Cero Papeles", max_length=20, blank=True, null=True)
    enviadoa = models.CharField(
        verbose_name="Enviado a",
        max_length=100,
        choices=dependencias,
        default='Otra'
    )
    estado = models.CharField(
        verbose_name="Estado",
        max_length=30,
        choices=estados,
        default='Ingresado'
    )
    observacion = models.TextField(
        verbose_name="Observacion", blank=True, null=True)

    class Meta:
        verbose_name = 'Trámites Digitales'
        verbose_name_plural = 'Trámites Digitales'
        ordering = ['-fechaingreso']

    def __str__(self):
        return 'Ingreso %s Registrado %s Identificacion %s Correo %s Usuario %s Tramite %s Cero Papeles %s Enviado a %s Estado %s' % (
            self.fechaingreso, self.registrado, self.identificacion, self.correo, self.usuario, self.tramite, self.ceropapeles, self.enviadoa, self.estado)


class Ciudad(models.Model):
    nombre = models.CharField(verbose_name="Ciudad", max_length=50)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Dependencias(models.Model):
    nombre = models.CharField(
        verbose_name="Dependencia", max_length=250, unique=True)

    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
        ordering = ['nombre']
        unique_together = ('nombre',)

    def __str__(self):
        return self.nombre


class Oficioindice(models.Model):
    numoficio = models.CharField(
        verbose_name="Oficio Nro", null=True, blank=True, max_length=10)
    fecha = models.DateField(
        verbose_name="Fecha", null=True, blank=True, auto_now=False, auto_now_add=False)
    origen = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, default=1)
    destinatario = models.CharField(
        verbose_name="Destinatario", max_length=450, null=True, blank=True)
    dpto = models.CharField(verbose_name="Departamento",  max_length=350)
    destino = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default=1)
    observacion = models.TextField(
        verbose_name="Asunto", null=True, blank=True)
    detalle = models.TextField(
        verbose_name="Observaciones", null=True, blank=True)

    class Meta:
        verbose_name = 'Indice de Oficios'
        verbose_name_plural = 'Indice de Oficios'
        ordering = ['-id']

    def __str__(self):
        return 'Oficio Nro %s Fecha %s Origen %s Destinatario %s Departamento %s Destino %s Asunto %s Observaciones %s' % (
            self.numoficio, self.fecha, self.origen, self.destinatario, self.dpto, self.destino, self.observacion, self.detalle)


class SecretariaG(models.Model):
    fecha = models.DateField(verbose_name="Fecha",
                             auto_now=False, auto_now_add=False)
    tramite = models.CharField(
        verbose_name="Tramite/Oficio/Memo", max_length=30, blank=True, null=True)
    remite = models.CharField(verbose_name="Remite", max_length=250)
    detalle = models.TextField(
        verbose_name="Detalle", default="Ingrese Detalle")
    sumilla = models.CharField(verbose_name="Sumilla", max_length=250)
    observacion = models.TextField(verbose_name="Observacion")

    class Meta:
        verbose_name = 'Ingresos Secretaria General'
        verbose_name_plural = 'Ingresos Secretaria General'
        ordering = ['-fecha']

    def __str__(self):
        return 'Fecha %s Tramite %s Remite %s Detalle %s Sumilla %s Observaciones %s' % (
            self.fecha, self.tramite, self.remite, self.detalle, self.sumilla, self.observacion)


class MemorandoAlcaldia(models.Model):
    nummemorando = models.CharField(
        verbose_name="Memorando", null=True, blank=True, max_length=15)
    fecha = models.DateField(
        verbose_name="Fecha", null=True, blank=True, auto_now=False, auto_now_add=False)
    dirigidoa = models.CharField(
        verbose_name="Dirigido A", max_length=250, blank=True, null=True)
    dependencia = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, default=1)
    asunto = models.CharField(verbose_name="Asunto",
                              max_length=150, blank=True, null=True)
    contenido = models.TextField(
        verbose_name="Contenido", null=True, blank=True)
    observacion = models.TextField(
        verbose_name="Observacion", blank=True, null=True)

    class Meta:
        verbose_name = 'Memorandos de Alcaldia'
        verbose_name_plural = 'Memorandos de Alcaldia'
        ordering = ['-nummemorando']

    def __str__(self):
        return 'Memorando %s Fecha %s Dirigido %s Dependencia %s Asunto %s Contenido %s Observaciones %s' % (
            self.nummemorando, self.fecha, self.dirigidoa, self.dependencia, self.asunto, self.contenido, self.observacion)


class resoluciones(models.Model):
    resolucion = models.CharField(verbose_name="Resolucion Nro", max_length=30)
    fecha = models.DateField(verbose_name="Fecha",
                             auto_now=False, auto_now_add=False)
    detalle = models.TextField(verbose_name="Detalle")
    observacion = models.TextField(
        verbose_name="Observacion", null=True, blank=True)

    class Meta:
        verbose_name = 'Resoluciones de Alcaldia'
        verbose_name_plural = "Resoluciones"
        ordering = ['-id']

    def __str__(self):
        return 'Resolucion Nro %s Fecha %s Detalle %s Observacion %s' % (
            self.resolucion, self.fecha, self.detalle, self.observacion)


class ordenanzas(models.Model):
    numero = models.CharField(verbose_name="Numero", max_length=4)
    ordenanza = models.TextField(verbose_name="Ordenanza")
    suscrita = models.DateField(
        verbose_name="Suscrita el", auto_now=False, auto_now_add=False)
    primerdebate = models.DateField(
        verbose_name="Primer Debate", auto_now=False, auto_now_add=False, null=True)
    segundodebate = models.DateField(
        verbose_name="Segundo Debate", auto_now=False, auto_now_add=False, null=True)
    sancionada = models.DateField(
        verbose_name="Sancionada", auto_now=False, auto_now_add=False, null=True)
    observacion = models.TextField(
        verbose_name="Observaciones", null=True, blank=True)
    registro = models.TextField(verbose_name="Registro Oficial", null=True)

    class Meta:
        verbose_name = 'Ordenanza'
        verbose_name_plural = "Ordenanzas"
        ordering = ['-id']

    def __str__(self):
        return 'Nro %s Ordenanza %s Suscrita %s Primer Debate %s Segundo Debate %s Sancionada %s Observaciones %s Registro Oficial %s' % (
            self.numero, self.ordenanza, self.suscrita, self.primerdebate, self.segundodebate, self.sancionada, self.observacion, self.registro)


class EntidadExterna(models.Model):
    Entidad = models.CharField(verbose_name="Entidad", max_length=250)

    def __str__(self):
        return (self.Entidad)


class Comunicaciones(models.Model):
    medio = [
        ('1', 'Quipux'),
        ('2', 'Correo'),
        ('3', 'Otro'),
    ]
    numero = models.CharField(verbose_name="Numero", max_length=4)
    fecha = models.DateField(verbose_name="Fecha",
                             auto_now=False, auto_now_add=False)
    medios = models.CharField(
        verbose_name="Medio",
        max_length=1,
        choices=medio,
        default='1'
    )
    entidad = models.ForeignKey(
        EntidadExterna, on_delete=models.CASCADE, default=1)
    remite = models.CharField(verbose_name="Remitente", max_length=350)
    asunto = models.CharField(verbose_name="Asunto", max_length=350)
    contestado = models.CharField(
        verbose_name="Contestado por Oficio Nro", max_length=20)
    observacion = models.TextField(verbose_name="Observacion")

    class Meta:
        verbose_name = 'Comunicaciones'
        verbose_name_plural = "Comunicaciones"
        ordering = ['-fecha']

    def __str__(self):
        return 'Nro %s Fecha %s Medio %s Entidad %s Remitente %s Asunto %s Contestado %s Observacion %s' % (
            self.numero, self.fecha, self.medio, self.entidad, self.remite, self.asunto, self.contestado, self.observacion)


class planificacion(models.Model):
    tipocategoria = [
        ("1", "MEMORANDO"),
        ("2", "INFORME TECNICO"),
        ("3", "TRAMITE EXTERNO"),
        ("4", "OFICIO"),
        ("5", "COPIA"),
        ("6", "S/D"),
        ("7", "TRAMITE INTERNO"),
    ]
    registro = models.PositiveIntegerField(verbose_name="Numero")
    fecha = models.DateField(null=False, blank=False, verbose_name="Fecha")
    guianro = models.CharField(
        max_length=40, verbose_name="Tramite Nro", null=True, blank=True)
    categoria = models.CharField(
        verbose_name="Categoria",
        max_length=1,
        choices=tipocategoria,
        default='1'
    )
    referencia = models.CharField(
        max_length=200, verbose_name="Referencia", null=False, blank=False)
    asunto = models.TextField(
        max_length=500, verbose_name="Asunto", null=False, blank=False)
    remitente = models.CharField(
        max_length=250, verbose_name="Remitente", null=True, blank=True)
    departamento = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, default=1, related_name='Origen')
    destinatario = models.CharField(
        verbose_name="Destinatario", max_length=250)
    departamentof = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, default=1, related_name='Destino')
    observacion = models.TextField(
        null=True, blank=True, verbose_name="Observacion")
    atendido = models.BooleanField('Atendido', default=False)

    class Meta:
        verbose_name = 'Planificacion'
        verbose_name_plural = 'Planificacion'
        ordering = ['-fecha']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Registro %s Fecha %s Guia %s Categoria %s Referencia %s Asunto %s Remitente %s Origen  %s Destinatario %s Destino %s Observacion %s Atendido %s' % (self.registro, self.fecha, self.guianro, self.categoria, self.referencia, self.asunto, self.remitente, self.departamento, self.destinatario, self.departamentof, self.observacion, self.atendido)


class convenios(models.Model):
    tipoinstitucion = [
        ("1", "MUNICIPIOS"),
        ("2", "GAD PARROQUIALES"),
        ("3", "MINISTERIOS"),
        ("4", "VARIAS INSTITUCIONES"),
        ("5", "CARTAS COMPROMISOS"),
        ("6", "ASOCIACIONES, SINDICATOS, BARRIOS"),
        ("7", "PRESTAMOS-CREDITOS")
    ]
    cumplimientos = [
        ("1", "EN EJECUCION"),
        ("2", "POR FINALIZAR"),
        ("3", "FINALIZADO"),
        ("4", "RETRASADO")
    ]
    registro = models.PositiveIntegerField(verbose_name="Numero")
    tipoinstituto = models.CharField(
        verbose_name="Tipo Institucion",
        choices=tipoinstitucion,
        default="1",
        max_length=1
    )
    institucion = models.CharField(verbose_name="Institucion", max_length=350)
    convenio = models.CharField(verbose_name="Convenio", max_length=450)
    objeto = models.TextField(verbose_name="Objeto")
    plazo = models.PositiveIntegerField(verbose_name="Plazo")
    fechainicio = models.DateField(
        null=False, blank=False, verbose_name="Fecha Inicio")
    fechafinal = models.DateField(
        null=False, blank=False, verbose_name="Fecha Final")
    cumplimiento = models.CharField(
        verbose_name="Cumplimiento",
        max_length=1,
        choices=cumplimientos,
        default="1"
    )
    encargado = models.CharField(
        max_length=520, verbose_name="Encargado", null=False, blank=False, unique=False)
    dependencia = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, default=1)
    observacion = models.TextField(
        null=True, blank=True, verbose_name="Observacion")

    class Meta:
        verbose_name = 'Convenios'
        verbose_name_plural = 'Convenios'
        ordering = ['-fechainicio']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Registro %s Institucion %s Convenio %s Objeto %s Plazo %s Fecha Inicial %s Fecha Final %s Cumplimiento  %s Encargado %s Dependencia %s Observacion %s' % (self.registro, self.institucion, self.convenio, self.objeto, self.plazo, self.fechainicio, self.fechafinal, self.cumplimiento, self.encargado, self.dependencia, self.observacion)
