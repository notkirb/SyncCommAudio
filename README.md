# SyncCommAudio

SyncCommAudio is a Windows service written in Python that fixes an issue I have with default audio devices in Windows, the way the default audio device can be different from the default communication device. This service works by checking if the default communication device is different from the audio device and then setting the default communication device to the same as the default audio device. It fixes the issue with Discord and other chatting apps not using the correct default audio device. 

## Installation

An automated installer is planned, but is not yet ready. To install SyncCommAudio, you need to clone the repository, install the requirements, and run the installation command. This code snipped assumes you installed Python using [Chocolatey](https://community.chocolatey.org/packages/python). If you have not installed Python through Chocolatey, install it from [https://www.python.org/](https://www.python.org/) or from Chocolatey by running `choco install python --pre`.
```
git clone https://github.com/notkirb/SyncCommAudio/
cd SyncCommAudio
C:\Python313\python.exe service.py install
```

NOTE: Make sure you are NOT using Python from the Windows Store. The Windows Store version does not support services, and therefore cannot be used for SyncCommAudio. You can install it from [https://www.python.org/](https://www.python.org/) or from [Chocolatey](https://community.chocolatey.org/packages/python) by running `choco install python --pre` assuming Chocolatey is installed on your system.
