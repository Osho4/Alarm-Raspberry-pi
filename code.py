import paho.mqtt.client as mq
import ssl
import random
import datetime
rootca=r"C:\Users\USER\Desktop\certificate\AmazonRootCa1.pem.txt"
certficate=r"C:\Users\USER\Desktop\certificate\a836e9172f-certificate.pem.crt"
keyfile=r"C:\Users\USER\Desktop\certificate\a836e9172f-private.pem.key"

c=mq.Client()

c.tls_set(rootca,certfile=certficate,keyfile=keyfile,cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)
c.connect('arn:aws:iot:ap-northeast-2:729760633731:thing/Thing1',8883)


def onc(c,userdata,flag,rc):
	print("Connected to AWS successfully ",rc)
	c.subscribe("mytopic/sidiot")
def onm(c,userdata,msg):
	m=msg.payload.decode()
	
        
    
	print(m)
c.on_connect=onc
c.on_message=onm
c.loop_forever()
