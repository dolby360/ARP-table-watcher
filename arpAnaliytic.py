import io
import json
import os
from utility import *

class arpAnaliytics():


    def __init__(self):
        self.check_if_file_is_exist_if_not_creat()

                
    def updateDataBase(self,listOf_ip_and_mac):
        pass


    def check_if_file_is_exist_if_not_creat(self):
        path_to_analiytic_json = os.path.dirname(os.path.abspath(__file__)) + '/ARPanaliytic.json'
        log(path_to_analiytic_json)

        if os.path.isfile(path_to_analiytic_json) and os.access(path_to_analiytic_json, os.R_OK):
            # checks if file exists
            log ("File exists and is readable")
        else:
            log ("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(path_to_analiytic_json, 'ARPanaliytic.json'), 'w') as db_file:
            
               db_file.write(json.dumps({}))