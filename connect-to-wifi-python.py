import pywifi
from pywifi import const

def connect_to_wifi(ssid, password):
    profile = pywifi.Profile()  # Create a new profile
    profile.ssid = ssid  # Set the SSID of the network

    profile.auth = const.AUTH_ALG_OPEN  # Set the authentication algorithm
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Set the Wi-Fi encryption type
    profile.cipher = const.CIPHER_TYPE_CCMP  # Set the cipher type
    profile.key = password  # Set the Wi-Fi password
    wifi = pywifi.PyWiFi()  # Create an instance of PyWiFi
    for iface in wifi.interfaces():
        print(iface.name())
        iface.disconnect()
        iface.remove_all_network_profiles()  # Remove any existing profiles
        tmp_profile = iface.add_network_profile(profile)  # Add the new profile
        iface.connect(tmp_profile)  # Connect to the network
        # Wait for the connection to be established
        print("Connected to", ssid)
        

wifi_ssid = "your_ssid_here"
wifi_password = "the_password_here"

connect_to_wifi(wifi_ssid, wifi_password)
