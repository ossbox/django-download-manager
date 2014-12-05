Download Manager - by request
==========================================


The idea is request a download filling a form. It will trigger a request
to download. It will be sent by email with a link to reject and another to accept.

If the admin accepts, the user will be able to download, otherwise no.





Requirements
-----------------

* Developed to Django 1.7.1

Please add it in local_settings.py (you have to create it, in the same folder of settings):

```
# -*- coding: utf-8 -*-


EMAIL_HOST = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = 'youremail'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "yourmeial@email.com"


ADMINS = (('Luís Bastião', 'yourock@email.com'), )
BASE_URL = "http://localhost:8000/"


PROJECT_NAME = "Your project name"

DOWNLOAD_FOLDER = "/dir/with/your/private/files"

```



Author
-----------------
Luís A. Bastião Silva
