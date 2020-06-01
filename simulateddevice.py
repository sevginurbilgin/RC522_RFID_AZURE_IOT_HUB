# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time
import threading
from pirc522 import RFID
import signal
import RPi.GPIO as GPIO 
 
# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse


rdr = RFID()
util = rdr.util()
util.debug = True

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")
 

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=Raspb.azure-devices.net;DeviceId=Raspberry;SharedAccessKey=o/T8UwpNRM3sbT3LaxaHa/83bVi37RLVSGYbgSlSkic="

# Define the JSON message to send to IoT Hub.
kart_uid = 0
mes_id =  0

MSG_TXT = '{{"messageId" : "{mes_id}" , "Personel_Id": "{kart_uid}"}}'

INTERVAL = 1

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


def device_method_listener(device_client):
    global INTERVAL
    while True:
        method_request = device_client.receive_method_request()
        print (
            "\nMethod callback called with:\nmethodName = {method_name}\npayload = {payload}".format(
                method_name=method_request.name,
                payload=method_request.payload
            )
        )
        if method_request.name == "SetTelemetryInterval":
            try:
                INTERVAL = int(method_request.payload)
            except ValueError:
                response_payload = {"Response": "Invalid parameter"}
                response_status = 400
            else:
                response_payload = {"Response": "Executed direct method {}".format(method_request.name)}
                response_status = 200
        else:
            response_payload = {"Response": "Direct method {} not defined".format(method_request.name)}
            response_status = 404

        method_response = MethodResponse(method_request.request_id, response_status, payload=response_payload)
        device_client.send_method_response(method_response)



def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        # Start a thread to listen 
        device_method_thread = threading.Thread(target=device_method_listener, args=(client,))
        device_method_thread.daemon = True
        device_method_thread.start()

        while True:
            # This loop checks for chips. If one is near it will get the UID
            try:
           
              while True:
           
                 global mes_id     
                 rdr.wait_for_tag()
                 (error, data) = rdr.request()
                 if not error:
                  print("\nKart Algilandi!")
                  (error, uid) = rdr.anticoll()
                 if not error:
                  # Print UID
                  kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
                  print(kart_uid)
                  time.sleep(2)  
                  mes_id+=1
                  msg_txt_formatted = MSG_TXT.format(mes_id=mes_id,kart_uid=kart_uid)
                  message = Message(msg_txt_formatted)
                   # Send the message.
                  print( "Sending message: {}".format(message) )
                  client.send_message(message)
                  print( "Message sent" )
                  time.sleep(INTERVAL)

            except KeyboardInterrupt:
              GPIO.cleanup()   
             

    except KeyboardInterrupt:
      print ( "IoTHubClient sample stopped" ) 
       

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #2 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
