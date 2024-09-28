# PRTG ZFS Health
Simple PRTG SSH Script Advanced sensor to monitor health of ZFS pools 

Documentation for this sensor type is available here: https://www.paessler.com/manuals/prtg/ssh_script_advanced_sensor

General guideline is to put the script in **/var/prtg/scriptsxml** on the target server.

The script uses a simple _zpool list_ command to poll health and utilization of all the pools on the system.

![Output example in PRTG](http://souslasurface.net/img/prtg-solaris.png)

The error and warning levels are hard-coded in the script at the moment and **should** be adjusted to your configurations.