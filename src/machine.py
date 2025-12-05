
import json
from pydantic import BaseModel, ValidationError, field_validator
from src.logger import logger


class Machine(BaseModel):
    name: str
    OS: str
    CPU: int
    RAM: int
    storage: int
    inEnv: str    

#VALIDATORS
    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 20:
            raise ValueError(" Name cannot exceed 20 characters")
        return value

    @field_validator("OS")
    def validate_os(cls, value):
        if not (value.lower() == 'windows' or value.lower()== 'ubuntu'):
            raise ValueError(" OS must be ubuntu or windows")
        return value
    
    @field_validator("RAM")
    def validate_RAM(cls, value):
        if not ((value >= 1) and (value <=128)):
            raise ValueError("RAM range should be 1-128(GB)")
        return value

    @field_validator("CPU")
    def validate_CPU(cls, value):
        if not ((value >= 1) and (value <=128)):
            raise ValueError("CPU range should be 1-128(GB)")
        return value

    @field_validator("storage")
    def validate_storage(cls, value):
        if not((value >= 1) and (value <=1000)):
            raise ValueError("Strorage range should between 1gb to 1tb (1000gb)")
        return value

    @field_validator("inEnv")
    def validate_inEnv(cls, value):
        if not (value.lower() == 'prod' or value.lower()== 'nonprod' or value.lower()== "dev"):
            raise ValueError("existing environments: prod, nonprod, dev")
        return value


    def __str__(self):
        returnString= (f"{self.name}\n")
        _dict = self.toDict()
        for key in _dict:
            returnString = returnString + (f"{key} : {_dict[key]}\n")
        return returnString
    

    def toDict(self):
        return {
        "name" : self.name,
        "OS" : self.OS,
        "CPU" : self.CPU,
        "RAM" : self.RAM,
        "storage" : self.storage,
        "inEnv" : self.inEnv
        }
    

    def log_creation(self):
        logger.info(f"Successfuly created instance: {self.name} with parameters: {self.toDict()}")
  
    



#Method to create, save as json, and document a new machines creation and their errors
def newMachine(_name:str):
    _OS= input("Operating System: ")
    _CPU= input("CPU: ")
    _RAM= input("RAM in GB: ")
    _storage= input("Storage in GB: ")
    _inEnv= input("Environment: ")
    print(f"these values: {_name,_OS,_CPU,_RAM,_storage,_inEnv}")
    try:
        _machine = Machine(name=_name,OS=_OS,CPU=_CPU,RAM=_RAM,storage=_storage,inEnv=_inEnv)
        print(" User input is  valid :")
        _machine.log_creation()
        return _machine

    except ValidationError as err:
        print(f" Creation of {_name} machine config failed on Validation error :\n{err}")
        logger.error(f"Creation of {_name} machine config failed on Validation error :\n{err}")

