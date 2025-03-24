from temp_socket import *
from mongo_function import *
from datetime import datetime
import pytz
IST = pytz.timezone('Asia/Kolkata')
from datetime import datetime
datetime_ist = datetime.now(IST) 
vendor = 'Fleetx_SL'
group_id = '5682'
trip_status = 1
result = get_trip_data(vendor) #fetch trip from courier table
# print(result)
count = len(result)
# print(count)
# exit()
vehicle = []
imei = []
     # print(result)
for document in result:
    # print(document)
    # exit()
    vehicle.append(document['vehicle_no'])
    imei.append(document['imei_no'])
print(vehicle)
# exit()

url = "https://vehicletrack.membocool.com/conservice.aspx?method=currentlockstatus&AID=AAE5CBB17C3C88C651A6A5DBE7Dsa246C699BB36da89874596324&UID=SAN001753&PWD=348624&VNo=All"


payload = {}
headers = {}

resp_arr = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
# print(data)
# exit()
for resp in data['returnds']:
    if resp['Trackingtime']!='':

        vehicleNumber = resp['vehicleNumber']
        if resp['lockstatus']=='Unlocked':
            lockstatus = 1
        else:
            lockstatus = 0 
        date_time = resp['Trackingtime'].strip()
        date_nw = datetime.strptime(date_time, '%d/%m/%Y %H:%M:%S')
        # print(date_nw)
        # exit()
        lat = resp['Lat']
        lng = resp['lng']

        resp_arr[vehicleNumber] = {
        "vehicleNumber" :vehicleNumber,
        'latitude':lat,
        'longitude':lng,
        'lockstatus':lockstatus,
        'createdDate':date_nw,
        }
        # print(resp_arr)  
        # exit()      


for vehicle_no in vehicle:
    imei_no = vehicle_no
    # print(imei_no)
    ApiResp = resp_arr[imei_no]['vehicleNumber']
    if ApiResp!='':
        imeitemp = resp_arr[imei_no]['vehicleNumber']
        lattemp = resp_arr[imei_no]['latitude']
        lngtemp = resp_arr[imei_no]['longitude']
        lockstatustemp = resp_arr[imei_no]['lockstatus']
        datetemp = resp_arr[imei_no]['createdDate']

        ver = "V3P"
        SupVoltage = ""
        speed =0.0
        # print(f"\nImei={imeitemp},Lat={lattemp},Lng={lngtemp},datetime={datetemp}")
        # exit()
        igni_io1 = ""
        igni_io2 = lockstatustemp
        igni_io3 = ""
        igni_io4 = ""
        igni_io5 = ""
        igni_io6 = ""
        igni_io7 = ""
        igni_io8 = ""
        ver = "V3P"
        MsgType = "NORMAL"
        Fix = ""
        speed = speed
        Signal_Strength = ""

        SupplyVoltage = ""
        CellName = ""
        ax = ""
        ay = ""
        az = ""
        mx = ""
        my = ""
        mz = ""
        bx = ""
        by = ""
        bz = ""
        SimID = ""
        No_Of_Satellites = ""

        data = f"{imeitemp},{datetemp},{MsgType},{ver},{Fix},{lattemp},{lngtemp},{speed},{igni_io1},{igni_io2},{igni_io3},{igni_io4},{igni_io5},{igni_io6},{igni_io7},{igni_io8},{Signal_Strength},{SupplyVoltage},{CellName},{ax},{ay},{az},{mx},{my},{mz},{bx},{by},{bz},{SimID},{No_Of_Satellites},eof"

        print(data)
        telnet_data(data)
        # print("\n\n")



