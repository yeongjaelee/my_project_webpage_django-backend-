from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # url(r'^graphql', FileUploadGraphQLView.as_view(graphiql=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
