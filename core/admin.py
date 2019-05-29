# Importing admin module from django.contrib directory
from django.contrib import admin 
# Importing all the models one by one from models.py module stored in the same directory 
from core.models import Event, Location, Feedback, Contact, ProblemReport, EventBook, LocationBook

# Register your models here.

# Registering Event model using decorator (decorators are denoted by symbol @)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin): # Customizing default admin web page of the model Event
	list_display = ['event_name', 'added_date', 'updated_date', 'event_added_by'] # customizing the displaying behaviour of different fields in the model admin
	list_filter = ['event_added_by'] # customizing the filter behaviour of different fields in the model admin

# Registering Location model using decorator (decorators are denoted by symbol @)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin): # Customizing default admin web page of the model Event
	list_display = ['location_name', 'location_city', 'added_date', 'updated_date', 'location_added_by'] # customizing the displaying behaviour of different fields in the model admin
	list_filter = ['location_state', 'location_country', 'added_date'] # customizing the filter behaviour of different fields in the model admin


# Registering Feedback model using decorator (decorators are denoted by symbol @)
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin): # Customizing default admin web page of the model Feedback
    list_display = ['email', 'name', 'rating'] # customizing the displaying behaviour of different fields in the model admin


# Registering Contact model using decorator (decorators are denoted by symbol @)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): # Customizing default admin web page of the model Contact
    list_display = ['email', 'name'] # customizing the displaying behaviour of different fields in the model admin


# Registering ProblemReport model using decorator (decorators are denoted by symbol @)
@admin.register(ProblemReport)
class ProblemReportAdmin(admin.ModelAdmin): # Customizing default admin web page of the model ProblemReport
    list_display = ['email', 'name'] # customizing the displaying behaviour of different fields in the model admin


@admin.register(EventBook)
class EventBookAdmin(admin.ModelAdmin):
	list_display = ['event', 'name_of_recipient', 'email_of_recipient', 'message_of_recipient']


@admin.register(LocationBook)
class LocationBookAdmin(admin.ModelAdmin):
	list_display = ['location', 'name_of_recipient', 'email_of_recipient', 'message_of_recipient']