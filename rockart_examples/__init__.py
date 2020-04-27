import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("rockart-examples").version
except pkg_resources.DistributionNotFound:
    pass
