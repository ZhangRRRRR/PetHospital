from django.contrib import admin
from .models import DiseaseCase,DiseaseEntity,DiseaseStage,DiseaseType,TextInformation,ImageInformation,VideoInformation,Vaccine,CheckItem,Medicine

# Register your models here.
admin.site.register(DiseaseCase)
admin.site.register(DiseaseEntity)
admin.site.register(DiseaseStage)
admin.site.register(DiseaseType)
admin.site.register(TextInformation)
admin.site.register(ImageInformation)
admin.site.register(VideoInformation)
admin.site.register(Vaccine)
admin.site.register(CheckItem)
admin.site.register(Medicine)