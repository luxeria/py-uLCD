# print out a message what's going to happen 
print 'Starting initialisation for uLCD...'

# import the needed extensions for python
import serial
import time

# Function for writing a string to the display
def disp_string(text, col = 0, row = 0, font = 0, color = 0xffff, ):
    col = chr(col)
    row = chr(row)
    font = chr(font)
    color = chr(color / 256) + chr(color % 256)
    term = '\x00'
    stringtosend = 's' + col + row + font + color + text + term
    ser.write(stringtosend)
    time.sleep(0.08)
    return(0)

# open the serial connection (check with dmesg if it's not working)
ser = serial.Serial('/dev/ttyUSB0', 9600)

# write the command for AUTOBAUD by sending the character 'U'
ser.write('U')
time.sleep(1)

# write the command for ERASE by sending the character 'E'
ser.write('E')
time.sleep(1)

# write the welcome-scentense
# Byte 1: column = 0
# Byte 2: row = 0
# Byte 3: font = 0
# Byte 4 & 5: color = ffff
# Byte 5+: "string"
# Byte n: terminator = 0
ser.write('s\x00\x00\x03\xff\xffpy-uLCD\x00')
time.sleep(0.08)

ser.write('s\x00\x07\x00\xff\xffLicense:        GNU GPLv2\x00')
time.sleep(0.08)
ser.write('s\x00\x08\x00\xff\xffDeveloper:      nino.ninux@gmail.com\x00')
time.sleep(0.08)
ser.write('s\x00\x09\x00\xff\xffOrganisation:   LuXeria\x00')
time.sleep(0.08)
ser.write('s\x00\x0A\x00\xff\xffDevice:         4D Systems uLCD32-PT\x00')
time.sleep(0.08)
ser.write('s\x00\x0B\x00\xff\xffBaud Rate:      9600\x00')
time.sleep(0.08)
ser.write('s\x00\x0C\x00\xff\xffParity:         No\x00')
time.sleep(0.08)

ser.close()

# write out a message that the sequence is done
print 'Initialisation for uLCD is done.'
