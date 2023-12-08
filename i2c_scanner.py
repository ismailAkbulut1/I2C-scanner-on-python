from machine import I2C, Pin

i2c = I2C(1, scl=Pin(19), sda=Pin(18))  # Örneğin, Pico'da I2C portlarını belirtin

devices = i2c.scan()

if len(devices) == 0:
    print("Hiçbir cihaz bulunamadı!")
else:
    print("Bulunan cihazların adresleri:")
    for device in devices:
        print(hex(device))
