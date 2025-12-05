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

#Runs script and pushes output and errors to log
#Need both in try and except incase an error doesn't cause the script to fail (double brackets)
def run_setup_script():
   try:
      logger.info("Starting Nginx Installer")
      result = subprocess.run(["sudo", "scripts/setup_nginx.sh"],check =True, capture_output=True, text=True)
      if result.stdout:
         print(result.stdout)
         logger.info(result.stdout)
      if result.stderr:
         logger.error(result.stderr)
      logger.info("[INFO] Nginx installation conpleted.")

   except subprocess.CalledProcessError as e:
      logger.error(f"[ERROR] Failed to run Nginx installation due to Error: {e}")
      if e.stdout:
         logger.info(e.stdout)
         print(e.stdout)
      if e.stderr:
         print(e.stderr)
         logger.error(e.stderr)

      


def get_user_input():
   logger.info("STARTING INFRASTRUCTURE SIMULATOR")
   logger.info("Loading pre-existing machines...")
   try:
      json_to_machine()
      logger.info("SUCCESFULY loaded pre-existing machines")
   except FileNotFoundError as e:
      logger.error(f"Path does not exist, error: \n{e}")
   except PermissionError as e:
      logger.error(f"Permission denied, with error: \n{e}")

   while True:
      print("Current Machines:")
      for _machine in machines:
            print(f"{_machine.name}")
      usrInput=input("\n\nEnter New Machine Name To Create (or 'done' to finish):")
      if usrInput.lower() == 'done' :
         print("Before exiting, infra-simulator will install nginx ")
         for _machine in machines:
            run_setup_script()
         print("Exiting Infra-Simulator Application")
         logger.info("Exiting Infra-Simulator Application")
         break
      logger.info("Starting Creation of New Machine")
      _machine=newMachine(usrInput)
      if _machine:
         machines.append(_machine)
         with open(f'configs/{_machine.name}-instance.json', 'w') as json_file:
            json.dump( _machine.toDict(), json_file, indent=4)
         logger.info(f"Config file generated: configs/{_machine.name}-instance.json (machine: {_machine.name}).")



get_user_input()






