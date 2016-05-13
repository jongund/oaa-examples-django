# OAA Accessibility

### Creating a <code>secrets.json</code> file

The "secretes.json" file must be created and provides:
* Security information for Django
* Information for Django to access and manage the database
* Information on on e-mail commmunications for registration and announcements.
* Place this file in the <code><em>[absolute path]</em>/oaa_examples_django</code> directory

```
{
    "FILENAME": "secrets.json",
    "SITE_URL": ["<Your SITE_URL>"],
    "SITE_NAME": "OAA Accessbility x.x",
    "SECRET_KEY": "",
    "DEBUG": false,
    "ALLOWED_HOSTS": ["<Your SITE_URL>"],
    "STATIC_URL": "<Your STATIC_URL>", 
    "STATIC_DIR": "",
    "DATABASES": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "<Your DATABASES NAME>",
        "USER": "<Your DATABASES USER>",
        "PASSWORD": "<Your DATABASES PASSWORD>"
    }
}
```