from rest_framework.decorators import api_view
from patient_api.serializers import PatientApiSerializer as TutorialSerializer
from patient_api.models import PatientApi as Tutorial
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")


@api_view(['GET', 'POST', 'DELETE'])
def event_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.query_params.get('patient_name', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def event_details(request, pk):
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         tutorial_serializer = TutorialSerializer(tutorial)
#         return JsonResponse(tutorial_serializer.data)

#     elif request.method == 'PUT':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         tutorial.delete()
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def event_list_past(request):
#     tutorials = Tutorial.objects.filter(flag=False)

#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)


# @api_view(['GET'])
# def event_list_future(request):
#     tutorials = Tutorial.objects.filter(flag=True)

#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['GET', 'DELETE'])
def get_event(request, patient_name):
    # tutorials = Tutorial.objects.filter(title=title)
    tutorials = Tutorial.objects.filter(
        patient_name=patient_name)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'DELETE':
        tutorials.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
