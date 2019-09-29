#! /bin/sh
cd /home/pi/hack2019/RTEllipsoidFit
RTIMULibCal
mv /home/pi/hack2019/RTEllipsoidFit/RTIMULib.ini /home/pi/hack2019/scripts
python /home/pi/hack2019/scripts/forward.py
