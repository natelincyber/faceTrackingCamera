from ipwebcam import IPWEBCAM

ipcam = IPWEBCAM('192.168.0.180:8080')


res = ipcam.resolutions["3"]
print(res[0:3])
