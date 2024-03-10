from django.contrib import admin
from .models import Text
from .models import News
from .models import Workers
from .models import Events
from .models import Refences

admin.site.register(Text)
admin.site.register(News)
admin.site.register(Workers)
admin.site.register(Events)
admin.site.register(Refences)

