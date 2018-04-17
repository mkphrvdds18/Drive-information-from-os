
"""
print all the drive letter for this system

"""

import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print('Available drives on this system are: ', drives)

import wmi
# 1st error - wmi not found; need to install by 'pip install wmi'
# / 1000000 #for Mb space

c = wmi.WMI ()
for d in c.Win32_LogicalDisk():
	x = round(int(d.FreeSpace) / 1000000000)
	y = round(int(d.Size) / 1000000000)
	
	print( d.Caption, 'Used Space:',x,'GB', 'Total Disk Space:',y,'GB', d.DriveType)
	

import win32api
import win32file

# define all the drive type information here
#
DRIVE_TYPES = """
0 	Unknown
1 	No Root Directory
2 	Removable Disk (USB)
3 	Local Disk (HDD)
4 	Network Drive
5 	Compact Disc
6 	RAM Disk
"""

# below gives the location - 0,1,2,3.. drive_types[2]=USB
# GetLogicalDriveStrings method will give a long information 

drive_types = dict((int (i), j) for (i, j) in (l.split ("\t") for l in DRIVE_TYPES.splitlines () if l))

drives = (drive for drive in win32api.GetLogicalDriveStrings ().split ("\000") if drive)
print("")

for drive in drives:
  vol_info = win32api.GetVolumeInformation(drive) # issue is here , why iy has to letter not variable
  print ("Drive name:", drive, "Vol name:", vol_info[0], drive_types[win32file.GetDriveType (drive)])
  
