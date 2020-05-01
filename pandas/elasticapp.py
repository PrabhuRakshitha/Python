import elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd


if __name__ == "__main__":
    es_obj = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es_obj:
        print("connected to elastic search")
    else:
        print('some error')

    # response = elastic_client.update(index='employee', body = source_to_update)
    # print('response:', response)
    csv_file = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    try:
        covid_global = pd.read_csv(csv_file)
    except FileNotFoundError:
        error_message = 'Not able to load file'

    covid_global.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
    covid_global_summary = covid_global.groupby('Country/Region').sum()
    serialized_data = covid_global_summary.to_dict(orient='index')
    for rec_key in serialized_data:
        print(rec_key)
        es_obj.index(index='covid19', id=rec_key ,body=serialized_data[rec_key])

    # resp=es_obj.bulk(body=serialized_data,index="COVID19")
    # print(resp['result'])






