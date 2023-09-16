from rest_framework.views import APIView
from customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomerListView(APIView):
    @swagger_auto_schema(
        operation_summary="List all customers",
        operation_description="Returns a list of all customers.",
        responses={200: CustomerSerializer(many=True)},
    )
    def get(self, request):
        """
        List all customers.
        """
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new customer",
        operation_description="Creates a new customer.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Customer name'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Customer email'),
            },
        ),
        responses={201: CustomerSerializer()},
    )
    def post(self, request):
        """
        Create a new customer.
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a customer by ID",
        operation_description="Retrieves a customer by their unique ID.",
        responses={200: CustomerSerializer()},
    )
    def get(self, request, id, format=None):
        """
        Retrieve a customer by ID.
        """
        customer = Customer.objects.filter(id=id).first()
        if customer is not None:
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a customer by ID",
        operation_description="Updates a customer's information by their unique ID.",
        request_body=CustomerSerializer(),
        responses={200: CustomerSerializer()},
    )
    def put(self, request, id, format=None):
        """
        Update a customer by ID.
        """
        customer = Customer.objects.filter(id=id).first()
        if customer is not None:
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete a customer by ID",
        operation_description="Deletes a customer by their unique ID.",
        responses={204: "No Content"},
    )
    def delete(self, request, id, format=None):
        """
        Delete a customer by ID.
        """
        customer = Customer.objects.filter(id=id).first()
        if customer is not None:
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)
