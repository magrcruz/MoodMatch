from django.urls import path

from .views import SignUpView, CustomLoginView,PremiunSubscriptionView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("premiun_subscription/", PremiunSubscriptionView.as_view(), name="premium"),

]