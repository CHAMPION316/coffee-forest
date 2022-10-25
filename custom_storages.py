"""
Imports and classes to upload
staticfiles to AWS
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ storage for static files to AWS """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ storage for media files to AWS """
    location = settings.MEDIAFILES_LOCATION
