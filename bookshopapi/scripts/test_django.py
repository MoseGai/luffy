
#测试settings

import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookshopapi.settings.dev")
django.setup()


from django.conf import  settings
print(settings)
