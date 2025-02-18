from tkinter import *
from tkinter import ttk
import serial

from data import data_struct

root = Tk() # create main root for gui
root.title("Project 2 GUI")

mainframe = ttk.Frame(root, padding="3 3 12 12") # create main frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # set grid layout onto frame
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

### labels ###

font = ("TkDefaultFont", 24, "bold")
padding = 10

## GPS ##

lat_label = ttk.Label(mainframe, font = font, padding = padding, text='Lattitude')
lat_label.grid(column=0, row=0)

long_label = ttk.Label(mainframe, font = font, padding = padding, text='Longitude')
long_label.grid(column=1, row=0)

elev_label = ttk.Label(mainframe, font = font, padding = padding, text='Elevation')
elev_label.grid(column=2, row=0)

num_sat_label = ttk.Label(mainframe, font = font, padding = padding, text='Num satellites')
num_sat_label.grid(column=3, row=0)

## IMU ##

# vel #

vel_x_label = ttk.Label(mainframe, font = font, padding = padding, text='Velocity: X')
vel_x_label.grid(column=0, row=2)

vel_y_label = ttk.Label(mainframe, font = font, padding = padding, text='Velocity: Y')
vel_y_label.grid(column=1, row=2)

vel_z_label = ttk.Label(mainframe, font = font, padding = padding, text='Velocity: Z')
vel_z_label.grid(column=2, row=2)

# acc #

acc_x_label = ttk.Label(mainframe, font = font, padding = padding, text='Acceleration: X')
acc_x_label.grid(column=0, row=4)

acc_y_label = ttk.Label(mainframe, font = font, padding = padding, text='Acceleration: Y')
acc_y_label.grid(column=1, row=4)

acc_z_label = ttk.Label(mainframe, font = font, padding = padding, text='Acceleration: Z')
acc_z_label.grid(column=2, row=4)

# mag #

mag_x_label = ttk.Label(mainframe, font = font, padding = padding, text='Mag field: X')
mag_x_label.grid(column=0, row=6)

mag_y_label = ttk.Label(mainframe, font = font, padding = padding, text='Mag field: Y')
mag_y_label.grid(column=1, row=6)

mag_z_label = ttk.Label(mainframe, font = font, padding = padding, text='Mag field: Z')
mag_z_label.grid(column=2, row=6)

### data display ####

data = data_struct

font = ("TkDefaultFont", 14)
padding = 0

## GPS ##

lat_data = ttk.Label(mainframe, font = font, padding = padding, text = data["GPS"]["lattitude"])
lat_data.grid(column=0, row=1)

long_data = ttk.Label(mainframe, font = font, padding = padding, text = data["GPS"]['longtiude'])
long_data.grid(column=1, row=1)

elev_data = ttk.Label(mainframe, font = font, padding = padding, text = data["GPS"]['elevation'])
elev_data.grid(column=2, row=1)

num_sat_data = ttk.Label(mainframe, font = font, padding = padding, text = data["GPS"]["num_satellites"])
num_sat_data.grid(column=3, row=1)

## IMU ##

# vel #

vel_x_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["velocity"])
vel_x_data.grid(column=0, row=3)

vel_y_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["velocity"])
vel_y_data.grid(column=1, row=3)

vel_z_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["velocity"])
vel_z_data.grid(column=2, row=3)

# acc #

acc_x_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["acceleration"])
acc_x_data.grid(column=0, row=5)

acc_y_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["acceleration"])
acc_y_data.grid(column=1, row=5)

acc_z_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["acceleration"])
acc_z_data.grid(column=2, row=5)

# mag #

mag_x_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["mag_field"])
mag_x_data.grid(column=0, row=7)

mag_y_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["mag_field"])
mag_y_data.grid(column=1, row=7)

mag_z_data = ttk.Label(mainframe, font = font, padding = padding, text = data["IMU"]["mag_field"])
mag_z_data.grid(column=2, row=7)

### buttons ###

running = False
status = StringVar()
status.set("Press start")

status_label = ttk.Label(mainframe, font = ("TkDefaultFont", 24, "bold"), padding = 10, text='Status')
status_label.grid(column=3, row=6)

status_data = ttk.Label(mainframe, font = font, padding = padding, textvariable = status)
status_data.grid(column=3, row=7)

def start():
    running = True
    status.set("Running")
    # serial_write(b'doesnt matter')

def stop():
    running = False
    status.set("Paused")
    # serial_write(b'doesnt matter')

start = ttk.Button(mainframe, text='Start', command = start)
start.grid(column=3, row=2)

stop = ttk.Button(mainframe, text='Stop', command = stop)
stop.grid(column=3, row=4)

### I/O with pico ###

serial_port = "/dev/cu.usbmodemXXXX"
# pico_serial = serial.Serial(serial_port)

def serial_read():
    return pico_serial.read()

def serial_write(data):
    pico_serial.write(data)

### main ###

gps_data = ''
imu_data = ''
while running:
    pass

root.mainloop()