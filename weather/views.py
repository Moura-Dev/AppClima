import requests
from django.shortcuts import render, redirect
from .models import Cidade
from .forms import CidadeForm


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=972813cb54cdee188e18d871cf292c95'

    err_msg = ''
    message = ''
    message_class = ''


    if request.method == 'POST':
        form = CidadeForm(request.POST)

        if form.is_valid():
            nova_cidade = form.cleaned_data['name']
            contar_cidades = Cidade.objects.filter(name=nova_cidade).count()

            if contar_cidades == 0:
                r = requests.get(url.format(nova_cidade)).json()
                print(r)
                if r['cod'] == 200:
                    form.save()
                    form.save()
                else:
                    err_msg = 'Cidade não existe no banco de dados!'

            else:
                err_msg = 'Cidade Ja existe no banco de dados!'


        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = "Cidade Adicionada com Sucesso!"
            message_class = 'is-sucess'

    form = CidadeForm()


    cidades = Cidade.objects.all()

    weather_data = []

    for cidade in cidades:


        r = requests.get(url.format(cidade)).json()

        cidade_weather = {
            'city': cidade.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(cidade_weather)

    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class
    }
    return render(request, 'weather/weather.html', context)



def delete_cidade(request, cidade_nome):
    Cidade.objects.get(name=cidade_nome).delete()
    return redirect('home')
