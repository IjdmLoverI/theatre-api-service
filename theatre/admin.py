from django.contrib import admin

from theatre.models import (
    TheatreHall,
    Ticket,
    Actor,
    Reservation,
    Genre,
    Play,
    Performance
)


admin.site.register(TheatreHall)
admin.site.register(Ticket)
admin.site.register(Actor)
admin.site.register(Reservation)
admin.site.register(Genre)
admin.site.register(Play)
admin.site.register(Performance)
