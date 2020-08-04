from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index,
    search,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    IndexView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from marketing.views import email_list_signup
from rankings.views import player_list
from autoridades.views import autoridad_list
from clubes.views import ClubListView
from torneos.views import TorneoListView
from contacto.views import ContactoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('rankings/', player_list, name='player-list'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('autoridades/', autoridad_list, name='autoridad-list'),
    path('clubes-asociados/', ClubListView.as_view(), name='club-list'),
    path('calendario/', TorneoListView.as_view(), name='torneo-list'),
    path('contacto/', ContactoListView.as_view(), name='titulado-list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
     urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administración F.M.A."
admin.site.site_title = "Administración F.M.A."
admin.site.index_title = "Bienvenidos a la Administración de la F.M.A."
