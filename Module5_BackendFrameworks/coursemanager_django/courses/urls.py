# 29. Wire both views in courses/urls.py: 
# path('courses/', CourseListView.as_view()) and 
# path('courses/<int:pk>/', CourseDetailView.as_view()). 

from django.urls import path 
from rest_framework.routers import DefaultRouter
from .views import CourseListView, CourseDetailView
from .views import CourseViewSet, StudentViewSet, EnrollmentViewSet

urlpatterns = [
    path("courses/", CourseListView.as_view(), name = "course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name = "course-detail")
]

# 32. Create a DefaultRouter in courses/urls.py and register the viewset: router.register('courses', CourseViewSet). 
# Include router.urls. Observe how the router auto-generates all URL patterns.

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"students", StudentViewSet)
router.register(r"enrollments", EnrollmentViewSet)

urlpatterns = router.urls # automatically generates routes for all CRUD operations
