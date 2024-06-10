.. include:: /include/include.rst

Documentation for the WiThrotle protocol library - WiThrottleProtocol
=====================================================================

.. toctree::
  :maxdepth: 4
  :hidden:

  WiThrottle protocol library <self>
  library

WiThrottle protocol library
---------------------------

This library implements the WiThrottleProtocol (as used in JMRI, the |DCC-EX| |EX-CS| and manya other DCc Command Stations), allowing a device to connect to the server and act as a client (such as a hardware based throttle).

The implementation of this library is tested on ESP32 based devices running the Arduino framework. There's nothing in here that's specific to the ESP32, and little of Arduino that couldn't be replaced as needed.

Credits
-------

The original version of the code in this library is taken directly from the WiThrottle library by **Copyright © 2018-2019 Blue Knobby Systems Inc.** and additioanl changes by lucadentella.
The rest of the code has been developed by Peter Akers (Flash62au).

-----

Differences from the original library
=====================================

 - Removed dependencies with external libraries (Chrono.h, ArduinoTime.h, TimeLib.h) 
 - Added NullStream class to disable (by default) logging
 - Changed begin() method to setLogStream()
 - Added a setter method for delegate class: setDelegate()
 - Added the ability to parse roster messages and to receive the roster list via delegate class
 
Differences from the lucadentella version of the library
========================================================

 - Added the trademark changes from the original library
 - supports multi-throttle commands (max 6)  (Added in version 1.1.0)
 - Support added for on-the-fly consists
 - Support added for turnouts/points
 - Support added for routes
 - Heartbeat sends the device name, which forces the WiThrottle server to respond (used to confirm it is still connected)
 - minimum time separation/delay between commands sent (introduced in v1.1.7)
 - bug fixes