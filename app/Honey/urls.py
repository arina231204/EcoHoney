from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from django.conf.urls.static import static
from Honey import settings

from products.views import *
from orders.views import *


products_router = DefaultRouter()
products_router.register('products', ItemViewSet)
products_router.register('feedbacks', FeedbackViewSet)
products_router.register('order', OrderCreateViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Honey API",
      default_version='v-0.01',
      description="API для взаимодействия с Honey API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="myrza.bakytbekovich@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/', include(products_router.urls)),
    path('cart/', include('cart.urls')),
    path('order_paid/<int:order_id>/', order_paid, name="order_paid"),
    path('order_delivery/<int:order_id>/', order_delivery, name="order_delivery"),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),


]


#
# urlpatterns = [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
