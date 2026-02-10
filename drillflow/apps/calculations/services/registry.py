CALCULATION_REGISTRY = {}


def register(service):
    CALCULATION_REGISTRY[service.name] = service


def get(name):
    return CALCULATION_REGISTRY.get(name)


# register default services
from .rheology import RheologyService
register(RheologyService())
