from common.permissions import IsSubClass
from .mixins import CanWriteMixin

__all__ = ['CanWrite']

CanWrite = IsSubClass(CanWriteMixin)