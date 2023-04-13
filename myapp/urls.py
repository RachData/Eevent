from django.urls import path
from .authentication.views import login_view, signup, logout_view
from .events.views import home, create_event, update_event, delete_event, event_list, event_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('create_event/', create_event, name='create_event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('event_list/', event_list, name='event_list'),
    path('event_detail/<int:event_id>/', event_detail, name='event_detail'),
]