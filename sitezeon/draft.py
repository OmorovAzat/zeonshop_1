import random


katerand_list = ("Ali", "Azat", "Aman", "Oskon", "Ismail")

print(random.choice(katerand_list))



# class IzbrannyeApiView(generics.ListAPIView):
#     queryset = Tovar.objects.filter(available=True)[0:12]
#     serializer_class = IzbrannyeSerializer


class SliderApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
#
# class NovinkiApiView(generics.ListAPIView):
#     queryset = Tovar.objects.filter(newlst=True)
#     serializer_class = NovinkiListSerializer



# class Hitofsales