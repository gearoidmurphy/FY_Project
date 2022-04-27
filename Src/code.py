import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import numpy
from scipy import ndimage
from datetime import datetime
# import smtplib, ssl
# import sqlite
# import colorDetection
import cv2 
import paho.mqtt.client as mqtt
import RFID_read
import yaml


with open("../FY_Project/config.yml", "r") as ymlfile: #opens the config file
    cfg = yaml.full_load(ymlfile) #Loads in the configurtionns from the yaml
config = cfg["settings"]
Display = config["Display"]
camera = cv2.VideoCapture(0)

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "lamenessdetection@gmail.com"  # Enter your address
# receiver_email = "gearoidmurphy2000@gmail.com"  # Enter receiver address
# password = 'cowscows12'
# context = ssl.create_default_context()

broker= config["broker"] # Sets the Broker address from config
def on_connect(client, userdata, flags, rc):
    print("Connected")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, 1883, 60)

counter = 0 

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
mlx_shape = (24,32) # mlx90640 shape
mlx_interp_val = 10 # interpolate # on each dimension
mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
                    mlx_shape[1]*mlx_interp_val) # new shape

file = open('data.txt', 'a')
if Display == 'True':
    fig = plt.figure(figsize=(12,7)) # start figure
    ax = fig.add_subplot(111) # add subplot
    fig.subplots_adjust(0.05,0.05,0.95,0.95) # get rid of unnecessary padding
    therm1 = ax.imshow(np.zeros(mlx_interp_shape),interpolation='none',
                    cmap=plt.cm.jet,vmin=0,vmax=60) # preemptive image
    cbar = fig.colorbar(therm1) # setup colorbar
    cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

    fig.canvas.draw() # draw figure to copy background
    ax_background = fig.canvas.copy_from_bbox(ax.bbox) # copy background
    fig.show() # show the figure before blitting

frame = np.zeros(mlx_shape[0]*mlx_shape[1]) # 768 pts
def plot_update():
    fig.canvas.restore_region(ax_background) # restore background
    mlx.getFrame(frame) # read mlx90640
    data_array = np.fliplr(np.reshape(frame,mlx_shape)) # reshape, flip data
    data_array = ndimage.zoom(data_array,mlx_interp_val) # interpolate
    therm1.set_array(data_array) # set data
    therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
    cbar.update_normal(therm1) # update colorbar range

    
    ax.draw_artist(therm1) # draw new thermal image
    fig.canvas.blit(ax.bbox) # draw background
    fig.canvas.flush_events() # show the new image
    #counter=counter+1
    #fig.show()
    return

def calcAverage(): # Calculates the average temperature 
    hightemps = 0
    counter = 0
    # print(frame)
    for h in range(24):
        for w in range(32):
            t = frame[h * 32 + w]
            if t > 24:
                hightemps = hightemps+t
                counter = counter + 1
    aveageOfHightemps = hightemps/counter
    return aveageOfHightemps

t_array = []
while True:
    t1 = time.monotonic() # for determining frame rate
    try:
        counter=counter+1
        if Display == "True":
            plot_update() # update plot
        averageTemp = calcAverage()
    except:
        continue
    # approximating frame rate
    # t_array.append(time.monotonic()-t1)
    # if len(t_array)>10:
    #     t_array = t_array[1:] # recent times for frame rate approx
    # print('Frame Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
    print('Average foot Temperature: '+ str(averageTemp))
    # print(counter)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    file.write(dt_string+'\t'+'Average Temperature: ' + str(averageTemp)+'\n')
    file.flush()
    if counter >= 20:
        tagnumber = 0
        tagnumber = RFID_read.getTagNumber()
        if averageTemp > LamenessTempPoint:
            print(str(tagnumber))
            client.publish(str(tagnumber), payload=averageTemp)
    #         with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #             server.login(sender_email, password)
    #             message = """\
    # Subject: Lameness Reading Automated 

    # Hi There,

    # The folowing reading was taken at """+dt_string+""" :
    #                 Average Temperature: """+str(averageTemp)+"""
    #                 """
    #             server.sendmail(sender_email, receiver_email, message)
    #             print('Sucessfully Sent')
                
            # id = sqlite.getNextID()
            # sqlite.addToDatabase(str(id),str(tagnumber),str(averageTemp),dt_string)
            counter = 0