from django.urls import path
from .views import HomePageView, AboutPageView, FruitsPageView, SFoodPageView, ContactPageView

urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
	path('about/',AboutPageView.as_view(), name = 'about'),
	path('fruits/',FruitsPageView.as_view(), name = 'fruits' ),
	path('seafood/', SFoodPageView.as_view(), name = 'seafood'),
	path('contact/', ContactPageView.as_view(), name = 'contact')


]