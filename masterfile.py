import libnacl.public
import libnacl.secret
import libnacl.utils
from tinydb import TinyDB, Query
from hashlib import sha256
import json

from pillar1 import keypair
from pillar1 import generatepillar1key
from pillar2 import pi2keypair
from pillar2 import generatepi2key
from pillar3 import pi3keypair
from pillar3 import generatepi3key

from sensorkey import sensorkeypair
from sensorkey import generatesensorkey      
from sensor2key import sensor2keypair
from sensor2key import generatesensor2key
from sensor3key import sensor3keypair
from sensor3key import generatesensor3key

from light import lightkeypair
from light import generatelightkey
from light2 import light2keypair
from light2 import generatelight2key
from light3 import light3keypair
from light3 import generatelight3key

pillarid = 'Pillar_ID'
pillarprivatekey = 'Pillar_privatekey'
pillarpublickey = 'Pillar_publickey'
pillarflag = 'Pillar_flag'
pillar2id = 'Pillar2_ID'
pillar2privatekey = 'Pillar2_privatekey'
pillar2publickey = 'Pillar2_publickey'
pillar2flag = 'Pillar2_flag'
pillar3id = 'Pillar3_ID'
pillar3privatekey = 'Pillar3_privatekey'
pillar3publickey = 'Pillar3_publickey'
pillar3flag = 'Pillar3_flag'

sensorid = 'sensor_ID'
sensorprivatekey = 'sensor_privatekey'
sensorpublickey = 'sensor_publickey'
sensorflag = 'sensor_flag'
sensor2id = 'sensor2_ID'
sensor2privatekey = 'sensor2_privatekey'
sensor2publickey = 'sensor2_publickey'
sensor2flag = 'sensor2_flag'
sensor3id = 'sensor3_ID'
sensor3privatekey = 'sensor3_privatekey'
sensor3publickey = 'sensor3_publickey'
sensor3flag = 'sensor3_flag'

lightid = 'light_ID'
lightprivatekey = 'light_privatekey'
lightpublickey = 'light_publickey'
lightflag = 'light_flag'
light2id = 'light2_ID'
light2privatekey = 'light2_privatekey'
light2publickey = 'light2_publickey'
light2flag = 'light2_flag'
light3id = 'light3_ID'
light3privatekey = 'light3_privatekey'
light3publickey = 'light3_publickey'
light3flag = 'light3_flag'


#PILLAR 1
with open("/home/pi/Desktop/jsontest/pillar1.json", 'w+'):
    db = TinyDB('/home/pi/Desktop/jsontest/pillar1.json')
    pillar1_table = db.table('PILLAR 1')
    pillar1_table.insert({"Table of IDs": {'Pillar 1 ID' : keypair[pillarid], 'Pillar 2 ID' : pi2keypair[pillar2id], 'Pillar 3 ID' : pi3keypair[pillar3id], 'Light 1 ID' : lightkeypair[lightid], 'Sensor 1 ID' : sensorkeypair[sensorid]}})
    pillar1_table.insert({"Pillar 1 Keys": {'Private key' : keypair[pillarprivatekey],'Public key' : keypair[pillarpublickey]}})
    pillar1_table.insert({"Light 1": {'Public key' : lightkeypair[lightpublickey]}})
    pillar1_table.insert({"Sensor 1": {'Public key' : sensorkeypair[sensorpublickey]}})
    pillar1_table.insert({"Adjacent Pillar 2": {'Public key' : pi2keypair[pillar2publickey]}})
    pillar1_table.insert({"Adjacent Pillar 3": {'Public key' : pi3keypair[pillar3publickey]}})


