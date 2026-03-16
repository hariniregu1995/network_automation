import paramiko
import yaml

with open("inventory/devices.yaml") as f:
    data = yaml.safe_load(f)

device = data["devices"]["aws_server"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file(device["key_file"])

ssh.connect(
    hostname=device["host"],
    username=device["username"],
    pkey=key
)

stdin, stdout, stderr = ssh.exec_command("uptime")

print(stdout.read().decode())

ssh.close()