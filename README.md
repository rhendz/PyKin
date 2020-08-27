# PyKin
Raspberry Pi hardware hack that tracks patient mobility

## Inspiration
We have had many friends in the medical field and other friends who've been injured and needed to seek out medical treatment. Many said it was hard to measure their progress as they progressed through their sessions. We thought this would be an interesting project/tool that could possibly be used to help both the medical professionals and their patients to keep track and monitor their progress!

## What it does
PyKin helps measure the mobility of a patient by track an individual's body part (joints, arms, legs, etc) and recording their range of motion. This data is then sent via Bluetooth to our user interface, for both the patient and doctor to see, and the range of motion is converted to a graph to visually interpret their mobility and compare it to previous progress.

## How we built it
Our prototype is based around a 9-axis IMU that we had modified (solder) to attach to our breadboard. The breadboard was then bridged with a cobbler cable to our Raspberry Pi 3 B that would send the sensor's data via Bluetooth to our UI. Our UI would then catch that data and convert it the data to graph whichever limb or joint we were testing at the time. 

## Challenges we ran into
Trying to set up two way communication via Bluetooth had been difficult and had been more time consuming than we had anticipated. Also the documentation for our IMU was poor and we had difficult time finding libraries compatible with our Pi due to it being mainly used for Arduino based projects. Finally, as team of two we had essentially split the work load for one of us to work on front end and the other back end. This caused issues when it came time to merge the two ends together!

## Accomplishments that we're proud of and what we learned
We are proud that we were able to finish a workable prototype and were able to begin the testing of a handful of limbs. This was a first for us in terms of soldering, Bluetooth programming, and the configuring of actual hardware. We were extremely proud that we are able to learn all this within the time frame of the Hackathon!

## What's next for PyKin
We both have agreed that we wouldn't mind to continue the development of this project if we research more into the prospects of its actual usability in the medical field! 
