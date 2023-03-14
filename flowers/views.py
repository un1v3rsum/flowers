from rest_framework import status
from rest_framework.response import Response
from .models import Flower
from .serializers import FlowerSerializer
from .filters import FlowerFilter
from rest_framework.decorators import api_view
from django.shortcuts import render


#main page view
from django.shortcuts import render
from .models import Flower
from .forms import MyFilterForm

def my_view(request):
    filter_form = MyFilterForm(request.GET)
    if filter_form.is_valid():
        filter_option = filter_form.cleaned_data['filter_option']
        queryset = Flower.objects.filter(field_name=filter_option)
    else:
        queryset = Flower.objects.all()

    return render(request, 'my_template.html', {'filter_form': filter_form, 'data': queryset})
#def flower_list(request, format=None):
    #filtered_flowers = FlowerFilter(request.GET, queryset=Flower.objects.all())
    #TO-DO -> make "species" filter selectable by attribute
    #context['filtered_flowers'] = filtered_flowers
    #context = {'filtered_flowers': filtered_flowers}
    #TO-DO aggregate - average and max
    #print(Flower.objects.aggregate(count = Count('id'), minSepalL = Min('sepal_length')))
    #return render(request, 'base.html',context=context)

#single flower view
@api_view(['GET', 'PUT', 'DELETE'])
def flower_detail(request,id, format=None):
    #checks if id number exist -> else: returns not_found error
    try:
        flower = Flower.objects.get(pk=id)
    except Flower.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get one flower from database
    if request.method == 'GET':
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    #enter new data into database
    elif request.method == 'PUT':
        serializer = FlowerSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete data from database
    elif request.method == 'DELETE':
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)