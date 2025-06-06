import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import synccommaudio
import time

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "SyncCommAudioService"
    _svc_display_name_ = "SyncCommAudio Service"
    _svc_description_ = "Fix Windows communication devices becoming unsynced from default devices"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isStopped = True
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.isStopped = False
        self.main()

    def main(self):
        while True: 
            if not self.isStopped:
                time.sleep(2)
                synccommaudio.sync_playback_device()
                synccommaudio.sync_recording_device() 


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)