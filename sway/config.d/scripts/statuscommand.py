import re

from datetime import datetime
from psutil import disk_usage, sensors_battery, virtual_memory, sensors_temperatures
from psutil._common import bytes2human
from socket import gethostname
from subprocess import check_output
from sys import stdout
from time import sleep


status_command = []


def write(data):
    stdout.write('%s\n' % data)
    stdout.flush()

def refresh():
    disk = bytes2human(disk_usage('/').free)

    memory = virtual_memory()
    total_memory = bytes2human(memory.total)
    available_memory = bytes2human(memory.available)
    used_memory = bytes2human(memory.used)
    shared_memory = bytes2human(memory.shared)
    # memory = f'S: {shared_memory} A: {available_memory} U/T: {used_memory}/{total_memory}'
    memory = f'{shared_memory} | {available_memory} : {used_memory}/{total_memory}'

    with open("/sys/class/power_supply/BAT0/charge_full_design") as f:
        capacity = int(f.read())
    with open("/sys/class/power_supply/BAT0/charge_now") as f:
        current_charge = int(f.read())
    with open("/sys/class/power_supply/BAT0/charge_full") as f:
        current_capacity = int(f.read())

    status = ''
    battery_plugged = sensors_battery().power_plugged
    battery = round(current_charge * 100 / capacity, 2)

    if current_capacity == current_charge:
        status += 'F'

    if battery_plugged:
        status += 'C'
    else:
        status += 'D'

    if battery <= 20:
        status += 'L'

    sensor_temperatures = [(sensor.current, sensor.label) for sensor in sensors_temperatures()['dell_ddv'] if sensor.label in ["CPU", "Video", "Ambient"]]
    cpu_temperatures = ''.join([f'{temp}°C' for temp, label in sensor_temperatures if label == "CPU"])
    video_temperatures = ''.join([f'{temp}°C' for temp, label in sensor_temperatures if label == "Video"])
    ambient_temperatures = ''.join([f'{temp}°C' for temp, label in sensor_temperatures if label == "Ambient"])

    nmcli = check_output('nmcli device status', shell=True, encoding="utf-8") 
    wifi = re.findall(r'.*wlan0.*.wifi.*.connected.*', nmcli)[0].split()[3] or None
    ethernet = re.findall(r'.*enp0s20f03u3.*.ethernet.*.connected.*', nmcli) or None
    internet = None

    if ethernet is not None:
        internet = 'Ethernet'
    if wifi is not None and internet is not None:
        internet += f'/{wifi}'
    elif wifi is not None and internet is None and wifi != '--':
        internet = wifi
    else:
        internet = 'No Internet'
    internet = remove_ansi_escape(internet)

    date = datetime.now().strftime('%h. %d. %A %H:%M:%S')

    # Theme
    # SURFACE1, PINK, BASE = get_colors()
    # # END = "</span>"
    # END = "\033[0m"
    # SEPERATOR = f' {PINK}|{END} '
    write(f'{cpu_temperatures} : {video_temperatures} : {ambient_temperatures} | {disk} | {memory} | {internet} | {status} {battery}% | {date}')


def hex_to_rgb(hex):
    hex_value = hex.lstrip('#')
    return f'\033[38;2;{";".join([str(int(hex_value[i:i+2], 16)) for i in (0, 2, 4)])}m'


def remove_ansi_escape(string_with_ansi):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')  # Match ANSI escape codes
    return ansi_escape.sub('', string_with_ansi)


def get_colors():
    surface1 = hex_to_rgb("#45475a")
    pink = hex_to_rgb("#f5c2e7")
    base = hex_to_rgb("#1e1e2e")
    return surface1, pink, base

refresh()

