
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get list of all doctors",
        responses={
            200: openapi.Response("Success", DoctorSerializer(many=True)),
            500: openapi.Response(description="Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request):
        try:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Create a new doctor",
        request_body=DoctorSerializer,
        responses={
            201: openapi.Response("Doctor created successfully", DoctorSerializer),
            400: openapi.Response(description="Validation errors"),
            500: openapi.Response(description="Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ]
    )
    def post(self, request):
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DoctorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Get details of a specific doctor",
        responses={
            200: openapi.Response("Success", DoctorSerializer),
            404: openapi.Response(description="Doctor not found"),
            500: openapi.Response(description="Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, pk):
        try:
            doctor = self.get_object(pk)
            if not doctor:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Update details of a specific doctor",
        request_body=DoctorSerializer,
        responses={
            200: openapi.Response("Doctor updated successfully", DoctorSerializer),
            404: openapi.Response(description="Doctor not found"),
            400: openapi.Response(description="Validation errors"),
            500: openapi.Response(description="Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ]
    )
    def put(self, request, pk):
        try:
            doctor = self.get_object(pk)
            if not doctor:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = DoctorSerializer(doctor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Delete a specific doctor",
        responses={
            204: openapi.Response("Doctor deleted successfully"),
            404: openapi.Response(description="Doctor not found"),
            500: openapi.Response(description="Internal Server Error")
        },
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer Token", type=openapi.TYPE_STRING)
        ]
    )
    def delete(self, request, pk):
        try:
            doctor = self.get_object(pk)
            if not doctor:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
            doctor.delete()
            return Response({"message": "Doctor deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
