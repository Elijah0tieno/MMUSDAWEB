from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_ovewrite = False
    
class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'static'
    
class PrivateMediaStorage(S3Boto3Storage):
    location = 'private-read'
    default_acl = 'private'
    file_ovewrite = False
    custom_domain = False
    
class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_ovewrite = False