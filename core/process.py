from metadata import *
import yaml

class Process:

    def __init__(self,yaml):
        self.yaml = yaml

    def _yaml_to_dict(self):
        with open(self.yaml) as f:
            self.param = yaml.load(f, Loader=yaml.FullLoader)
    

    def _Get_User_info(self):
        ID = self.param['ID']
        NAME = self.param['NAME']

    def _Data(self):

        DATANAME :  self.param['DATANAME']
        COLNAME : ["sepal.length","sepal.width","petal.length","petal.width"]
TARGETNAME : ["variety"]
DATAINFO : None

        DATANAME = self.param['DATANAME']
        NAME = self.param['NAME']