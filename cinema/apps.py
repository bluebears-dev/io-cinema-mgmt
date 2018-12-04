from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CinemaConfig(AppConfig):
    name = 'cinema'
    verbose_name = _('Sieć kin KAPPA')
