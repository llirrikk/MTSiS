import telnetlib


HOST = "172.17.9.151"
PORT = 4010
FILEPAHT = "commands.txt"


def to_bytes(line):
    return f"{line}\n".encode("utf-8")

    
def send_commands(host: str, port: int, commands: list[str]) -> None:
    with telnetlib.Telnet(host, port, timeout=5) as session:
        for command in commands:
            print("IN:", command.rstrip("\n\r"))
            session.write(to_bytes(command))
            output = session.read_until(b"$ ", timeout=1).decode('utf-8')
            print("OUT:", output)
            print()
            
    
def make_commands(filepath: str) -> list[str]:
    with open(filepath) as file:
        commands = [line.rstrip() for line in file]
    return commands


        
if __name__ == "__main__":
    commands = make_commands(FILEPAHT)
    send_commands(HOST, PORT, commands)
