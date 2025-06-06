from subprocess import run
from re import split
from time import sleep

#includes code from https://gist.github.com/logixism/613337a02f6638d31a42053fdb42fd35

def _exec_powershell(cmd):
        result = run(["powershell", "-Command", cmd], capture_output=True, text=True)

        if result.stderr != "":
            raise ValueError(result.stderr)
        else:
            return result.stdout
        
def install_audio_module():
      powershell_command = f"Install-Module -Name AudioDeviceCmdlets"
      _exec_powershell(powershell_command)
        
def _convert_value(value):
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.find("%") > 0:
            return float(value.replace("%", ""))
        else:
            return value
        
def _format_data(data):
        entries = split(r"\n\n+", data.strip())
        entry_dict = {}
        for entry in entries:
            lines = entry.split("\n")
            for line in lines:

                key, value = split(r"\s*:\s*", line)
                entry_dict[key.strip()] = _convert_value(value)
        return entry_dict
        
def get_default_playback_device():
        powershell_command = "Get-AudioDevice -Playback"
        data = _exec_powershell(f"{powershell_command}")
        return _format_data(data)

def get_default_recording_device():
        powershell_command = "Get-AudioDevice -Recording"
        data = _exec_powershell(f"{powershell_command}")
        return _format_data(data)

def set_active_device_by_id(device_id: str):
        powershell_command = f"""Set-AudioDevice -ID "{device_id}" -DefaultOnly"""
        _exec_powershell(powershell_command)

def set_active_communications_device_by_id(device_id: str):
        powershell_command = f"""Set-AudioDevice -ID "{device_id}" -CommunicationOnly"""
        _exec_powershell(powershell_command)

def sync_playback_device():
    default_playback_device = get_default_playback_device()
    if not default_playback_device["DefaultCommunication"]:
        set_active_communications_device_by_id(default_playback_device["ID"])
        print(f"Successfully set {default_playback_device["Name"]} as the default communications playback device")
    else:
        print(f"No changes")

def sync_recording_device():
    default_recording_device = get_default_recording_device()
    if not default_recording_device["DefaultCommunication"]:
        set_active_communications_device_by_id(default_recording_device["ID"])
        print(f"Successfully set {default_recording_device["Name"]} as the default communications recording device")
    else:
        print(f"No changes")



    
    
