import xml.etree.ElementTree as et
import logging,os
from gpiozero import Button,LED 
from prettytable import PrettyTable
from time import sleep

logging.basicConfig(level=logging.ERROR,format = '%(levelname)s - %(asctime)s - %(message)s')
file_name = "/home/pi/Documents/residencias/configGPIO.xml"

def searchAndAssign(xmlSection,labelName):
    """
    This function is used to search and especific label in 
    XML file, if the label is found, it's returned as argument,
    if label is noth found, an error showed
    
    Input:
        xmlSection - This is a XML section where the specific label will be searched
        labelName  - Label that we want to search in XML file
    
    Output:
        Labels group that are in specified Label
    """
    if xmlSection.findall(labelName):
        if xmlSection.find(labelName):
            logging.debug("{} was succesfully found as labels group in XML file".format(labelName))
            return xmlSection.find(labelName)    
        elif xmlSection.findtext(labelName):
            logging.debug("{} was succesfully found as label in XML file".format(labelName))
            return xmlSection.findtext(labelName)    
    else:
        logging.error("There is an error loking for {} in XML file".format(labelName))
        exit(1)

def monitorButtons(buttons,iterations=1):
    """
    Funtion used to print buttons state with a PrettyTable format

    Input:
        buttons              - Buttons dictionary
        iterations(optional) - number of times that you want to show states
    """
    for i in range(iterations):
        if iterations != 1:         os.system("clear")
 
        buttonsTable = PrettyTable()
        buttonsTable.field_names = ["Button Name","State"]
        for i in range(len(buttons)):
            buttonsTable.add_row(["Button {}:".format(i),buttons[i].is_pressed])
        print(buttonsTable)
        sleep(.1)

def ledsDemo(leds):
    for led in leds:
        led.off()
    
    for led in leds:
        led.on() 
        sleep(0.1)

    for led in leds:
        led.off()
        sleep(0.1)

try:
    tree = et.parse(file_name)
except:
    print("There is an error with XML file")
    exit(1)

configXML  = tree.getroot()

#########################################################################
#            Reading GPIO Buttons config from xml file                  #
#########################################################################
buttonsXML = searchAndAssign(configXML,"buttons")
buttons = [Button(int(searchAndAssign(buttonsXML,"button0"))),
           Button(int(searchAndAssign(buttonsXML,"button1"))),
           Button(int(searchAndAssign(buttonsXML,"button2")))]

#########################################################################
#              Reading GPIO LEDs config from xml file                   #
#########################################################################
ledsXML = searchAndAssign(configXML,"leds")
leds = [LED(int(searchAndAssign(ledsXML,"led0"))),
        LED(int(searchAndAssign(ledsXML,"led1"))),
        LED(int(searchAndAssign(ledsXML,"led2"))),
        LED(int(searchAndAssign(ledsXML,"led3")))]
