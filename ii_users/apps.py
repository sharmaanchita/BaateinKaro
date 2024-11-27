from django.apps import AppConfig


class IiUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ii_users"
    
    def ready(self):
        import ii_users.signals