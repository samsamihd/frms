from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "frms.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import frms.users.signals  # noqa F401
        except ImportError:
            pass
