import board
import busio
import binascii
from digitalio import DigitalInOut
#
# NOTE: pick the import that matches the interface being used
#
# from adafruit_pn532.i2c import PN532_I2C
from adafruit_pn532.adafruit_pn532 import PN532
from adafruit_pn532.spi import PN532_SPI

#from adafruit_pn532.uart import PN532_UART

# I2C connection:
# i2c = busio.I2C(board.SCL, board.SDA)

# Non-hardware
#pn532 = PN532_I2C(i2c, debug=False)

# With I2C, we recommend connecting RSTPD_N (reset) to a digital pin for manual
# harware reset
# reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
# req_pin = DigitalInOut(board.D12)
# pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

# UART connection
#uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=100)
#pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print('Waiting for RFID/NFC card...')

def scan():
    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)
        print('.', end="")
        # Try again if no card is available.
        if uid is None:
            continue
        print('')
        hex_uid = format(binascii.hexlify(uid))
        return hex_uid
