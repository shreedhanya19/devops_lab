import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)
print(f"Container started: {container.short_id}")

exit_code, output = container.exec_run("cat /etc/passwd")
print(f"Read /etc/passwd -> Exit Code {exit_code}, Output: {output.decode().strip()}")

exit_code, output = container.exec_run("/bin/bash -c 'echo hi'")
print(f"Execute /bin/bash -> Exit Code {exit_code}, Output: {output.decode().strip()}")

container.stop()
container.remove()
print("Container stopped and removed")