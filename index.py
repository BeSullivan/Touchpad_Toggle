import subprocess

# to find your touchpad id use "xinput list" in command line

deviceId = '11'
enableCmd= 'xinput set-prop ' + deviceId + ' \"Device Enabled\" 1'
disableCmd = 'xinput set-prop ' + deviceId + ' \"Device Enabled\" 0'

getState = 'xinput list-props ' + deviceId + ' | grep \"Device Enabled\"'

stateText = subprocess.check_output(getState ,shell = True).decode("utf-8").strip()
# stateText is like "Device Enabled (163):	1" as enable or "Device Enabled (163):	0" as disable
state = stateText[ len(stateText) - 1 ]

if state == '1':
    subprocess.call(disableCmd ,shell = True)
else:
    subprocess.call(enableCmd ,shell = True)


