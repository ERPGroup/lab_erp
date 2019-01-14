SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cart-tests.db',
    }
}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.sites',
    'cart',
    'cart.tests',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'cart.tests.urls'

SECRET_KEY = 'any-key'

CART_PRODUCT_MODEL = 'cart.tests.models.Product'
