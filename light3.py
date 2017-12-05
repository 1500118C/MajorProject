import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatelight3key():
    
    global light3keypair

    light3keypair = {}
    
    checklight3key = []

    light3id = 'light3_ID'
    light3privatekey = 'light3_privatekey'
    light3publickey = 'light3_publickey'
    light3flag = 'light3_flag'
        
    count = 0
    while (count <64):

        light3keys = libnacl.public.SecretKey()
        
        light3privkey = str(light3keys.sk)
        light3pubkey = str(light3keys.pk)

        light3unique_id= light3privkey + light3pubkey

        light3flag = "active"

        light3keypair.setdefault(light3id,[])
        light3keypair.setdefault(light3privatekey,[])
        light3keypair.setdefault(light3publickey,[])
        light3keypair.setdefault(light3flag,[])
        
        checklight3key.append(light3privkey)
        checklight3key.append(light3pubkey)

        if not light3keypair.setdefault(light3id):

            light3keypair[light3id].append(light3unique_id)
            light3keypair[light3privatekey].append(light3privkey)
            light3keypair[light3publickey].append(light3pubkey)
            light3keypair[light3flag].append(light3flag)

            #print("PRIVKEYYYY", light3keypair[light3privatekey])
            print("LIGHT 2 PUBLIC KEY", light3keypair[light3publickey])
        
        else:
            for light3key in checklight3key: 
                light3occurences=[index for index, value in enumerate(checklight3key) if value == light3key]
                if len(light3occurences)>1:
                    check_light3key = libnacl.public.SecretKey()
                    checklight3keys_box = libnacl.public.Box(check_light3key.sk, check_light3key.pk)

                    check_light3privkey = str(check_light3key.sk)
                    check_light3pubkey= str(check_light3key.pk)
                    check_light3unid = check_light3privkey + check_light3pubkey
                    check_light3flag = "active"

                    light3keypair[light3id].append(check_light3unid)
                    light3keypair[light3privatekey].append(check_light3privkey)
                    light3keypair[light3publickey].append(check_light3pubkey)
                    light3keypair[light3flag].append(check_light3flag)

                    light3occurences.pop()
                    [checklight3key.remove(light3key)for o in light3occurences]
                    print("failed")
                    break;

            else:
                light3keypair[light3id].append(light3unique_id)
                light3keypair[light3privatekey].append(light3privkey)
                light3keypair[light3publickey].append(light3pubkey)
                light3keypair[light3flag].append(light3flag)
                print("success")
                                
        count+=1

    '''
    for light3pubkey in light3keypair[light3publickey]:
        print("Light 3 Public key:",light3pubkey)

    for light3key in light3keypair[light3privatekey]:
        print("Light 3 Private key", light3key)
   
    for li3id in light3keypair[light3id]:
        print("Light 3 Unique ID:",li3id)

    '''
    with open("/home/pi/Desktop/jsontest/light3.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/light3.json')
        table = db.table('light 3')
        db.insert_multiple([{'Light 3 Private key' : light3keypair[light3privatekey]}, {'Light 3 Public key' : light3keypair[light3publickey]}])
 
    
generatelight3key()

