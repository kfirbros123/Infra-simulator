import logging
import json
import os
import subprocess
from src.machine import Machine, newMachine
from src.logger import logger

machines = []

#loads pre-existing machines to array
def json_to_machine():
    config_dir = "configs"
    for filename in os.listdir(config_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(config_dir, filename)
            with open(file_path, "r") as f:
                data = json.load(f)
                machines.append(Machine(name=data["name"],OS=data["OS"],CPU=data["CPU"],RAM=data["RAM"],storage=data["storage"],inEnv=data["inEnv"]))

def run_setup_script():
   try:
      logger.info("Starting Nginx Installer")
      subprocess.run(["sudo", "scripts/setup_nginx.sh"],check =True)
      logger.info("[INFO] Nginx installation conpleted.")
   except subprocess.CalledProcessError as e:
      logger.error(f"[ERROR] Failed to run Nginx installation due to Error: {e}")


def get_user_input():
   json_to_machine()
   while True:
      print("Current Machines:")
      for _machine in machines:
            print(f"{_machine.name}")
      usrInput=input("\n\nEnter New Machine Name To Create (or 'done' to finish):")
      if usrInput.lower() == 'done' :
         for _machine in machines:
            run_setup_script()
         break

      _machine=newMachine(usrInput)
      if _machine:
         machines.append(_machine)



get_user_input()






