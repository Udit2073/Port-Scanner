import socket
from tqdm import tqdm

target = input("Enter the target IP address or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in tqdm(range(start_port, end_port + 1)):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
        break
    except socket.gaierror:
        print("Hostname could not be resolved.")
        break
    except socket.error:
        print("Couldn't connect to server.")
        break
