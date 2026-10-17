import docker

client = docker.from_env()
client.images.build(path=".", tag="flask-apparmor")

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

info = client.api.inspect_container(container.id)
print(f"AppArmor profile applied: {info['HostConfig']['SecurityOpt']}")

container.stop()
container.remove()
print("Container stopped and removed")