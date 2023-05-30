from django.db import models


class Incidents(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class VideoData(models.Model):
    filename = models.TextField()
    date_processed = models.DateTimeField()
    objects_detected = models.IntegerField()
    processing_time = models.FloatField()

    def __str__(self):
        return self.filename
