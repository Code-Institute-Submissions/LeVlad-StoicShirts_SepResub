from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "custom_name",
        "quotes",
    )


admin.site.register(Quote, QuoteAdmin)
