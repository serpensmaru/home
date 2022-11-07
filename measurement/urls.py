from django.urls import path
from measurement.views import add_measurement, get_info_id, SensorGetList, SensorCls


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('add_measurement/', add_measurement),
    path('get_info_id/', get_info_id),
    path('get_list_sensor/', SensorGetList.as_view()),
    path('add_sensor/', SensorCls.as_view()),                  #  POST запрос на добавление датчика
    path('sensor_update/<pk>', SensorCls.as_view()),           #  PUT запрос на изменение датчика
]
