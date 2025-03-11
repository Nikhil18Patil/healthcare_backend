from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Patient
from .serializers import PatientSerializer

# --- Patient APIs ---
class PatientListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of patients",
        responses={200: PatientSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request):
        try:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Create a new patient",
        request_body=PatientSerializer,
        responses={201: PatientSerializer(), 400: "Bad Request"},
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def post(self, request):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PatientDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a single patient",
        responses={200: PatientSerializer(), 404: "Patient not found"},
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request, pk):
        try:
            patient = self.get_object(pk)
            if not patient:
                return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Update a patient's details",
        request_body=PatientSerializer,
        responses={200: PatientSerializer(), 400: "Bad Request", 404: "Patient not found"},
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def put(self, request, pk):
        try:
            patient = self.get_object(pk)
            if not patient:
                return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Delete a patient",
        responses={204: "Patient deleted", 404: "Patient not found"},
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ],
    )
    def delete(self, request, pk):
        try:
            patient = self.get_object(pk)
            if not patient:
                return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
            patient.delete()
            return Response({"message": "Patient deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)