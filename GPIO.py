import os,sys
import xml.etree.ElementTree as et
import logging

logging.basicConfig(level=logging.DEBUG,format = '%(levelname)s - %(asctime)s - %(message)s')
file_name = "configGPIO.xml"

def searchAndAssign(xmlSection,labelName):
    if xmlSection.find(labelName):
        logging.debug("{} was succesfully found in XML file".format(labelName))
        return config.find(labelName)    
    else:
        logging.error("There is an error loking for {} in XML file".format(labelName))
        exit(1)

try:
    tree = et.parse(file_name)
except:
    print("There is an error with XML file")
    exit(1)

config = tree.getroot()
buttons = searchAndAssign(config,"buttons")
