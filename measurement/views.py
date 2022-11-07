from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer





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
def add_measurement(request):
    """ Добавить измерение у датчика по id"""
    id = request.GET.get('sensor_id')
    temperature = request.GET.get('temp')
    temperature = float(temperature)
    id = int(id)
    sensor = Sensor.objects.filter(id=id).first()
    Measurement(temperature=temperature, sensor=sensor).save()
    return Response({'status': 'Измерение успешно добавлено'})


class SensorGetList(ListAPIView):
    """ ПОлучить сипско датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer



class SensorCls(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, reauest):
        sens_new = reauest.data.get("sensor")
        print(sens_new)
        serializer = SensorSerializer(data=sens_new)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
        return Response({"success": "Sensor '{}' created successfully".format(sensor_saved)})


    def put(self, request, pk):
        saved_article = get_object_or_404(Sensor.objects.all(), pk=pk)
        data = request.data.get('sensor')
        serializer = SensorSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
        return Response({
            "success": "Sensor '{}' updated successfully".format(sensor_saved)})

