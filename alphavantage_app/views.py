
from django.conf import settings
from django.shortcuts import render
from alpha_vantage.timeseries import TimeSeries
import csv
import json


def data_view(request):
    f = open('NASDAQ.csv')
    reader = csv.DictReader(f)
    symbols_list = json.dumps([row for row in reader])
    f = open('parsedNASDAQ.json', 'w')
    f.write(symbols_list)
    sym = json.loads(symbols_list)

    api_list = [{'id': '1', 'name': 'Alpha Vantage'},
                {'id': '2', 'name': 'Alpaccaa'}]

    symbols_parent_list = [{'id': '1', 'name': 'NASDAQ'},
                           {'id': '2', 'name': 'AMEX'},
                           {'id': '3', 'name': 'NYSE'}]

    data_type_list =[{'id': '1', 'name': 'Intraday'},
                     {'id': '2', 'name': 'Daily'},
                     {'id': '3', 'name': 'Weekly'},
                     {'id': '4', 'name': 'Monthly'}
                    ]
    api_data = None
    symbol_detail = None
    data_type = None
    if request.method == "POST":
        symbol_detail = request.POST.get('symbol_detail', None)
        data_type = request.POST.get('data_type', None)
        symbol_parent_detail = request.POST.get('symbol_parent_detail', None)
        api_detail = request.POST.get('api_detail', None)
        # api_key= request.POST.get('API_KEY', None)
        # print(api_key)
        # IF0GVC63L4LYZKYP
        if api_detail == '1':
            ts = TimeSeries(key=settings.API_KEY, output_format='json')
            if data_type == 'Intraday':
                api_data, meta_data = ts.get_intraday(symbol=symbol_detail, interval='1min', outputsize='full')
            elif data_type == 'Weekly':
                api_data, meta_data = ts.get_weekly(symbol=symbol_detail)
            elif data_type == 'Daily':
                api_data, meta_data = ts.get_daily(symbol=symbol_detail)
            else:
                api_data, meta_data = ts.get_monthly(symbol=symbol_detail)

    return render(request, "djblog/alphavantage_app/test.html", {
        'api_list': api_list,
        'symbols_parent_list': symbols_parent_list,
        'symbols_list': sym,
        'data_type_list': data_type_list,
        'api_data': api_data,
        'symbol_name': symbol_detail,
        'type_of_data': data_type,
    })
