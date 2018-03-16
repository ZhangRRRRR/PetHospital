from django.shortcuts import render
from django.http import HttpResponse

from .models import DiseaseCase, DiseaseEntity, DiseaseStage, TextInformation, ImageInformation, VideoInformation
import json


# Create your views here.
def get_case_by_entity(request,entity_id):
    cases = DiseaseCase.objects.filter(diseaseEntity=entity_id)
    if cases.exists():
        entity = DiseaseEntity.objects.get(id=entity_id)  # error
        list = []
        for c in cases:
            case = {}
            case["caseId"] = c.id
            case["caseName"] = c.name
            case["diseaseEntity"] = entity.name
            stages = DiseaseStage.objects.filter(diseaseCase=c.id)
            if stages.exists():
                for stage in stages:
                    info = {}
                    text = TextInformation.objects.filter(diseaseStage=stage.id)
                    info["text"] = []
                    for t in text:
                        info["text"].append(t.content)
                    image = ImageInformation.objects.filter(diseaseStage=stage.id)
                    info["image"] = []
                    for i in image:
                        info["image"].append(i.content)
                    video = VideoInformation.objects.filter(diseaseStage=stage.id)
                    info["video"] = []
                    for v in video:
                        info["video"].append(v.content)
                    stage_name = stage.name
                    case[stage_name] = info
            else:
                case["stageError"] = "no disease stage"
            list.append(case)
        return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"caseError": "no disease case"}), content_type="application/json")
