"""
Executable MicroPython Code:

Load into microcontroller as:
HwM_E1.py => main.py

Powered by YAKOTT
"""


"""
Disclaimer:
This project is for educational purposes only and should not be used for illegal or malicious activities. YAKOTT is not responsible for misuse of the information or tools provided in the project.
"""


"""
ESP32
WLAN Analyzer 2.4 GHz

https://docs.micropython.org/en/latest/library/network.html
https://mpython.readthedocs.io/en/latest/library/micropython/network.html

Prompt: Write a script in MicroPython to present available Wi-Fi networks around an ESP32.
"""


# Packages


# Modules
# Network
import network
# uBinaASCII
import ubinascii as binascii


# Global variables


# Functions


# Classes


# Main
print("WLAN Analyzer 2.4 GHz")
print()

# WLAN() => Instantiate a network interface object
#   network.AP_IF => Access point mode
#   network.STA_IF => Station client mode
station = network.WLAN(network.STA_IF)

# Turn on Wi-Fi
print("Turn on Wi-Fi")
# active() => Activate/Deactivate the networt interface
#   True => Activate
#   False => Deactivate
station.active(True)
print()

print("Status")
# status() => Query dynamic information of the network interface
#   response
#       1000 => STAT_IDLE
#       1001 => STAT_CONNECTING
#       202 => STAT_WRONG_PASSWORD
#       201 => STAT_NO_AP_FOUND
#       1010 => STAT_GOT_IP
#       203 => STAT_ASSOC_FAIL
#       200 => STAT_BEACON_TIMEOUT
#       204 => STAT_HANDSHAKE_TIMEOUT
#   parameter
#       network.AP_IF
#           'stations' => Devices connected
#       network.STA_IF
#           'rssi' => Signal meter
response_option = {"1000": "STAT_IDLE", "1001": "STAT_CONNECTING", "202": "STAT_WRONG_PASSWORD", "201": "STAT_NO_AP_FOUND", "1010": "STAT_GOT_IP", "203": "STAT_ASSOC_FAIL", "200": "STAT_BEACON_TIMEOUT", "204": "STAT_HANDSHAKE_TIMEOUT"}
response_value = station.status()
print(" ", response_option[str(response_value)])
print()

while True:
    # scan() => Scan for the available network services/connections
    #   parameter
    #       ssid => Access point name
    #       bssid => Access point MAC address
    #       channel => 2.4 GHz band
	#			[1:13]
    #       rssi => Signal meter
    #       security => Security protocol
	#			["AUTH_OPEN", "AUTH_WEP", "AUTH_WPA_PSK", "AUTH_WPA2_PSK", "AUTH_WPA_WPA2_PSK", "", "AUTH_MAX"]
    #       hidden => Whether SSID is hidden
	#			["Visible", "Hidden"]
    list_wlans = station.scan()

    # Print how many networks have been found
    # format() => Formats the specified value(s) and insert them inside the string's placeholder {}
    print("Found {} Wi-Fi networks:".format(len(list_wlans)))
    print()

    # Present all the networks
    item = 0
    for i in range(len(list_wlans)):
        # decode() => Encodes the string to bytes using UTF-8 by default
        # hexlify() => Return the hexadecimal representation of the binary data
        ssid = list_wlans[i][0].decode()
        bssid = binascii.hexlify(list_wlans[i][1], ':').decode()
        channel = list_wlans[i][2]
        rssi = list_wlans[i][3]

        security_option = ["AUTH_OPEN", "AUTH_WEP", "AUTH_WPA_PSK", "AUTH_WPA2_PSK", "AUTH_WPA_WPA2_PSK", "", "AUTH_MAX"]
        security_value = list_wlans[i][4]
        security = security_option[security_value]

        hidden_option = ["Visible", "Hidden"]
        hidden_value = list_wlans[i][5]
        hidden = hidden_option[hidden_value]

        item = item + 1
        print("  " + str(item) + ". " + ssid + ", " + bssid + ", " + str(channel) + ", " + str(rssi) + ", " + security + ", " + hidden)
    print()

# Turn off Wi-Fi
print("Turn off Wi-Fi")
station.active(False)
print()
