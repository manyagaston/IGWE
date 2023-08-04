from rest_framework import routers
from .views import QuestionViewsets,PersonneSerializer


router = routers.DefaultRouter()
router.register('Questions', QuestionViewsets)

router = routers.DefaultRouter()
router.register('Personne', PersonneSerializer)

