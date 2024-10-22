from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    #POR_HACER = 'POR_HACER'
    #EN_PROGRESO = 'EN_PROGRESO'
    #COMPLETADA = 'COMPLETADA'
    
    ESTADOS_TAREA = [
        ('POR_HACER', 'Por hacer'),
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADA', 'Completada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    criterios_aceptacion = models.TextField(blank=True, null=True)
    prioridad = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS_TAREA, default='POR_HACER')
    esfuerzo_estimado = models.IntegerField(default=0)
    responsable = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    sprint_asignado = models.ForeignKey('Sprint', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    dependencias = models.ManyToManyField('self', blank=True, symmetrical=False)
    bloqueadores = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(prioridad__gte=0), name='prioridad_no_negativa'),
            models.CheckConstraint(check=models.Q(esfuerzo_estimado__gte=0), name='esfuerzo_estimado_no_negativo'),
            models.CheckConstraint(check=models.Q(estado__in=['POR_HACER', 'EN_PROGRESO', 'COMPLETADA']), name='estado_valido_tarea'),
        ]

class Epica(models.Model):
    
    ESTADOS_EPICA = [
        ('POR_HACER', 'Por hacer'),
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADA', 'Completada'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    criterios_aceptacion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_EPICA, default='POR_HACER')
    responsable = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tareas_asociadas = models.ManyToManyField(Tarea, blank=True)
    esfuerzo_estimado_total = models.IntegerField(default=0)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    progreso = models.FloatField(default=0.0)
    dependencias = models.ManyToManyField('self', blank=True, symmetrical=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(esfuerzo_estimado_total__gte=0), name='esfuerzo_total_no_negativo'),
            models.CheckConstraint(check=models.Q(progreso__gte=0, progreso__lte=1), name='progreso_valido'),
            models.CheckConstraint(check=models.Q(fecha_fin__gte=models.F('fecha_inicio')), name='fecha_fin_posterior_epica'),
            models.CheckConstraint(check=models.Q(estado__in=['POR_HACER', 'EN_PROGRESO', 'COMPLETADA']), name='estado_valido_epica'),
        ]

class Sprint(models.Model):
    nombre = models.CharField(max_length=200)
    objetivo = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    velocidad = models.IntegerField(default=0)
    scrum_master = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    equipo_desarrollo = models.ManyToManyField(User, related_name='equipo_desarrollo', blank=True)
    backlog_sprint = models.ManyToManyField(Tarea, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(fecha_fin__gte=models.F('fecha_inicio')), name='fecha_fin_posterior'),
            models.CheckConstraint(check=models.Q(velocidad__gte=0), name='velocidad_no_negativa'),
        ]
