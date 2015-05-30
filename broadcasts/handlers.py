from django.dispatch import receiver
from django.db.models.signals import pre_save

from broadcasts.models import Slide
 
@receiver(pre_save, sender=Slide)
def slide_save_handler(sender, instance, *args, **kwargs):
    if instance and instance.position == -1:
        instance.position = Slide.objects.filter(broadcasting=instance.broadcasting).count()