from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer


class SensorGetList(ListAPIView):
    """ ПОлучить сипско датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


@api_view(["GET"])
def get_info_id(request):
    """ Информация о датчике и его измерениях"""
    id = request.GET.get('sensor_id')
    id = int(id)
    sensor = Sensor.objects.filter(id=id).first()
    ser = SensorSerializer(sensor)
    info = dict(ser.data)
    info["measurement"] = []
    for temp in sensor.sensor.all():
        temperature = temp.temperature
        date = temp.created_at
        intro = {"temperature": temperature, "created_at": date}
        info["measurement"].append(intro)
    return Response(info)


@api_view(["POST"])
def sensor_update(request):
    """ Изменение информации о датчике"""
    id = request.GET.get('sensor_id')
    sensor_name = request.GET.get('name')
    description = request.GET.get('desc')
    values = {'name':sensor_name, 'description': description}
    keys = values.keys()
    for key in keys:
       if values[key] == None:
           del(values[key])
    Sensor.objects.select_for_update().filter(id=id).update(**values)
    return Response({'status': 'Обновление успешно прошло'})


@api_view(["POST"])
def add_measurement(request):
    """ Добавить измерение у датчика по id"""
    id = request.GET.get('sensor_id')
    temperature = request.GET.get('temp')
    temperature = float(temperature)
    id = int(id)
    sensor = Sensor.objects.filter(id=id).first()
    Measurement(temperature=temperature, sensor=sensor).save()
    return Response({'status': 'Измерение успешно добавлено'})


@api_view(["POST"])
def add_sensor(request):
    """ Добавить измерение у датчика по id"""
    name = request.GET.get('name')
    description = request.GET.get('description')
    Sensor(name=name, description=description).save()
    return Response({'status': 'Датчик успешно добавлен'})


class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer
