from threading import Thread

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CinemaConfig(AppConfig):
    name = 'cinema'
    verbose_name = _('Sieć kin KAPPA')

    def ready(self):
        from .views.booking import worker
        task = Thread(target=worker)

        # task.start()
