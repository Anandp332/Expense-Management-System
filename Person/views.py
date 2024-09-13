from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer


class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.filter(is_deleted=False)
        serializer = PersonSerializer(persons, many=True)
        return Response({"data": serializer.data}, status=200)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Person Table Created Successfully"}, status=201)
        return Response({"Error": "Person Table Not Created"}, status=400)


class PersonViewById(APIView):
    def get(self, request, pk):
        person = Person.objects.filter(pk=pk, is_deleted=False).first()
        if not person:
            return Response({"Error": "Invalid Primary Key or Record Not Found"}, status=404)
        serializer = PersonSerializer(person)
        return Response({"data": serializer.data}, status=200)

    def put(self, request, pk):
        person = Person.objects.filter(pk=pk, is_deleted=False).first()
        if not person:
            return Response({"Error": "Invalid Primary Key"}, status=404)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Person Table Updated Successfully"}, status=200)
        return Response({"Error": "Person Table Not Updated"}, status=400)

    def patch(self, request, pk):
        person = Person.objects.filter(pk=pk, is_deleted=False).first()
        if not person:
            return Response({"Error": "Invalid Primary Key"}, status=404)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Person Table Updated Successfully"}, status=200)
        return Response({"Error": "Person Table Not Updated"}, status=400)

    def delete(self, request, pk):
        person = Person.objects.filter(pk=pk, is_deleted=False).first()
        if not person:
            return Response({"Error": "Invalid Primary Key"}, status=404)
        person.is_deleted = True
        person.save()
        return Response({"message": "Person Table Deleted Successfully"}, status=200)
