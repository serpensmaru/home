from django.urls import path
from measurement.views import sensor_update, add_measurement, get_info_id, SensorGetList, add_sensor


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor_update/', sensor_update),
    path('add_measurement/', add_measurement),
    path('get_info_id/', get_info_id),
    path('get_list_sensor/', SensorGetList.as_view()),
    path('add_sensor/', add_sensor),

]
