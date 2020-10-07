import socket
socket.setdefaulttimeout(1)
scan=(input("masukkan ip address target:"))
daftar_port=[20,21,22,23,25,53,79,80,110,137,138,139,443,445,3306] # bisa di tambahkan portnya
print ("#####################################")

for port in daftar_port:
  socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  result=socket_obj.connect_ex((scan,int(port)))
  if result==0:
    print ("Terbuka port : " + str(port))
    socket_obj.close()
  else:
    print("Tertutup port : " + str(port))
    socket_obj.close()