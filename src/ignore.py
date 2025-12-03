
import json
from pydantic import BaseModel, ValidationError, field_validator
template_string=""""
 {
    "Machine Name" : {{ input.name | tojason }}
    "OS" : {{ input.OS | tojason }}
    "CPU": {{ input.CPU | tojason }}
    "RAM": {{ input.RAM | tojason }}
 }   
 """

class test(BaseModel):
    name: str
    OS: str
    CPU: int
    RAM: int
    storage: int
    inEnv: str  

    def toJson(self):
        with open(f'configs/{self.name}-instance.json', 'w') as json_file:
            json.dump( self.toDict(), json_file, indent=4)
    

    def toDict(self):
        return {
        "name" : self.name,
        "OS" : self.OS,
        "CPU" : self.CPU,
        "RAM" : self.RAM,
        "storage" : self.storage,
        "inEnv" : self.inEnv
        }


    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 20:
            #logger.error("user input exceeds 20 characters")
            raise ValueError(" Name cannot exceed 20 characters")
        return value

    @field_validator("OS")
    def validate_os(cls, value):
        if not (value.lower() == 'windows' or value.lower()== 'ubuntu'):
            #logger.error("User input does not match known OS")
            raise ValueError(" OS must be ubuntu or windows")
        return value
    
    @field_validator("RAM")
    def validate_RAM(cls, value):
        if not ((value >= 1) and (value <=128)):
            #logger.error("Value for RAM not in correct range")
            raise ValueError("RAM range should be 1-128(GB)")
        return value

        
    @field_validator("CPU")
    def validate_CPU(cls, value):
        if not ((value >= 1) and (value <=128)):
            #logger.error("Value for CPU not in correct range")
            raise ValueError("CPU range should be 1-128(GB)")
        return value

    @field_validator("storage")
    def validate_storage(cls, value):
        if not((value >= 1) and (value <=1000)):
            #logger.error("Storage value not in correct range")
            raise ValueError("Strorage range should between 1gb to 1tb (1000gb)")
        return value

    @field_validator("inEnv")
    def validate_inEnv(cls, value):
        if not (value.lower() == 'prod' or value.lower()== 'nonprod' or value.lower()== "dev"):
            #logger.error("Inputed Environment does not exist")
            raise ValueError("existing environments: prod, nonprod, dev")
        return value
   


try:
    test1 = test(name="correct",OS="ubuntu",RAM=4,CPU=4,storage=10,inEnv="prod")
    print(" User input is  valid :")

except ValidationError as err:
    print(" Validation error :")
    print(err)
try:
    test2 = test(name="incorrect_OS",OS= "ubuntu",RAM=4,CPU=4,storage=1000,inEnv="prod")
    print(" User input is  valid :")

except ValidationError as err:
    print(" Validation error :")
    print("try agine")
    print(err)
    

class ignore_this(BaseModel):
    def editMode(self):
        user_input: str
        while True:
            print(f"Editing machine: {self.name}\nchoose attribute to change")
            print(self)
            user_input= input("To quit write done: ")

            if user_input in self.machine_data :
                newValue= input(f"old value: {self.user_input}\nnew value for {user_input}: ")
                self.machine_data[user_input] = newValue
                self.toJson()
            elif user_input == "done":
                break
            else:
                print(f"The attribute {user_input} does not exist")



