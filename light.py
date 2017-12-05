import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatelightkey():

    global lightkeypair

    lightkeypair = {}
    
    checklightkey = []

    lightid = 'light_ID'
    lightprivatekey = 'light_privatekey'
    lightpublickey = 'light_publickey'
    lightflag = 'light_flag'
        
    count = 0
    while (count <64):

        lightkeys = libnacl.public.SecretKey()

        lightprivkey = str(lightkeys.sk)
        lightpubkey = str(lightkeys.pk)

        lightunique_id= lightprivkey + lightpubkey

        lightflag = "active"

        lightkeypair.setdefault(lightid,[])
        lightkeypair.setdefault(lightprivatekey,[])
        lightkeypair.setdefault(lightpublickey,[])
        lightkeypair.setdefault(lightflag,[])
        
        checklightkey.append(lightprivkey)
        checklightkey.append(lightpubkey)

        if not lightkeypair.setdefault(lightid):

            lightkeypair[lightid].append(lightunique_id)
            lightkeypair[lightprivatekey].append(lightprivkey)
            lightkeypair[lightpublickey].append(lightpubkey)
            lightkeypair[lightflag].append(lightflag)

            #print("PRIVKEYYYY", lightkeypair[lightprivatekey])
            print("LIGHT 1 PUBKEYYYY", lightkeypair[lightpublickey])
        
        else:
            for lightkey in checklightkey: 
                lightoccurences=[index for index, value in enumerate(checklightkey) if value == lightkey]
                if len(lightoccurences)>1:
                    check_lightkey = libnacl.public.SecretKey()
                    checklightkeys_box = libnacl.public.Box(check_lightkey.sk, check_lightkey.pk)

                    check_lightprivkey = str(check_lightkey.sk)
                    check_lightpubkey= str(check_lightkey.pk)
                    check_lightunid = check_lightprivkey + check_lightpubkey
                    check_lightflag = "active"

                    lightkeypair[lightid].append(check_lightunid)
                    lightkeypair[lightprivatekey].append(check_lightprivkey)
                    lightkeypair[lightpublickey].append(check_lightpubkey)
                    lightkeypair[lightflag].append(check_lightflag)

                    lightoccurences.pop()
                    [checklightkey.remove(lightkey)for o in lightoccurences]
                    print("failed")
                    break;

            else:
                lightkeypair[lightid].append(lightunique_id)
                lightkeypair[lightprivatekey].append(lightprivkey)
                lightkeypair[lightpublickey].append(lightpubkey)
                lightkeypair[lightflag].append(lightflag)
                print("success")
                                
        count+=1

    '''
    for lightpubkey in lightkeypair[lightpublickey]:
        print("Light 1 Public key:",lightpubkey)

    for lightkey in lightkeypair[lightprivatekey]:
        print("Light 1 Private key", lightkey)
   
    for liid in lightkeypair[lightid]:
        print("Light 1 Unique ID:",liid)
    
    '''
    with open("/home/pi/Desktop/jsontest/light.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/light.json')
        table = db.table('light')
        db.insert_multiple([{'Light 1 Private key' : lightkeypair[lightprivatekey]}, {'Light 1 Public key' : lightkeypair[lightpublickey]}])
    
     
generatelightkey()

