import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json


def generatepillar1key():
    global keypair
    
    keypair = {}    

    checkpikey = []

    pillarid = 'Pillar_ID'
    pillarprivatekey = 'Pillar_privatekey'
    pillarpublickey = 'Pillar_publickey'
    pillarflag = 'Pillar_flag'          

    sensorid = 'sensor_ID'
    sensorprivatekey = 'sensor_privatekey'
    sensorpublickey = 'sensor_publickey'
    sensorflag = 'sensor_flag'

    lightid = 'light_ID'
    lightprivatekey = 'light_privatekey'
    lightpublickey = 'light_publickey'
    lightflag = 'light_flag'

    pillar2id = 'Pillar2_ID'
    pillar2privatekey = 'Pillar2_privatekey'
    pillar2publickey = 'Pillar2_publickey'
    pillar2flag = 'Pillar2_flag'

    pillar3id = 'Pillar3_ID'
    pillar3privatekey = 'Pillar3_privatekey'
    pillar3publickey = 'Pillar3_publickey'
    pillar3flag = 'Pillar3_flag'
    count = 0
    while (count <3):

        pikeys = libnacl.public.SecretKey()
    
        piprivkey = str(pikeys.sk)
        pipubkey = str(pikeys.pk)
        
        piunique_id = piprivkey + pipubkey

        piflag = "active"
         

        keypair.setdefault(pillarid,[])
        keypair.setdefault(pillarprivatekey,[])
        keypair.setdefault(pillarpublickey,[])
        keypair.setdefault(pillarflag,[])

        checkpikey.append(piprivkey)
        checkpikey.append(pipubkey)
        
        if not keypair.setdefault(pillarid):

            keypair[pillarid].append(piunique_id)
            keypair[pillarprivatekey].append(piprivkey)
            keypair[pillarpublickey].append(pipubkey)
            keypair[pillarflag].append(piflag)

            print("PILLAR 1 PRIVATE KEY", keypair[pillarprivatekey])
            print("PILLAR 1 PUBLIC KEY", keypair[pillarpublickey])
        
        else:
            for key in checkpikey: 
                keyoccurences=[index for index, value in enumerate(checkpikey) if value == key]
                if len(keyoccurences)>1:
                    check_pikey = libnacl.public.SecretKey()
                    checkpikeys_box = libnacl.public.Box(check_pikey.sk, check_pikey.pk)

                    check_piprivkey = str(check_pikey.sk)
                    check_pipubkey= str(check_pikey.pk)
                    check_piunid = check_pip
                    check_privkey + check_pipubkey
                    check_piflag = "active"

                    keypair[pillarid].append(check_piunid)
                    keypair[pillarprivatekey].append(check_piprivkey)
                    keypair[pillarpublickey].append(check_pipubkey)
                    keypair[pillarflag].append(check_piflag)

                    keyoccurences.pop()
                    [checkpikey.remove(key)for o in keyoccurences]
                    print("failed")
                    break;

            else:
                keypair[pillarid].append(piunique_id)
                keypair[pillarprivatekey].append(piprivkey)
                keypair[pillarpublickey].append(pipubkey)
                keypair[pillarflag].append(piflag)
                print("success")
                                
                                   
        count+=1 
    
    for pubkey in keypair[pillarpublickey]:
        print("Pillar 1 Public key: ",pubkey)

    for pikey in keypair[pillarprivatekey]:
        print("Pillar 1 Private key: ", pikey)
        
    for piid in keypair[pillarid]:
        print("Pillar 1 Unique ID: ", piid)
    '''    
    return keypair

    with open("/home/pi/Desktop/jsontest/pillar1.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/pillar1.json')
        table = db.table('PILLAR 1')
        db.insert_multiple([{'Private key' : keypair[pillarprivatekey], 'Public key' : keypair[pillarpublickey], 'Pillar ID' : keypair[pillarid], 'Pillar Flag': keypair[pillarflag]}])
    '''
generatepillar1key()
    
