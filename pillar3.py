import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json

               
def generatepi3key():

    global pi3keypair
    
    pi3keypair = {}    

    checkpi3key = []
    
    pillar3id = 'Pillar3_ID'
    pillar3privatekey = 'Pillar3_privatekey'
    pillar3publickey = 'Pillar3_publickey'
    pillar3flag = 'Pillar3_flag'

    count = 0
    while (count <3):

        pi3keys = libnacl.public.SecretKey()

        pi3privkey = str(pi3keys.sk)
        pi3pubkey = str(pi3keys.pk)
        
        pi3unique_id = pi3privkey + pi3pubkey

        pi3flag = "active"
         

        pi3keypair.setdefault(pillar3id,[])
        pi3keypair.setdefault(pillar3privatekey,[])
        pi3keypair.setdefault(pillar3publickey,[])
        pi3keypair.setdefault(pillar3flag,[])

        checkpi3key.append(pi3privkey)
        checkpi3key.append(pi3pubkey)
        
        if not pi3keypair.setdefault(pillar3id):

            pi3keypair[pillar3id].append(pi3unique_id)
            pi3keypair[pillar3privatekey].append(pi3privkey)
            pi3keypair[pillar3publickey].append(pi3pubkey)
            pi3keypair[pillar3flag].append(pi3flag)

            #print("PRIVKEYYYY", pi3keypair[pillar3privatekey])
            print("PILLAR 3 PUBLIC KEY", pi3keypair[pillar3publickey])
        
        else:
            for pi3key in checkpi3key: 
                pi3occurences=[index for index, value in enumerate(checkpi3key) if value == pi3key]
                if len(pi3occurences)>1:
                    check_pi3key = libnacl.public.SecretKey()
                    checkpi3keys_box = libnacl.public.Box(check_pi3key.sk, check_pi3key.pk)

                    check_pi3privkey = str(check_pi3key.sk)
                    check_pi3pubkey= str(check_pi3key.pk)
                    check_pi3unid = check_pi3privkey + check_pi3pubkey
                    check_pi3flag = "active"

                    pi3keypair[pillar3id].append(check_pi3unid)
                    pi3keypair[pillar3privatekey].append(check_pi3privkey)
                    pi3keypair[pillar3publickey].append(check_pi3pubkey)
                    pi3keypair[pillar3flag].append(check_pi3flag)

                    pi3occurences.pop()
                    [checkpi3key.remove(pi3key)for o in pi3occurences]
                    print("failed")
                    break;

            else:
                pi3keypair[pillar3privatekey].append(pi3privkey)
                pi3keypair[pillar3publickey].append(pi3pubkey)
                pi3keypair[pillar3id].append(pi3unique_id)
                pi3keypair[pillar3flag].append(pi3flag)
                print("success")
                                
                                   
        count+=1
 

    for pi3pubkey in pi3keypair[pillar3publickey]:
        print("Pillar 3 Public key:",pi3pubkey)
    
    for pi3key in pi3keypair[pillar3privatekey]:
        print("Pillar 3 Private Key: ", pi3key)

    for pi3id in pi3keypair[pillar3id]:
        print("Pillar 3 Unique ID:", pi3id)

    '''
    with open("/home/pi/Desktop/jsontest/pillar3.json", 'w+'):
        db = TinyDB('/home/pi/Desktop/jsontest/pillar3.json')   
        table = db.table('Pillar 3')
        db.insert_multiple([{'Pillar 3 Private key' : pi3keypair[pillar3privatekey]}, {'Pillar 3 Public key' : pi3keypair[pillar3publickey]}])
        db.insert_multiple([{'Private key' : pi3keypair[pillar3privatekey],'Public key' : pi3keypair[pillar3publickey], 'Pillar ID' : pi3keypair[pillar3id], 'Pillar Flag': pi3keypair[pillar3flag]}])
    
    
    target = '/home/pi/Desktop/json/pillar3.json'
    sensor = '/home/pi/Desktop/json/sensor3.json'
    light = '/home/pi/Desktop/json/light3.json'

    t = open(target, 'a')
    t.write(open(sensor).read())
    t.write(open(light).read())
    t.close()
    '''

generatepi3key()
