from scapy.all import *
import sys

def findIP(s):
    out_s = ""
    for i in s:
       if i == "." or i.isnumeric():
           out_s+=i
    return out_s       


TIMEOUT = 2
conf.verb = 0
timetl = 1

if len(sys.argv) == 2:
 dst_ip = sys.argv[1]
elif len(sys.argv) > 2 and sys.argv[2] == "-a":
    dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=sys.argv[1]))
    answer = sr1(dns_req, verbose=0)
    answer = findIP(answer[DNS].summary())
    dst_ip = answer
else:
    print("error")
    exit()

while(1): 
 packet = IP(dst=dst_ip, ttl=timetl)/ICMP()
 reply = sr1(packet, timeout=TIMEOUT)

 if not (reply is None):
         print(timetl,":",reply.src)
         if reply.src == dst_ip:
            break         

 else:
         print(timetl,": *")
        


 timetl+=1
