# TLSAES
 ampy --port COM6 --baud 115200 put C:\Users\mpkhs\PycharmProjects\CNfDA\test.py main.py

Installing micro python on ESP8266 NodeMCU:

1.
    download micropython from:
    https://micropython.org/download/esp8266/
    and the driver USB to UART Bridge:
    https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

2.
    install esptool:
        pip install esptool
    check if installed:
        esptool version

3.
    Find the port in device manager
    if no port, use cable not made for charging but for sending data

4.
    erase flash memory of ESP8266:
        esptool --port COM6 erase_flash

5.
    Install firmware:
    cd downloads
    esptool.py --port COM6 --baud 460800 write_flash --flash_size=detect 0 esp8266-20200911-v1.13.bin

    change esp8266-20200911-v1.13.bin according to what version of micropython was installed
