"""
Production settings for AWS deployment.
Uses environment variables — set these in AWS Elastic Beanstalk or EC2.
"""
from .settings import *
import os
from decouple import config

# ── Security ──────────────────────────────────────────────────────────────────
DEBUG = False
SECRET_KEY = config('SECRET_KEY', default='change-me-in-production')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# ── Database (AWS RDS PostgreSQL) ─────────────────────────────────────────────
# Option 1: Use PostgreSQL on AWS RDS (recommended for production)
# Uncomment when you have an RDS instance:
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME', default='lmt_db'),
#         'USER': config('DB_USER', default='postgres'),
#         'PASSWORD': config('DB_PASSWORD', default=''),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }

# Option 2: Keep SQLite for simple deployment (fine for small apps)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ── Static & Media Files (AWS S3) ─────────────────────────────────────────────
# Option 1: Use AWS S3 for media files (recommended)
# Uncomment when you have S3 bucket:
#
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
# AWS_STORAGE_BUCKET_NAME = config('AWS_S3_BUCKET', default='lmt-media')
# AWS_S3_REGION_NAME = config('AWS_S3_REGION', default='ap-south-1')
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

# Option 2: Serve from local disk (simpler, fine for EC2)
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# ── Static Files with WhiteNoise ──────────────────────────────────────────────
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE[2:]  # skip duplicate SecurityMiddleware

# ── CORS ──────────────────────────────────────────────────────────────────────
CORS_ALLOW_ALL_ORIGINS = True  # Restrict in prod: CORS_ALLOWED_ORIGINS = ['https://yourapp.com']

# ── Razorpay ──────────────────────────────────────────────────────────────────
RAZORPAY_KEY_ID = config('RAZORPAY_KEY_ID', default='rzp_test_e664V0FP0zQy7N')
RAZORPAY_KEY_SECRET = config('RAZORPAY_KEY_SECRET', default='QdnuRxUHrPGeiJc9lDTXYPO7')
