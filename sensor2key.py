import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatesensor2key():

    global sensor2keypair

    sensor2keypair = {}
    
    checksensor2key = []

    sensor2id = 'sensor2_ID'
    sensor2privatekey = 'sensor2_privatekey'
    sensor2publickey = 'sensor2_publickey'
    sensor2flag = 'sensor2_flag'
        
    count = 0
    while (count <16):

        sensor2keys = libnacl.public.SecretKey()
       
        sensor2privkey = str(sensor2keys.sk)
        sensor2pubkey = str(sensor2keys.pk)

        sensor2unique_id= sensor2privkey + sensor2pubkey

        sensor2flag = "active"

        sensor2keypair.setdefault(sensor2id,[])
        sensor2keypair.setdefault(sensor2privatekey,[])
        sensor2keypair.setdefault(sensor2publickey,[])
        sensor2keypair.setdefault(sensor2flag,[])
        
        checksensor2key.append(sensor2privkey)
        checksensor2key.append(sensor2pubkey)

        if not sensor2keypair.setdefault(sensor2id):

            sensor2keypair[sensor2id].append(sensor2unique_id)
            sensor2keypair[sensor2privatekey].append(sensor2privkey)
            sensor2keypair[sensor2publickey].append(sensor2pubkey)
            sensor2keypair[sensor2flag].append(sensor2flag)

            #print("PRIVKEYYYY", sensor2keypair[sensor2privatekey])
            print("SENSOR 2 PUBLIC KEY", sensor2keypair[sensor2publickey])
        
        else:
            for sensor2key in checksensor2key: 
                sensor2occurences=[index for index, value in enumerate(checksensor2key) if value == sensor2key]
                if len(sensor2occurences)>1:
                    check_sensor2key = libnacl.public.SecretKey()
                    checksensor2keys_box = libnacl.public.Box(check_sensor2key.sk, check_sensor2key.pk)

                    check_sensor2privkey = str(check_sensor2key.sk)
                    check_sensor2pubkey= str(check_sensor2key.pk)
                    check_sensor2unid = check_sensor2privkey + check_sensor2pubkey
                    check_sensor2flag = "active"

                    sensor2keypair[sensor2id].append(check_sensor2unid)
                    sensor2keypair[sensor2privatekey].append(check_sensor2privkey)
                    sensor2keypair[sensor2publickey].append(check_sensor2pubkey)
                    sensor2keypair[sensor2flag].append(check_sensor2flag)

                    sensor2occurences.pop()
                    [checksensor2key.remove(sensor2key)for o in sensor2occurences]
                    print("failed")
                    break;

            else:
                sensor2keypair[sensor2id].append(sensor2unique_id)
                sensor2keypair[sensor2privatekey].append(sensor2privkey)
                sensor2keypair[sensor2publickey].append(sensor2pubkey)
                sensor2keypair[sensor2flag].append(sensor2flag)
                print("success")
                                
        count+=1

    '''
    for sensor2pubkey in sensor2keypair[sensor2publickey]:
        print("Sensor 2 Public key:",sensor2pubkey)
    
    for sensorpriv2key in sensor2keypair[sensor2privatekey]:
        print("Sensor 2 Private key:", sensorpriv2key)

    for sen2id in sensor2keypair[sensor2id]:
        print("Sensor 2 Unique ID:", sen2id)
    '''
    with open("/home/pi/Desktop/jsontest/sensor2.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/sensor2.json')
        table = db.table('sensor 2')
        db.insert_multiple([{'Sensor 2 Private key' : sensor2keypair[sensor2privatekey]}, {'Sensor 2 Public key' : sensor2keypair[sensor2publickey]}])

    
generatesensor2key()

