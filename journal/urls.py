from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('login', views.sign_in, name='login'),
    path('logout', views.sign_out, name='logout'),
    path('<table>/', views.table_view, name='table_view'),
    path('<table>/order-by-<int:amount_items>', views.table_view, name='order_by'),
    path('view/<table>/<int:pk>', views.entry_view, name='entry_view'),
    path('view/<table>/<int:pk>/<delete>', views.entry_view, name='delete_entry'),
    path('create/<table>/', views.create_entry, name='create_entry'),
    path('update/<table>/<int:pk>/', views.create_entry, name='update_entry')
]