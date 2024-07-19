from django.contrib import admin
from cart_app.models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
