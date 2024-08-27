import json
from backrafApp.models import StationData, SensorData

with open("C:/Users/Matias/Downloads/RAFDB.stationdata.json") as f:
    datos = json.load(f)
    
    for entrada in datos:
        sensores_datos = entrada['sensors']
        
        sensores = SensorData.objects.create(
            solar_radiation_avg=sensores_datos.get('solarRadiation', {}).get('avg', None),
            solar_panel_last=sensores_datos.get('solarPanel', {}).get('last', None),
            # Mapea el resto de los campos usando get(), asegurándote de proporcionar un valor por defecto como None
        )
        
        StationData.objects.create(
            station_id=entrada['stationID']['$oid'],
            date=entrada['date']['$date'],
            sensors=sensores
        )
