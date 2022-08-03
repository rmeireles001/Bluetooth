#MAC Addr 1C:52:16:03:52:E2

import bluetooth

def scan():
	print("Scanning for bluetooth devices:")
	print("...............................")

	devices = bluetooth.discover_devices(duration = 20, lookup_names = True)

	number_devices = len(devices)

	print(str(number_devices)+" device(s) found")

	for addr, name in devices:
		print("\n")
		print("Device name: %s" %(name))
		print("MAC Address: %s" %(addr))

scan()