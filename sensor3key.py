import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatesensor3key():

    global sensor3keypair

    sensor3keypair = {}
    
    checksensor3key = []

    sensor3id = 'sensor3_ID'
    sensor3privatekey = 'sensor3_privatekey'
    sensor3publickey = 'sensor3_publickey'
    sensor3flag = 'sensor3_flag'
        
    count = 0
    while (count <16):

        sensor3keys = libnacl.public.SecretKey()
       
        sensor3privkey = str(sensor3keys.sk)
        sensor3pubkey = str(sensor3keys.pk)

        sensor3unique_id= sensor3privkey + sensor3pubkey

        sensor3flag = "active"

        sensor3keypair.setdefault(sensor3id,[])
        sensor3keypair.setdefault(sensor3privatekey,[])
        sensor3keypair.setdefault(sensor3publickey,[])
        sensor3keypair.setdefault(sensor3flag,[])
        
        checksensor3key.append(sensor3privkey)
        checksensor3key.append(sensor3pubkey)

        if not sensor3keypair.setdefault(sensor3id):

            sensor3keypair[sensor3id].append(sensor3unique_id)
            sensor3keypair[sensor3privatekey].append(sensor3privkey)
            sensor3keypair[sensor3publickey].append(sensor3pubkey)
            sensor3keypair[sensor3flag].append(sensor3flag)

            #print("PRIVKEYYYY", sensor3keypair[sensor3privatekey])
            print("SENSOR 3 PUBLIC KEY: ", sensor3keypair[sensor3publickey])
        
        else:
            for sensor3key in checksensor3key: 
                sensor3occurences=[index for index, value in enumerate(checksensor3key) if value == sensor3key]
                if len(sensor3occurences)>1:
                    check_sensor3key = libnacl.public.SecretKey()
                    checksensor3keys_box = libnacl.public.Box(check_sensor3key.sk, check_sensor3key.pk)

                    check_sensor3privkey = str(check_sensor3key.sk)
                    check_sensor3pubkey= str(check_sensor3key.pk)
                    check_sensor3unid = check_sensor3privkey + check_sensor3pubkey
                    check_sensor3flag = "active"

                    sensor3keypair[sensor3id].append(check_sensor3unid)
                    sensor3keypair[sensor3privatekey].append(check_sensor3privkey)
                    sensor3keypair[sensor3publickey].append(check_sensor3pubkey)
                    sensor3keypair[sensor3flag].append(check_sensor3flag)

                    sensor3occurences.pop()
                    [checksensor3key.remove(sensor3key)for o in sensor3occurences]
                    print("failed")
                    break;

            else:
                sensor3keypair[sensor3id].append(sensor3unique_id)
                sensor3keypair[sensor3privatekey].append(sensor3privkey)
                sensor3keypair[sensor3publickey].append(sensor3pubkey)
                sensor3keypair[sensor3flag].append(sensor3flag)
                print("success")
                                
        count+=1

    '''
    for sensor3pubkey in sensor3keypair[sensor3publickey]:
        print("Sensor 3 Public key:",sensor3pubkey)
    
    for sensorpriv3key in sensor3keypair[sensor3privatekey]:
        print("Sensor 3 Private key:", sensorpriv3key)

    for sen3id in sensor3keypair[sensor3id]:
        print("Sensor 2 Unique ID:", sen3id)
        
    '''
    with open("/home/pi/Desktop/jsontest/sensor3.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/sensor3.json')
        table = db.table('sensor 3')
        db.insert_multiple([{'Sensor 3 Private key' : sensor3keypair[sensor3privatekey]}, {'Sensor 3 Public key' : sensor3keypair[sensor3publickey]}])
    
generatesensor3key()

