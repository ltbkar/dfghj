from django.views import generic
from . import models


class AllClothView(generic.ListView):
    template_name = 'cloth/all_cloth.html'
    context_object_name = 'cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class MenClothView(generic.ListView):
    template_name = 'cloth/male_cloth.html'
    context_object_name = 'male'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='For Men').order_by('-id')


class WomenClothView(generic.ListView):
    template_name = 'cloth/woman_cloth.html'
    context_object_name = 'female'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='For Women').order_by('-id')


class KidsClothView(generic.ListView):
    template_name = 'cloth/kids_cloth.html'
    context_object_name = 'kids'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='For Kids').order_by('-id')
