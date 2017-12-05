import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatesensorkey():

    global sensorkeypair

    sensorkeypair = {}
    
    checksensorkey = []

    sensorid = 'sensor_ID'
    sensorprivatekey = 'sensor_privatekey'
    sensorpublickey = 'sensor_publickey'
    sensorflag = 'sensor_flag'
        
    count = 0
    while (count <16):

        sensorkeys = libnacl.public.SecretKey()

        sensorprivkey = str(sensorkeys.sk)
        sensorpubkey = str(sensorkeys.pk)

        sensorunique_id= sensorprivkey + sensorpubkey

        sensorflag = "active"

        sensorkeypair.setdefault(sensorid,[])
        sensorkeypair.setdefault(sensorprivatekey,[])
        sensorkeypair.setdefault(sensorpublickey,[])
        sensorkeypair.setdefault(sensorflag,[])
        
        checksensorkey.append(sensorprivkey)
        checksensorkey.append(sensorpubkey)

        if not sensorkeypair.setdefault(sensorid):

            sensorkeypair[sensorid].append(sensorunique_id)
            sensorkeypair[sensorprivatekey].append(sensorprivkey)
            sensorkeypair[sensorpublickey].append(sensorpubkey)
            sensorkeypair[sensorflag].append(sensorflag)

            #print("PRIVKEYYYY", sensorkeypair[sensorprivatekey])
            print("SENSOR 1 PUBKEYYYY", sensorkeypair[sensorpublickey])
        
        else:
            for sensorkey in checksensorkey: 
                sensoroccurences=[index for index, value in enumerate(checksensorkey) if value == sensorkey]
                if len(sensoroccurences)>1:
                    check_sensorkey = libnacl.public.SecretKey()
                    checksensorkeys_box = libnacl.public.Box(check_sensorkey.sk, check_sensorkey.pk)

                    check_sensorprivkey = str(check_sensorkey.sk)
                    check_sensorpubkey= str(check_sensorkey.pk)
                    check_sensorunid = check_sensorprivkey + check_sensorpubkey
                    check_sensorflag = "active"

                    sensorkeypair[sensorid].append(check_sensorunid)
                    sensorkeypair[sensorprivatekey].append(check_sensorprivkey)
                    sensorkeypair[sensorpublickey].append(check_sensorpubkey)
                    sensorkeypair[sensorflag].append(check_sensorflag)

                    sensoroccurences.pop()
                    [checksensorkey.remove(sensorkey)for o in sensoroccurences]
                    print("failed")
                    break;

            else:
                sensorkeypair[sensorid].append(sensorunique_id)
                sensorkeypair[sensorprivatekey].append(sensorprivkey)
                sensorkeypair[sensorpublickey].append(sensorpubkey)
                sensorkeypair[sensorflag].append(sensorflag)
                print("success")
                                
        count+=1

    '''
    for sensorpubkey in sensorkeypair[sensorpublickey]:
        print("Sensor 1 Public key:",sensorpubkey)
    
    for sensorprivkey in sensorkeypair[sensorprivatekey]:
        print("Sensor 1 Private key:", sensorprivkey)

    for senid in sensorkeypair[sensorid]:
        print("Sensor 1 Unique ID:", senid)
 
    '''
    with open("/home/pi/Desktop/jsontest/sensor.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/sensor.json')
        table = db.table('sensor')
        db.insert_multiple([{'Sensor 1 Private key' : sensorkeypair[sensorprivatekey]}, {'Sensor 1 Public key' : sensorkeypair[sensorpublickey]}])
    
generatesensorkey()



