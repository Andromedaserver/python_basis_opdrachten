import psutil

ifcs = psutil.net_if_addrs()
IPs = []

for ifc in ifcs:
    for snic in ifcs[ifc]:
        IPs.append(snic.address)
#        IPs.append(snic.address)

print(IPs[4])