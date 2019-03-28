from scripts import lcddriver
import subprocess
from time import sleep 

loadingChars =  [".","..","..."]

lcd = lcddriver.lcd()
lcd.lcd_display_string("{}Welcome BORRA!!".format(" "*2),1)
sleep(2)

ipFound = False
i=0
searchingCount = 0
while not ipFound:
    lcd.lcd_clear()
    IP = str(subprocess.check_output("hostname -I", shell = True ),'utf').split(" ")[0]
    lcd.lcd_display_string("Searching IP {}".format(loadingChars[i]),1)
    searchingCount+=1
    if searchingCount == 50:
        break
    i+=1
    if i == 3: i=0

    if IP.find(".") >= 0:
        lcd.lcd_clear()
        lcd.lcd_display_string("IP found !!",1) 
        lcd.lcd_display_string("IP {}".format(IP),3)
        ipFound = True
    sleep(.5)

if not ipFound:
    lcd.lcd_clear()
    lcd.lcd_display_string("IP was not Found :c",1)

exit(0)
