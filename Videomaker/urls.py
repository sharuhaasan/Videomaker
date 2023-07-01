"""
URL configuration for Videomaker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Audio_Elements.views import AudioElementListCreateView, AudioElementRetrieveUpdateDeleteView,AudioFragmentListView

urlpatterns = [
    path('audio-elements/', AudioElementListCreateView.as_view(), name='audio-element-list'),
    path('audio-elements/<int:id>/', AudioElementRetrieveUpdateDeleteView.as_view(), name='audio-element-detail'),
    path('audio-fragments/<int:start_time>/<int:end_time>/', AudioFragmentListView.as_view(), name='audio-fragments'),
]
