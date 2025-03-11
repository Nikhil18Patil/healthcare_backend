
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()

class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="User Registration (Customer)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "first_name", "last_name", "mobile", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, format="email"),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "mobile": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format="password"),
            },
        ),
        responses={
            201: openapi.Response(description="User registered successfully", examples={"application/json": {"message": "User registered successfully"}}),
            400: openapi.Response(description="Validation errors", examples={"application/json": {"error": "All fields are required"}}),
            500: openapi.Response(description="Internal server error", examples={"application/json": {"error": "Some error message"}}),
        }
    )
    def post(self, request):
        try:
            email = request.data.get("email")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            mobile = request.data.get("mobile")
            password = request.data.get("password")

            if not email or not password or not first_name or not last_name or not mobile:
                return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                password=make_password(password)
            )

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            data["first_name"] = self.user.first_name
            data["last_name"] = self.user.last_name
            data["mobile"] = self.user.mobile
            return data
        except Exception as e:
            raise ValueError(f"Authentication error: {e}")

class LoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
