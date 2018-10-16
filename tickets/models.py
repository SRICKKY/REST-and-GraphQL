from django.db import models

# Create your models here.

class Ticket(models.Model):
	name = models.CharField(max_length=100)
	tickets = models.CharField(max_length=200)
	side_seat = models.CharField(max_length=200)

	def __str__(self):
	    return self.name


class Screen(models.Model):
    name = models.OneToOneField(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
