from django.urls import path,include
from users import views as userViews
from books import views as bookviews
from borrow_records import views as borrowviews
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('authors',userViews.AllAuthorsViewSet)
router.register('members', userViews.AllMembersViewSet)
router.register('books', bookviews.BookViewSet)
router.register('borrow-records',borrowviews.AllBorrowRecordsViewSet)


urlpatterns = router.urls


# urlpatterns = [
#     path('', include(router.urls)),
# ]