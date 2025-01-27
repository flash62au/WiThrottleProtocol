# WiThrottle<sup>TM</sup> network protocol library

This library implements the WiThrottle protocol (as used in JMRI and other servers), allowing an device to connect to the server and act as a client (such as a dedicated fast clock device or a hardware based throttle).

The implementation of this library is tested on ESP32 based devices running the Arduino framework.   There's nothing in here that's specific to the ESP32, and little of Arduino that couldn't be replaced as needed.

Refer to https://flash62au.github.io/WiThrottleProtocol/index.html for additional information.

## Basic Design Principles

First of all, this library implements the WiThrottle protocol in a non-blocking fashion.  After creating a WiThrottleProtocol object, you set up various necessities (like the network connection and a debug console) (see [Dependency Injection][depinj]).   Then call the ```check()``` method as often as you can (ideally, once per invocation of the ```loop()``` method) and the library will manage the I/O stream, reading in command and calling methods on the [delegate] as information is available.

These patterns (Dependency Injection and Delegation) allow you to keep the different parts of your sketch from becoming too intertwined with each other.  Nothing in the code that manages the pushbuttons or speed knobs needs to have any detailed knowledge of the WiThrottle network protocol.

## Differences in the lucadentella version from the original library by David Zuhn

https://github.com/davidzuhn/WiThrottleProtocol

 - Removed dependencies with external libraries (Chrono.h, ArduinoTime.h, TimeLib.h) 
 - Added NullStream class to disable (by default) logging
 - Changed begin() method to setLogStream()
 - Added a setter method for delegate class: setDelegate()
 - Added the ability to parse roster messages and to receive the roster list via delegate class
 
 ## Differences in this version from the lucadentella version of the library

 https://github.com/lucadentella/WiThrottle

 - Added the trademark changes from the original library
 - Support multi-throttle commands (max 6)  (Added in version 1.1.0)
 - Support added for on-the-fly consists
 - Support added for turnouts/points
 - Support added for routes
 - Heartbeat sends the device name, which forces the WiThrottle server to respond (used to confirm it is still connected)
 - minimum time separation/delay between commands sent (introduced in v1.1.7)
 - Support for broadcast messages and alerts (introduced in v1.1.12)
 - Added logging levels (introduced in v1.1.18/19)
 - Lots of bug fixes

## Included examples

### WiThrottleProtocol_Basic

Basic example to implement a WiThrottleProtocol client and connect to a server (with static IP).

Change the WiFi settings and enter the IP address of the computer running JMRI (or other WiThrottle server):
```
const char* ssid = "MySSID";
const char* password =  "MyPWD";
IPAddress serverAddress(192,168,1,1);
int serverPort = 12090;
```
Compile and run, you should see a new client connected in JMRI:

![](https://github.com/flash62au/WiThrottleProtocol/raw/master/images/basic-example.jpg)

### WiThrottleProtocol_Delegate

Example to show how to implement a delegate class to handle callbacks.

Compile and run, you should see in Serial monitor the server version, printed by ```void receivedVersion(String version)``` method:

![](https://github.com/flash62au/WiThrottleProtocol/raw/master/images/delegate-example.jpg)

### WiThrottleProtocol_FastTime

Example to show how to get the fasttime from WiThrottle server, and how to transform the timestamp in HOUR:MINUTE format. As explained above, I removed all the external dependences: the library returns a timestamp (method ```getCurrentFastTime()```) and you can choose your preferred library (or none) to parse it.

For this example you need the [```Time``` library](https://github.com/PaulStoffregen/Time), which can be installed through IDE Library Manager.

Compile and run. Use a proper terminal (MobaXterm in my screenshot) to see the time updated in the same line:

![](https://github.com/flash62au/WiThrottleProtocol/raw/master/images/fastclock-example.jpg)

### WiThrottleProtocol_Roster

Example to show how to get the list of locomotives in the roster. The library parses the roster message (RLx) but **doesn't** store the list. Instead, it offers two callbacks to get the number of entries and, for each entry, name / address / length (**S**hort|**L**ong).

Compile and run, you should see in the Serial monitor the list of locomotives as defined in JMRI:

![](https://github.com/flash62au/WiThrottleProtocol/raw/master/images/roster-example.jpg)

### WiThrottleProtocol_mDNS

Example to show how to browse for WiThrottle mDNS servers.

The example lists the discovered server in the serial monitor and connects to the first one found.

Compile and run, you should see in Serial monitor the discovered WiThrottle servers.

### WiThrottleProtocol_multiThrottle

Example to show how to use the multiThrottle methods.

This sketch connects to the first discovered server and acquires locos 10 and 11 in throttles 0 and 1.  It then reverses their direction every 5 seconds.

Compile and run.  To best see this in action, use a controller app like Engine Driver (android) or WiThrottle (iOS) and acquire locos 10 and 11 in separate throttles.  You will see their direction change every 5 seconds.

---

## Public Methods and attributes

see https://flash62au.github.io/WiThrottleProtocol/library.html


## Todos

 - Update the examples
 - Add multithrottle examples
 - Finish the in-code documentation 
 - Better Parser (Antlr?)
 
 ## Usage Notes
 
 ### Multithrottle Support

 - When I added the multithrottle support I have done my best to maintain backwards compatibility.  As a result if you use the non-multithrottle versions of any of the methods, the *default* multithrottle is now defunct 'T' rather than the now standard '0'.<br/>That means that you ***cannot mix*** multithrottle and non-multithrottle versions of the methods in your code.

 ### WiFi limitations

 This is **not** a limitation of the library, but of the ESP32 architecture.
 
 The ESP32 *cannot use the 5gHz* frequencies.  It is limited to the 2.4gHz  frequencies. 
 
 It also seems to be *unable to use channels beyond 10* (and I have seen it struggle with channel 10 itself.)

----
----

# License

Creative Commons [CC-BY-SA 4.0][CCBYSA]   ![CCBYSA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)


**Free Software, Oh Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [depinj]: <https://en.wikipedia.org/wiki/Dependency_injection>
   [delegate]: <https://en.wikipedia.org/wiki/Delegation_(object-oriented_programming)>
   [CCBYSA]: <http://creativecommons.org/licenses/by-sa/4.0/>
   
