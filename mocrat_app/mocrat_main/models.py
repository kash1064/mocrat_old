from django.db import models
from mocrat_user.models import User

# class Event(models.Model):
#     class Meta:
#         db_table = 'Event'

#     event_name = models.CharField(verbose_name='Event', max_length=255)
#     event_type = models.CharField(verbose_name='EventType', max_length=255)
#     event_author = models.ManyToManyField(User, verbose_name='event_author', related_name='event_author', blank=True)
#     event_member = models.ManyToManyField(User, verbose_name='event_member', related_name='event_member', blank=True)

#     #TODO created_atを、django-readonly-field以外の方法でReadOnlyにする方法があれば実施
#     created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='Updated' ,auto_now=True)

#     def __str__(self):
#         return self.event_name