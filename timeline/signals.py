from django.dispatch import Signal

timeline_changed = Signal(providing_args = ['year'])