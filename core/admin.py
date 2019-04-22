from django.contrib import admin
from core.models import Event, Location, Feedback, Contact, ProblemReport, EventBook, LocationBook

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'added_date', 'updated_date', 'event_added_by']
	list_filter = ['event_added_by']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ['location_name', 'location_city', 'added_date', 'updated_date', 'location_added_by']
	list_filter = ['location_state', 'location_country', 'added_date']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'rating']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(ProblemReport)
class ProblemReportAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(EventBook)
class EventBookAdmin(admin.ModelAdmin):
	list_display = ['event', 'name_of_recipient', 'email_of_recipient', 'message_of_recipient']


@admin.register(LocationBook)
class LocationBookAdmin(admin.ModelAdmin):
	list_display = ['location', 'name_of_recipient', 'email_of_recipient', 'message_of_recipient']