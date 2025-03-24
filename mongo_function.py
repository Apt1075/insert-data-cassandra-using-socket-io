import requests
import json


def get_trip_data(vendor):
    try:
        response = []
        condition = []
        # url = ''
        url = ""

        payload={'conditions': '{ "trip_status":1,"group_id":"5682","gps_vendor_name":"'+vendor+'"}',"table": "courier_trip_detail","fields": '{}'}
        # print(payload)
        files=[]
        headers = {}
        result = requests.request("POST", url, headers=headers, data=payload, files=files)
        data = result.json()
        # exit()
        # data_decode = json.load(data)
        # print(data)
        # exit()
        for i in data:
            # print(i)
            # exit()
            response.append(i)
        return response
    except Exception as e:
        print(f'Error in reading Travel records from  Mongo db: {e}')
 
