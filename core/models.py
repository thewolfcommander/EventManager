from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	"""
	This model is going to be converted into a table that will store the information of all the events and their information that are available in the database
	"""
	event_name = models.CharField(max_length=255, blank=True, unique=True, null=True, help_text="This is event name that should be unique.")
	event_description = models.CharField(max_length=1255, blank=True, null=True, help_text="This is event description.")
	event_image = models.ImageField(upload_to="event_image", help_text="This is event image.")
	added_date = models.DateTimeField(auto_now_add=True, help_text="This is the date and time at which the event is first added to the database.")
	updated_date = models.DateTimeField(auto_now=True, help_text="This is the time and date, the event is last updated")
	event_added_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="This is the person who have added the event to the database")

	def __str__(self):
		return self.event_name

class Location(models.Model):
	"""
	This model is going to be converted into a table that will store the information of all the locations that are going to be scheduled to organize an event.
	"""
	location_name = models.CharField(max_length=255, blank=True, unique=True, null=True, help_text="This is location name that should be unique.")
	location_city = models.CharField(max_length=255, blank=True, null=True, help_text="This is location city.")
	location_state = models.CharField(max_length=255, blank=True, null=True, help_text="This is location state.")
	location_country = models.CharField(max_length=255, blank=True, null=True, help_text="This is location country.")
	location_pin_code = models.CharField(max_length=20, blank=True, null=True, help_text="This is pin code of the location.")
	location_image = models.ImageField(upload_to="location_image", help_text="This is location image")
	added_date = models.DateTimeField(auto_now_add=True, help_text="This is the date and time at which the location is first added to the database.")
	updated_date = models.DateTimeField(auto_now=True, help_text="This is the time and date, the location is last updated")
	location_added_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="This is the person who have added the location to the database")

	def __str__(self):
		return self.location_name



class Feedback(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient Email")
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient name")
    message = models.CharField(max_length=255, blank=True, null=True, help_text="Message")
    rating = models.IntegerField(blank=True, null=True, help_text="Rating (from scale -100 to 100)")

    def __str__(self):
        return self.email


class Contact(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient Email")
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient name")
    message = models.CharField(max_length=255, blank=True, null=True, help_text="Message")
    
    def __str__(self):
        return self.email

class ProblemReport(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient Email")
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Recipient name")
    message = models.CharField(max_length=255, blank=True, null=True, help_text="Message")
    problem_screenshot = models.ImageField(upload_to="problem_insystem_images", blank=True, null=True, help_text="Problem screenshot")

    def __str__(self):
        return self.email

class EventBook(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, help_text="This is the event information from the database")
	location = models.ForeignKey(Location, on_delete=models.CASCADE, help_text="This is the location information from the database")
	name_of_recipient = models.CharField(max_length=255, blank=True, help_text="This is the reciepient's name who want to book the event.")
	email_of_recipient = models.CharField(max_length=255, blank=True, help_text="This is the reciepient's email who want to book the event.")
	message_of_recipient = models.CharField(max_length=1500, blank=True, help_text="This is the message of recipient that wants to ")