# Infra Simulator

Infra Simulator is a Python-based tool that interactively provisions virtual machine (VM) definitions and outputs them into a structured JSON file. It is designed to simulate infrastructure setup workflows by collecting machine specifications, validating them with Pydantic models, and preparing each VM with a simple post-provisioning script.

## Features

* **Dynamic VM creation**: The program prompts the user for machine details for each VM.
* **Input validation with Pydantic**: All fields are validated using Pydantic to ensure proper data types and constraints.
* **JSON output**: Once validated, VM definitions are saved into a JSON file.
* **Automatic nginx installation**: After provisioning, each machine triggers a script that installs and configures **nginx**. (theoretically)

## VM Fields Collected

For each machine, the program requests:

* **Machine Name** – Unique identifier for the VM.
* **Operating System** – Example: Ubuntu, Debian, CentOS, Windows.
* **CPU** – Number of virtual CPU cores.
* **RAM** – Memory size in GB.
* **Storage** – Disk allocation in GB.
* **Environment** – Example: dev, nonprod, prod.

Each of these values is validated using a Pydantic model to ensure correctness and prevent malformed data.

## Workflow

1. Run the script.
2. The program interactively asks for VM information.
3. Pydantic validates the entered fields.
4. Valid machine objects are appended to the JSON infrastructure file.
5. A post-provisioning script is executed to install **nginx** on each machine.(theoreticaly)

## Requirements

* Python 3.10+
* Create virtual env and pip install Pydantic



## Running the Program

```bash
python3 infra_simulator.py
```

Follow the prompts to add as many VMs as needed.

## JSON Output

The resulting files may look like:

```json
[
  {
    "name": "web-server-01",
    "os": "Ubuntu",
    "cpu": 4,
    "ram": 16,
    "storage": 100,
    "environment": "prod"
  }
]
```

## Script Execution (nginx Installation)

After each VM is successfully provisioned, the application runs a setup script that installs **nginx** and performs initial configuration.

Example steps performed:

* Update package lists
* Install nginx package
* Change html file and Start the nginx service

## Project Structure

```
infra-simulator/
|-- scripts/
|-- configs/
|-- logs/
|-- src/
|-- README.md
```


## Future Enhancements

* Cloud provider integration
* * get IP of actually provisioned machine
* The **nginx** will install on the new vm after creation using ip

