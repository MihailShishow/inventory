"""inv_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from inventory import views
from frontend import views as front_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'counterparties', views.CounterpartyViewSet)
router.register(r'incomewarrants', views.IncomeWarrantViewSet)
router.register(r'outcomewarrants', views.OutcomeWarrantViewSet)
router.register(r'productcategories', views.ProductCategoryViewSet)
router.register(r'incomeinvoices', views.IncomeInvoiceViewSet)
router.register(r'outcomeinvoices', views.OutcomeInvoiceViewSet)
router.register(r'productoutcomes', views.ProductOutcomeViewSet)
router.register(r'productincomes', views.ProductIncomeViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title='Warehouse API',
        default_version='v1',
        description='API для ведения складского и кассового учета.',
        contact=openapi.Contact(email="fanoffm@gmail.com"),
        license=openapi.License(name="GNU General Public License"),

    ),
    url='api/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    re_path(
        r'api/products/(?P<pk>\d+)/circulation/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/', views.ProductCirculationByDateRange.as_view()),
    re_path(
        r'api/counterparties/(?P<pk>\d+)/summary/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/', views.CounterpartySummaryByDateRange.as_view()),
    path('', front_views.TestTemplateView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc')
]
