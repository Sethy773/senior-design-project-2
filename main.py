from machine import Pin, UART, I2C, SPI, sdcard
import os 

### pin/port initialization ###

gps_scl_pin = 25 #integar value specifying pico pin
gps_sda_pin = 24
gps_i2c = I2C(0, scl = Pin(gps_scl_pin), sda = Pin(gps_sda_pin)) # set up gps i2c on bus 0

imu_scl_pin = 27 #integar value specifying pico pin
imu_sda_pin = 26
imu_i2c = I2C(1, scl = Pin(imu_scl_pin), sda = Pin(imu_sda_pin))  # set up imu i2c on bus 1

# check hco6 guide on canvas to get this working
# byte stuff is 8N1
radio_rx_pin = 2
radio_tx_pin = 1
radio_baud_rate = 9600 # from datasheet
radio_uart = UART(0, baudrate=9600, tx=Pin(radio_tx_pin), rx=Pin(radio_rx_pin))

# will show as /dev/cu.usbmodemXXXX on mac, /dev/ttyACM0 on windows
# use minicom to test, minicom -b 115200 -o -D /dev/tty.usbmodem0000000000001  on mac
gui_rx_pin = 7
gui_tx_pin = 6
gui_baud_rate = 9600 # default?
gui_uart = UART(1, baudrate=9600, tx=Pin(gui_tx_pin), rx=Pin(gui_rx_pin)) 

sd_mosi_pin = 15
sd_miso_pin = 16
sd_sck_pin = 14
sd_chip_select = 17
sd_spi = spi = SPI(0, sck = Pin(sd_sck_pin), mosi = Pin(sd_mosi_pin), miso = Pin(sd_miso_pin))

sd_card = SDCard(sd_spi, Pin(sd_chip_select, Pin.OUT))
vfs = os.VfsFat(sd_card) # maybe uos?
os.mount(vfs, "/sd")

### read/write functions ###

def uart_write(port, data): # port is the object, like "gui_uart"
    port.write(data) # turn data to bytes first?

def uart_read(port, bus): # bus 0 is radio, bus 1 is gui
    return port.read(bus)

def i2c_write(port, data):
    address = port.scan()
    port.writeto(address, data)

def i2c_read(port, num_bytes):
    address = port.scan()
    port.readfrom(address, num_bytes)

def sd_write(data):
    with open("/sd/data.txt", "w") as file:
        file.write(data)

def sd_read():
    with open("/sd/data.txt", "r") as file:
        return file.read()
        




