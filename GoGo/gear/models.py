from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"Avatar for {self.user.username}"


class Vuelo(models.Model):
    class Tipo(models.TextChoices):
        DESTINO = 'DES' , 'Destino'
        AEROPUERTO = 'AE', 'Aeropuerto'
        SALA_DE_EMBARQUE = 'EMB', 'Sala de Embarque'
        ESCALA = 'ESC', 'Escala'

    nombre = models.CharField(max_length=40)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)  # Puedes definir un valor predeterminado si lo deseas
    tipo = models.CharField(
        max_length=3,
        choices=Tipo.choices,
        default=Tipo.DESTINO,
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Reserva(models.Model):
    nombre_de_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name="reservas")
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    asientos_reservados = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.vuelo.nombre} - {self.fecha}"
