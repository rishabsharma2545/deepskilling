from django.shortcuts import render
from django.http import HttpResponse

# 8. In courses/views.py, create a simple function-based view hello_view 
# that returns an HttpResponse with 'Course Management API is running'.
def hello_view(request):
    return HttpResponse('Course Management API is running')

# 27. In courses/views.py, create a CourseListView using DRF's APIView: 
# handle GET (return all courses serialized) and POST (create a new course from request.data).

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action

from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer

class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# 28. Create a CourseDetailView for GET (single course by pk), PUT (update), and DELETE operations.

class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None
        
    def get(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            ) 
        
        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
# 31. Replace CourseListView and CourseDetailView with a single CourseViewSet that extends viewsets.ModelViewSet. 

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    # 34. Add a custom action to CourseViewSet using the @action decorator: 
    # a GET endpoint /api/courses/{id}/students/ that returns all students enrolled in that course.
    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        course = self.get_object()

        students = Student.objects.filter(enrollments__course = course).distinct()

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

# 33. Do the same for StudentViewSet and EnrollmentViewSet.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
