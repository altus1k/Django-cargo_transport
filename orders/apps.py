from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        import orders.signals

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals