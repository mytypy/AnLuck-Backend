from django.utils.timesince import timesince
from django.utils import timezone


def normal_time(time):
    diff = timesince(time, timezone.now())
    return f'{diff} назад'