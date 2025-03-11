from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# --- Patient-Doctor Mapping APIs ---
class PatientDoctorMappingListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve all patient-doctor mappings",
        responses={
            200: openapi.Response("Success", PatientDoctorMappingSerializer(many=True)),
            500: openapi.Response("Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request):
        try:
            mappings = PatientDoctorMapping.objects.all()
            serializer = PatientDoctorMappingSerializer(mappings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Create a new patient-doctor mapping",
        request_body=PatientDoctorMappingSerializer,
        responses={
            201: openapi.Response("Created", PatientDoctorMappingSerializer),
            400: openapi.Response("Bad Request"),
            500: openapi.Response("Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def post(self, request):
        try:
            import pdb ; pdb.set_trace()
            serializer = PatientDoctorMappingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PatientDoctorMappingDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve mappings for a specific patient",
        responses={
            200: openapi.Response("Success", PatientDoctorMappingSerializer(many=True)),
            500: openapi.Response("Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request, patient_id):
        try:
            mappings = PatientDoctorMapping.objects.filter(patient__id=patient_id)
            serializer = PatientDoctorMappingSerializer(mappings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Delete a specific patient-doctor mapping",
        responses={
            204: openapi.Response("No Content"),
            404: openapi.Response("Not Found"),
            500: openapi.Response("Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def delete(self, request, pk):
        try:
            mapping = PatientDoctorMapping.objects.get(pk=pk)
            mapping.delete()
            return Response({"message": "Mapping deleted"}, status=status.HTTP_204_NO_CONTENT)
        except PatientDoctorMapping.DoesNotExist:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
