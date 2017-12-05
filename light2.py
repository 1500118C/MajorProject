import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json
               
def generatelight2key():

    global light2keypair

    light2keypair = {}
    
    checklight2key = []

    light2id = 'light2_ID'
    light2privatekey = 'light2_privatekey'
    light2publickey = 'light2_publickey'
    light2flag = 'light2_flag'
        
    count = 0
    while (count <64):

        light2keys = libnacl.public.SecretKey()

        light2privkey = str(light2keys.sk)
        light2pubkey = str(light2keys.pk)

        light2unique_id= light2privkey + light2pubkey

        light2flag = "active"

        light2keypair.setdefault(light2id,[])
        light2keypair.setdefault(light2privatekey,[])
        light2keypair.setdefault(light2publickey,[])
        light2keypair.setdefault(light2flag,[])
        
        checklight2key.append(light2privkey)
        checklight2key.append(light2pubkey)

        if not light2keypair.setdefault(light2id):

            light2keypair[light2id].append(light2unique_id)
            light2keypair[light2privatekey].append(light2privkey)
            light2keypair[light2publickey].append(light2pubkey)
            light2keypair[light2flag].append(light2flag)

            #print("PRIVKEYYYY", light2keypair[light2privatekey])
            print("LIGHT 2 PUBLIC KEY", light2keypair[light2publickey])
        
        else:
            for light2key in checklight2key: 
                light2occurences=[index for index, value in enumerate(checklight2key) if value == light2key]
                if len(light2occurences)>1:
                    check_light2key = libnacl.public.SecretKey()
                    checklight2keys_box = libnacl.public.Box(check_light2key.sk, check_light2key.pk)

                    check_light2privkey = str(check_light2key.sk)
                    check_light2pubkey= str(check_light2key.pk)
                    check_light2unid = check_light2privkey + check_light2pubkey
                    check_light2flag = "active"

                    light2keypair[light2id].append(check_light2unid)
                    light2keypair[light2privatekey].append(check_light2privkey)
                    light2keypair[light2publickey].append(check_light2pubkey)
                    light2keypair[light2flag].append(check_light2flag)

                    light2occurences.pop()
                    [checklight2key.remove(light2key)for o in light2occurences]
                    print("failed")
                    break;

            else:
                light2keypair[light2id].append(light2unique_id)
                light2keypair[light2privatekey].append(light2privkey)
                light2keypair[light2publickey].append(light2pubkey)
                light2keypair[light2flag].append(light2flag)
                print("success")
                                
        count+=1

    '''
    for light2pubkey in light2keypair[light2publickey]:
        print("Light 2 Public key:",light2pubkey)

    for light2key in light2keypair[light2privatekey]:
        print("Light 2 Private key", light2key)
   
    for li2id in light2keypair[light2id]:
        print("Light 2 Unique ID:",li2id)
     
    '''
    with open("/home/pi/Desktop/jsontest/light2.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/light2.json')
        table = db.table('light2')
        db.insert_multiple([{'Light 2 Private key' : light2keypair[light2privatekey]}, {'Light 2 Public key' : light2keypair[light2publickey]}])
    
generatelight2key()

