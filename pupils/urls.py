from rest_framework.routers import DefaultRouter
from . views import Exam_materialsViewSet, CoursesViewSet, BestPupilsViewSet

router=DefaultRouter()
router.register(r'materials', Exam_materialsViewSet, basename='materials')
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'best_pupils', BestPupilsViewSet, basename='best_pupils')

urlpatterns = [

] + router.urls