#PILLAR 2
with open("/home/pi/Desktop/jsontest/pillar2.json", 'w+'):
    db = TinyDB('/home/pi/Desktop/jsontest/pillar2.json')
    pillar2_table = db.table('PILLAR 2')
    pillar2_table.insert({"Table of IDs": {'Pillar 2 ID' : pi2keypair[pillar2id], 'Pillar 1 ID' : keypair[pillarid], 'Pillar 3 ID' : pi3keypair[pillar3id], 'Light 2 ID' : light2keypair[light2id], 'Sensor 2 ID' : sensor2keypair[sensor2id]}})
    pillar2_table.insert({"Pillar 2 Keys": {'Private key' : pi2keypair[pillar2privatekey],'Public key' : pi2keypair[pillar2publickey]}})
    pillar2_table.insert({"Light 2": {'Public key' : light2keypair[light2publickey]}})
    pillar2_table.insert({"Sensor 2": {'Public key' : sensor2keypair[sensor2publickey]}})
    pillar2_table.insert({"Adjacent Pillar 1": {'Public key' : keypair[pillarpublickey]}})
    pillar2_table.insert({"Adjacent Pillar 3": {'Public key' : pi3keypair[pillar3publickey]}})


#PILLAR 3
with open("/home/pi/Desktop/jsontest/pillar3.json", 'w+'):
    db = TinyDB('/home/pi/Desktop/jsontest/pillar3.json')
    pillar3_table = db.table('PILLAR 3')
    pillar3_table.insert({"Table of IDs": {'Pillar 3 ID' : pi3keypair[pillar3id], 'Pillar 1 ID' : keypair[pillarid], 'Pillar 2 ID' : pi2keypair[pillar2id], 'Light 3 ID' : light3keypair[light3id], 'Sensor 3 ID' : sensor3keypair[sensor3id]}})
    pillar3_table.insert({"Pillar 3 Keys": {'Private key' : pi3keypair[pillar3privatekey],'Public key' : pi3keypair[pillar3publickey]}})
    pillar3_table.insert({"Light 3": {'Public key' : light3keypair[light3publickey]}})
    pillar3_table.insert({"Sensor 3": {'Public key' : sensor3keypair[sensor3publickey]}})
    pillar3_table.insert({"Adjacent Pillar 1": {'Public key' : keypair[pillarpublickey]}})
    pillar3_table.insert({"Adjacent Pillar 2": {'Public key' : pi2keypair[pillar2publickey]}})

    
with open("/home/pi/Desktop/jsontest/masterfile.json", 'w+'):
    db = TinyDB('/home/pi/Desktop/jsontest/masterfile.json')
    master_table = db.table('MASTER TABLE')
    master_table.insert({"Pillar 1": {'Private key' : keypair[pillarprivatekey], 'Public key' : keypair[pillarpublickey],'Pillar ID' : keypair[pillarid], 'Pillar Flag': keypair[pillarflag]}})
    master_table.insert({"Pillar 2": {'Private key' : pi2keypair[pillar2privatekey],'Public key' : pi2keypair[pillar2publickey], 'Pillar ID' : pi2keypair[pillar2id], 'Pillar Flag': pi2keypair[pillar2flag]}})
    master_table.insert({"Pillar 3": {'Private key' : pi3keypair[pillar3privatekey],'Public key' : pi3keypair[pillar3publickey], 'Pillar ID' : pi3keypair[pillar3id], 'Pillar Flag': pi3keypair[pillar3flag]}})
    master_table.insert({"Sensor 1": {'Private key' : sensorkeypair[sensorprivatekey], 'Public key' : sensorkeypair[sensorpublickey], 'Sensor ID' : sensorkeypair[sensorid]}})
    master_table.insert({"Sensor 2": {'Private key' : sensor2keypair[sensor2privatekey], 'Public key' : sensor2keypair[sensor2publickey], 'Sensor ID' : sensor2keypair[sensor2id]}})
    master_table.insert({"Sensor 3": {'Private key' : sensor3keypair[sensor3privatekey], 'Public key' : sensor3keypair[sensor3publickey], 'Sensor ID' : sensor3keypair[sensor3id]}})
    master_table.insert({"Light 1": {'Private key' : lightkeypair[lightprivatekey], 'Public key' : lightkeypair[lightpublickey], 'Light ID' : lightkeypair[lightid]}})
    master_table.insert({"Light 2": {'Private key' : light2keypair[light2privatekey], 'Public key' : light2keypair[light2publickey], 'Light ID' : light2keypair[light2id]}})
    master_table.insert({"Light 3": {'Private key' : light3keypair[light3privatekey], 'Public key' : light3keypair[light3publickey], 'Light ID' : light3keypair[light3id]}})




    
