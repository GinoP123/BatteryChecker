#!/usr/bin/env python3

import re
import subprocess as sp
import settings
from datetime import datetime

output = sp.run("pmset -g batt", shell=True, capture_output=True).stdout.decode()
charging_status, battery_percentage = output.strip().split('\n')

charging_status = re.search("(?<=').*?(?=')", charging_status).group()
battery_percentage = int(re.search("\\S*(?=%)", battery_percentage).group(0))


if charging_status != "AC Power" and battery_percentage < settings.battery_percentage_threshold:
	sp.run(f'"{settings.create_event_path}" "Check Battery On Mac Server!!!" 0', shell=True)
	print("Battery Low")
else:
	print("Battery Fine/Charging")

