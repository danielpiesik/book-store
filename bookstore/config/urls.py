from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('auth/', include('rest_auth.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls')),

    path('', include('authors.urls')),
    path('', include('books.urls')),
    path('', include('orders.urls')),
    path('', include('users.urls')),
]

swagger_view = get_swagger_view(
    title='Bookstore API',
    patterns=urlpatterns,
)

urlpatterns = urlpatterns + [
    path('documentation/', swagger_view),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
