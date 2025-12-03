import logging
import json
import subprocess
from src.machine import Machine, newMachine
from src.logger import logger



def run_setup_script():
   try:
      subprocess.run(["bash", "scripts/setup_nginx.sh"],check =True)
      print("[INFO] Nginx installation conpleted.")
   except subprocess.CalledProcessError as e:
      print(f"[ERROR] Failed to install Nginx: {e}")


def get_user_input():
   machines = []
   while True:
      print("Current Machines:")
      for _machine in machines:
            print(f"{_machine.name}")
      usrInput=input("\n\nEnter New Machine Name To Create (or 'done' to finish):")
      if usrInput.lower() == 'done' :
         break

      _machine=newMachine(usrInput)
      if _machine:
         machines.append(_machine)




get_user_input()






