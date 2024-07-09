from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.http import HttpResponse
from .models import Commodity, CommodityData, IntegrityError
from django.contrib import messages


# Create your views here.

api_key2 = 'JW2GUJL7N4MM85CW'
api_key = 'NJ7SLFGP1D1SO7N8'
#Chave da API foram mantidas por se tratar de um projeto de avaliação, e não de um código que entrará em produção. Além disso, trata-se de chaves demo.



def index(request):
    commodities = Commodity.objects.all()
    return render(request, 'dados_financeiros/main.html', {'commodities': commodities})

def fetching_data(request):
    if request.method == 'POST':
        commodity = request.POST.get('commodity')
        url = f'https://www.alphavantage.co/query?function={commodity}&interval=annual&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        if 'Note' in data:
            messages.error(request, 'Limite de requisições excedido')
            return HttpResponse('Limite de requisições excedido', status=429)
        messages.success(request, 'Banco de dados atualizado com sucesso!')
        
        if 'name' in data and 'interval' in data and 'unit' in data and 'data' in data:
            commodity_obj, created = Commodity.objects.get_or_create(
                name=data['name'], 
                interval=data['interval'], 
                unit=data['unit']
            )
            for item in data['data']:
                if 'date' in item and 'value' in item:
                    try:
                        value = float(item['value'])
                        date = item['date']
                        
                        if not CommodityData.objects.filter(commodity=commodity_obj, date=date, value=value).exists():
                            CommodityData.objects.create(
                                commodity=commodity_obj, 
                                date=date, 
                                value=value
                            )
                    except ValueError:
                        messages.error(request, 'Dados incompletos desconsiderados')
                        break
                    except IntegrityError:
                        messages.info(request, f'Dados já presentes no banco de dados')
                        break

        commodities = Commodity.objects.all()
        return render(request, 'dados_financeiros/main.html', {'commodities': commodities})
    return HttpResponse('Estrutura de dados inválida', status=400)

def showing_data(request):
    if request.method == 'GET':
        commodity_name = request.GET.get('commodity_data')
        if commodity_name:
            try:
                commodity = Commodity.objects.get(name=commodity_name)
                return render(request, 'dados_financeiros/main.html', {'commodity': commodity})
            except Commodity.DoesNotExist:
                messages.error(request, 'Nenhuma commodity encontrada no banco de dados com o nome fornecido. Tente atualizar os dados com a API.')
                return redirect('index')
        else:
            messages.error(request, 'Nenhuma commodity foi selecionada.')
            return redirect('index')
    return HttpResponse('Método não permitido', status=405)

def delete_data(request):
    if request.method == 'POST':
        commodity_name = request.POST.get('commodity')
        commodity = get_object_or_404(Commodity, name=commodity_name)
        commodity.data.all().delete()
        return redirect('index') 
    return HttpResponse('Método não permitido', status=405)

def edit_notes(request,data_id):
   if request.method == 'POST':
        notes = request.POST.get('notes')
        commodity_data = get_object_or_404(CommodityData, id=data_id)
        commodity_data.notes = notes
        commodity_data.save()
        return redirect('index') 

def delete_note(request,data_id):
    if request.method == 'POST':
        commodity_data = get_object_or_404(CommodityData, id=data_id)
        commodity_data.notes = None
        commodity_data.save()
        return redirect('index') 
    return HttpResponse('Método não permitido', status=405)