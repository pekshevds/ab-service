from django.db import models
from server.base import Directory


class Recipient(Directory):
    email = models.EmailField(verbose_name="Почта", unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
