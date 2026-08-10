raw_stations = [ 
{"station_code": "S301", "type": "fast", "price_per_kwh": 5000, "status": "available"}, 
{"station_code": " s101 ", "type": "normal", "price_per_kwh": 3000, "status": "available"}, 
{"station_code": "S202", "type": "ultra_fast", "price_per_kwh": 7000, "status": 
"occupied"}, 
{"station_code": "S102", "type": "normal", "price_per_kwh": 3200, "status": 
"maintenance"}, 
{"station_code": "S302", "type": "fast", "price_per_kwh": 5500, "status": "available"} 
] 


def clean_and_validate_stations(station_code):
    clean_code = station_code.strip().upper()

    if clean_code[1:2].isdigit() and clean_code.startswith("S") or clean_code.startswith("s") :
        ok_code = clean_code
        return ok_code
    else: 
        return None


def  search_stations(price_per_kwh, status):
    
    for raw_station in raw_stations:
        if raw_station[status] == None:
            if raw_station[price_per_kwh] <= price_per_kwh:
                return raw_station
        if raw_station[price_per_kwh] <= price_per_kwh and raw_stations[status]:
            return raw_station


def  sort_stations_by_price_desc(raw_stations):
    for i in range(len(raw_stations)):
        swapped = False
        for j in range(len(raw_stations) - i - 1):
            if raw_stations[j]["price_per_kwh"] < raw_stations[j + 1]["price_per_kwh"]:
                raw_stations[j], raw_stations[j + 1] = raw_stations[j + 1], raw_stations[j]
                swapped = True
        if not swapped:
            break






























