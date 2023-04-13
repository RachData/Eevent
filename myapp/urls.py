from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .authentication.views import login_view, signup, logout_view
from .authentication.api_views import UserList, UserDetail, LogoutView
from .events.views import home, create_event, update_event, delete_event
from .events.api_views import EventList, EventDetail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('create_event/', create_event, name='create_event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('event_list/', EventList.as_view(), name='event_list'),
    path('event_detail/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserList.as_view(), name='api_user_list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='api_user_detail'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/events/', EventList.as_view(), name='api_event_list'),
    path('api/events/<int:pk>/', EventDetail.as_view(), name='api_event_detail'),
]