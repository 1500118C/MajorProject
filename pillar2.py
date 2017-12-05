import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json

def generatepi2key():
    
    global pi2keypair
    
    pi2keypair = {}    

    checkpi2key = []
    
    pillar2id = 'Pillar2_ID'
    pillar2privatekey = 'Pillar2_privatekey'
    pillar2publickey = 'Pillar2_publickey'
    pillar2flag = 'Pillar2_flag'

    sensor2id = 'sensor2_ID'
    sensor2privatekey = 'sensor2_privatekey'
    sensor2publickey = 'sensor2_publickey'
    sensor2flag = 'sensor2_flag'

    light2id = 'light2_ID'
    light2privatekey = 'light2_privatekey'
    light2publickey = 'light2_publickey'
    light2flag = 'light2_flag'

    pillarid = 'Pillar_ID'
    pillarprivatekey = 'Pillar_privatekey'
    pillarpublickey = 'Pillar_publickey'
    pillarflag = 'Pillar_flag'

    pillar3id = 'Pillar3_ID'
    pillar3privatekey = 'Pillar3_privatekey'
    pillar3publickey = 'Pillar3_publickey'
    pillar3flag = 'Pillar3_flag'

    count = 0
    while (count <3):

        pi2keys = libnacl.public.SecretKey()
       
        pi2privkey = str(pi2keys.sk)
        pi2pubkey = str(pi2keys.pk)
        
        pi2unique_id = pi2privkey + pi2pubkey

        pi2flag = "active"
         

        pi2keypair.setdefault(pillar2id,[])
        pi2keypair.setdefault(pillar2privatekey,[])
        pi2keypair.setdefault(pillar2publickey,[])
        pi2keypair.setdefault(pillar2flag,[])

        checkpi2key.append(pi2privkey)
        checkpi2key.append(pi2pubkey)
        
        if not pi2keypair.setdefault(pillar2id):

            pi2keypair[pillar2id].append(pi2unique_id)
            pi2keypair[pillar2privatekey].append(pi2privkey)
            pi2keypair[pillar2publickey].append(pi2pubkey)
            pi2keypair[pillar2flag].append(pi2flag)

            #print("PILLAR 2 PRIVATE PRIVATE KEY", pi2keypair[pillar2privatekey])
            print("PILLAR 2 PUBLIC KEY ", pi2keypair[pillar2publickey])
        
        else:
            for pi2key in checkpi2key: 
                pi2occurences=[index for index, value in enumerate(checkpi2key) if value == pi2key]
                if len(pi2occurences)>1:
                    check_pi2key = libnacl.public.SecretKey()
                    checkpi2keys_box = libnacl.public.Box(check_pi2key.sk, check_pi2key.pk)

                    check_pi2privkey = str(check_pi2key.sk)
                    check_pi2pubkey= str(check_pi2key.pk)
                    check_pi2unid = check_pi2privkey + check_pi2pubkey
                    check_pi2flag = "active"

                    pi2keypair[pillar2id].append(check_pi2unid)
                    pi2keypair[pillar2privatekey].append(check_pi2privkey)
                    pi2keypair[pillar2publickey].append(check_pi2pubkey)
                    pi2keypair[pillar2flag].append(check_pi2flag)

                    pi2occurences.pop()
                    [checkpi2key.remove(pi2key)for o in pi2occurences]
                    print("failed")
                    break;

            else:
                pi2keypair[pillar2id].append(pi2unique_id)
                pi2keypair[pillar2privatekey].append(pi2privkey)
                pi2keypair[pillar2publickey].append(pi2pubkey)
                pi2keypair[pillar2flag].append(pi2flag)
                print("success")
                                
                                   
        count+=1

        
    for pi2pubkey in pi2keypair[pillar2publickey]:
        print("Pillar 2 Public key:",pi2pubkey)
    
    for pi2key in pi2keypair[pillar2privatekey]:
        print("Pillar 2 Private key:",pi2key)

    for pi2id in pi2keypair[pillar2id]:
        print("Pillar 2 Unique ID:",pi2id)

    '''    
    return pi2keypair
    

    with open("/home/pi/Desktop/jsontest/pillar2.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/pillar2.json')
        table = db.table('Pillar 2')
        db.insert_multiple([{'Private key' : pi2keypair[pillar2privatekey],'Public key' : pi2keypair[pillar2publickey], 'Pillar ID' : pi2keypair[pillar2id], 'Pillar Flag': pi2keypair[pillar2flag]}])
    

def save2json():

    pi2keypair = generatepi2key()
    
    pillarid = 'Pillar_ID'
    pillarprivatekey = 'Pillar_privatekey'
    pillarpublickey = 'Pillar_publickey'
    pillarflag = 'Pillar_flag'
    
    pillar2id = 'Pillar2_ID'
    pillar2privatekey = 'Pillar2_privatekey'
    pillar2publickey = 'Pillar2_publickey'
    pillar2flag = 'Pillar2_flag'

    sensor2id = 'sensor2_ID'
    sensor2privatekey = 'sensor2_privatekey'
    sensor2publickey = 'sensor2_publickey'
    sensor2flag = 'sensor2_flag'

    light2id = 'light2_ID'
    light2privatekey = 'light2_privatekey'
    light2publickey = 'light2_publickey'
    light2flag = 'light2_flag'
    
    with open("/home/pi/Desktop/json/pillar2.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/json/pillar2.json')
        table = db.table('HUNGRY')
        db.insert_multiple([{'Pillar 2 Private key' : pi2keypair[pillar2privatekey],'Pillar 2 Public key' : pi2keypair[pillar2publickey]}])
        db.insert_multiple([{'Light 2 Public key' : light2keypair[light2publickey]}])
        db.insert_multiple([{'Sensor 2 Public key' : sensor2keypair[sensor2publickey]}])
        db.insert_multiple([{'Pillar 1 Private key' : keypair[pillarprivatekey],'Pillar 1 Public key' : keypair[pillarpublickey]}])
    
save2json()
'''
generatepi2key()

