from django.urls import path 
from .  import views 
app_name ='app1'



urlpatterns = [

    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path('signup',views.signup_view,name='signup'),
    path('Booksu',views.Booksu,name='Booksu'),
    path('<int:book_id>',views.add,name='add'),
    path('addform',views.addform,name='addform'),
    path('update/<int:book_id>',views.update,name='update'),

 ]