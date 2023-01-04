import paramiko
import subprocess
import pytest
import sys


server_ip = "192.168.1.102"
port = 22
password = "lab7-server"
username = "lab7-server"


@pytest.fixture(scope="function")
def server():
    ssh = paramiko.SSHClient()
    print("Opened SSH connection")
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server_ip, port=port, username=username, password=password)
        print(f"Connected to {server_ip}")
        # -1 automatically close server after first connection
        stdin, stdout, stderr = ssh.exec_command("iperf3 -s -1")
        # ToDo: recheck how to wait completing of command
        stdin.close()
        print(f"Created iperf server on {server_ip}")
    except paramiko.AuthenticationException:
        print(f"Authentication failed when connecting to {server_ip}")
        sys.exit(1)
    finally:
        ssh.close()
        print("Closed SSH connection")


@pytest.fixture(scope="function")
def client():
    return subprocess.run(["iperf3", "-c", server_ip, "--json"], capture_output=True, text=True)