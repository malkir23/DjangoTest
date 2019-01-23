from django.db import models

progres = (
        ('to do','to do'),
        ('in progress', 'in progress'),
        ('done','done'),
    )

class Board(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name Works')
    text = models.TextField()
    category = models.CharField(max_length=15, choices=progres, default='to do')

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

    def __str__(self):
        return "{} -- {}".format(self.name, self.category)