# 🔍 Port Scanner

A simple yet powerful command-line Port Scanner built with Python. Quickly scan single or multiple targets and discover open ports in no time.

## 🚀 Features

- Scan a single IP or hostname
- Scan multiple ports or port ranges
- Fast multithreaded scanning
- Results include open ports and optional service banner grabbing
- Lightweight and easy to use

## 📦 Requirements

- Python 3.6+
- Optional: `colorama` for colored terminal output
  

### Install dependencies:

1. Clone the repository:
   
   ```shell
   git clone https://github.com/Udit2073/DDoS-Tool
   
3. Navigate to the project directory:
   
   ```shell
   cd DDoS-Tool
   
5. Install the required python package:
   
   ```shell
   pip install -r requirements.txt
   

##  Usage
```bash
python port_scanner.py -t example.com
```


## Options   
Usage: port_scanner.py [-h] -t TARGET [-p PORTS] [-th THREADS] [--banner]

Optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP or hostname
  -p PORTS, --ports PORTS
                        Ports (e.g. 80,443 or 1-1000)
  -th THREADS, --threads THREADS
                        Number of threads (default: 50)
  --banner              Attempt to grab service banners



## Scan Multiple Ports
```bash
python port_scanner.py -t 192.168.1.1 -p 22,80,443
```


## Scan a port range
```bash
python port_scanner.py -t 10.0.0.1 -p 20-100
```


## Multithreaded scan
```bash
python port_scanner.py -t scanme.nmap.org -p 1-1024 -th 100
```


## ⚠️ Disclaimer
This tool is intended for educational purposes only. Do not use it on networks or systems without explicit permission.


## 📜 License
This project is licensed under the [LICENSE](https://github.com/Udit2073/Port-Scanner/blob/main/LICENSE).
  



   
   
