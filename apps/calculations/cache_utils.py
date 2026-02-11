from django.core.cache import cache

def cache_calculation_result(key, result, timeout=3600):
    cache.set(key, result, timeout)

def get_cached_calculation_result(key):
    return cache.get(key)
