"""
Executable MicroPython Code:

Load into microcontroller as:
HwM_E2.py => main.py

Powered by YAKOTT
"""


"""
ESP32
Wi-Fi Fake Access Point

https://docs.micropython.org/en/latest/library/network.html
https://mpython.readthedocs.io/en/latest/library/micropython/network.html

Prompt: Write a script in MicroPython to create fake access points with an ESP32.
"""


# Packages


# Modules
# Network
import network
# uBinaASCII
import ubinascii as binascii
# Time
import utime as time


# Global variables
# Wait time in seconds
wait_time_s = 10


# Functions


# Classes


# Main
print("Wi-Fi Fake Access Point")
print()

# WLAN() => Instantiate a network interface object
#   network.AP_IF => Access point mode
#   network.STA_IF => Station client mode
ap = network.WLAN(network.AP_IF)

# Turn on Wi-Fi
print("Turn on Wi-Fi")
# active() => Activate/Deactivate the networt interface
#   True => Activate
#   False => Deactivate
ap.active(True)
print()

print("Device Information")
# decode() => Encodes the string to bytes using UTF-8 by default
# hexlify() => Return the hexadecimal representation of the binary data
print("  MAC Address: " + binascii.hexlify(ap.config('mac'), ':').decode())
# hostname() => Get or set the hostname that will identify this device on the network
#   parameter
#       name => Hostname
print("  Hostname: " + network.hostname())
# country() => Get or set the two-letter ISO 3166-1 Alpha-2 country code to be used for radio compliance
#   parameter
#       code => "EC"
print("  Country: " + network.country())
# phy_mode() => Get or set the PHY mode. Only with ESP8266
#   parameter
#       network.MODE_11B => IEEE 802.11b,
#       network.MODE_11G => IEEE 802.11g,
#       network.MODE_11N => IEEE 802.11n.
#print("  Mode: " + network.phy_mode())
print()

print("New Device Information")
# https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
# Apple, Inc.           18F643000001    Brian's iPhone
# Cisco Systems, Inc    18E728000001    router
mac_hexadecimal = "18F643000001"
# unhexlify() => Return the binary data representation by the hexadecimal string
mac_binary = binascii.unhexlify(mac_hexadecimal)
# config() => Get/Set general network interface parameters
#   parameter => Standar IP configuration
#       mac/'mac' => BSSID MAC address
#       essid/'essid' => Access point name
#       channel/'channel' => 2.4 GHz band
#           [1:13]
#       hidden/'hidden' => Whether SSID is hidden
#           ["Visible", "Hidden"]
#       authmode/'authmode' => Security protocol
#           ["AUTH_OPEN", "AUTH_WEP", "AUTH_WPA_PSK", "AUTH_WPA2_PSK", "AUTH_WPA_WPA2_PSK", "", "AUTH_MAX"]
#       password/'password' => Password
#       max_clients/'max_clients' => Clients numbers
#       txpower/'txpower' => TX power in dB
ap.config(mac=mac_binary)
network.hostname("Unknown")
network.country("EC")
#network.phy_mode(network.MODE_11G))
print("  MAC Address: " + binascii.hexlify(ap.config('mac'), ':').decode())
print("  Hostname: " + network.hostname())
print("  Country: " + network.country())
#print("  Mode: " + network.phy_mode())
print()

print("IP Information:")
# ifconfig() => Get/Set IP-level network interface parameters
#   ip => IP address
#   subnet_mask => Subnet mask
#   gateway => Gateway
#   dns_server => DNS server
print("  IP Address: " + ap.ifconfig()[0])
print("  Subnet Mask: " + ap.ifconfig()[1])
print("  IP Gateway: " + ap.ifconfig()[2])
print("  DNS Server: " + ap.ifconfig()[3])
print()

print("New IP Information:")
ip = "192.168.0.1"
subnet_mask = "255.255.255.0"
gateway = "192.168.0.1"
dns_server = "8.8.8.8"
ap.ifconfig((ip, subnet_mask, gateway, dns_server))
print("  IP Address: " + ap.ifconfig()[0])
print("  Subnet Mask: " + ap.ifconfig()[1])
print("  IP Gateway: " + ap.ifconfig()[2])
print("  DNS Server: " + ap.ifconfig()[3])
print()

essid_list = ["h4ck3r", "w0lf", "cyb3r", "1nf0s3c", "p1r4t", "s3cur1ty", "y4k0tt", "c0mput3r", "3sp", "m1cr0c0ntr0ll3r"]
password_list = ["12345678a", "12345678b", "12345678c", "12345678d", "12345678e", "12345678f", "12345678g", "12345678h", "12345678i", "12345678j"]
while True:
    for i in range(len(essid_list)):
        # config() => Get/Set general network interface parameters
        #   parameter => Standar IP configuration
        #       mac/'mac' => BSSID MAC address
        #       essid/'essid' => Access point name
        #       channel/'channel' => 2.4 GHz band
        #           [1:13]
        #       hidden/'hidden' => Whether SSID is hidden
        #           ["Visible", "Hidden"]
        #       authmode/'authmode' => Security protocol
        #           ["AUTH_OPEN", "AUTH_WEP", "AUTH_WPA_PSK", "AUTH_WPA2_PSK", "AUTH_WPA_WPA2_PSK", "", "AUTH_MAX"]
        #       password/'password' => Password
        #       max_clients/'max_clients' => Clients numbers
        #       txpower/'txpower' => TX power in dB
        ap.config(essid=essid_list[i], channel=3, hidden=False, authmode=network.AUTH_WPA_WPA2_PSK, password=password_list[i], max_clients=10)

        print("Access Point information")
        # decode() => Encodes the string to bytes using UTF-8 by default
        # hexlify() => Return the hexadecimal representation of the binary data
        print("  BSSID:", binascii.hexlify(ap.config('mac'), ':').decode())
        print("  ESSID:", ap.config('essid'))
        print("  Channel:", ap.config('channel'))
        print("  Hidden:", ap.config('hidden'))
        print("  Security protocol:", ap.config('authmode'))
        print("  Clients numbers:", ap.config('max_clients'))
        print()

        # sleep() => Wait time in seconds
        time.sleep(wait_time_s)

# Turn off Wi-Fi
print("Turn off Wi-Fi")
ap.active(False)
print()
