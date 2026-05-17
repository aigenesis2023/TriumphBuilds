# Source content extraction — Keyless New Proposal 080526


## Slide 1

Refreshed Proposal.
The original content has been divided into two sections, the first is the material to be included in the e-learning lesson. 
T
he second is material that should be included in a supporting reference document (.pdf).
The purpose of this is to reduce the likelihood of cognitive overload and aid retention of key principles rather than a bombardment of facts that won’t be remembered.
Exact details of the cut/uncut content is open to some discussion.

## Slide 2

Purpose 
The purpose of this eLearning course is to give a more detailed insight into both key and keyless systems that Triumph motorcycles use .  For a more general appreciation of the Triumph Diagnostic Tool user instructions relating to these systems, technicians are recommended to refer to the diagnostic tool user guide that can be found on Triumph Online (TOL)  Service and Technical section .

## Slide 3

Basic Overview of KEY vs KEYLESS systems
KEY System 
- In a traditional key-operated motorcycle ignition system, the rider inserts a physical key into the ignition slot. The antenna ring, integrated around the key barrel, reads the RFID (Radio Frequency Identification) signal embedded in the key. Once the key is turned, the antenna relays this data to the receiver control unit (RCU), which interfaces with the immobilizer system. Upon verifying the correct key, the immobilizer disengages, allowing the ECU (electronic control unit) to activate the electronic fuel injection system (
efi
). With fuel delivery enabled, the engine control system enables 
efi
, and the motorcycle is allowed to start.
KEYLESS System - 
In contrast, a keyless motorcycle ignition system relies on proximity technology. The rider carries a smart fob, which emits a secure radio frequency signal. When the rider approaches within a 1m radius, the onboard receiver unit detects the fob’s signal. As the rider presses the start button, the system autonomously authenticates the fob with a secure set of handshake sequences. Once validated, the RCU or CCU (chassis control unit) or KCU (keyless control unit), this will depend on system and model, authorizes the 
efi
 ECU to enable ignition and fuel delivery. Thus, the motorcycle starts without physical key insertion, relying on encrypted proximity communication.

## Slide 4

Feature
Key Ignition System
Keyless Ignition System
Authentication Method
Physical RFID key detection
Proximity-based encrypted fob communication
Security
Moderate (key can be lost or copied)
High (encryption and proximity add security)
Complexity of Use
Simple, traditional operation
Slightly more complex, automatic detection
Reliability
Proven, long-term technology
Dependent on battery in fob
Convenience
Requires manual key insertion
Seamless, no physical action needed
Vulnerability to Theft
Key duplication possible
Potential fob hacking, relay attacks unless key is ‘off’
Cost
Lower, simple mechanical components
Higher, advanced electronic modules
Maintenance
Low, minimal wear parts
Medium, fob battery replacement required
This should give a clear, technical side-by-side comparison of the two systems!
Basic Overview Key vs Keyless

## Slide 5

Key
 Ignition Overview facts  
Transponder in key 125Khz
TPMS Operates using LF frequency (434 ROW + 315MHZ JP market) 
Comms / paired with RCU (receiver control unit) / Immobiliser 
Keys must be separated with RCU via antenna ring
Max 4 keys per bike (depending on model)
TPMS also is paired to the RCU (if fitted)
TDT required to pair keys / immobiliser / TPMS
Cut keys available to order from Triumph 
for certain models only (see 
epc
 for details) 
As a rule, generally smart ‘keyless’ keys do not have blank key blade support, whereas immobilisers and seat locks do.
If all keys lost, replacement immobiliser, keys and lockset will be required
TDT note:
The 
Add New Key function 
allows the user to pair one key to the 
immobiliser
 system at a time, provided the maximum number of paired keys has not been reached. An attack delay of 5 minutes must pass for each key pairing.
The 
Re-Register All Keys function 
erases all keys from 
immobiliser
 system memory, except the key used to turn the motorcycle ignition ON at the start of the process. The function then allows multiple keys to be paired, up until the maximum number of allowed keys has been 
reached. 
An attack delay of 5 minutes must pass for each key pairing. On some motorcycles, an attack delay of 5 minutes must also pass before existing key pairings can be 
erased.

## Slide 6

TDT note: 
When
 to use Add/Reregister?
Common confusion when usin
g the TDT is when to:
Use the 
Add New Key 
function to:
Pair new keys when the maximum number of paired keys has not been reached.
Use the 
Re-Register All Keys 
function to:
Pair new keys if the motorcycle’s lock set has been replaced.
Pair new/replacement keys when some/all keys have been lost.
Pair new/replacement keys when the maximum number of paired keys has been reached.
Important: Make sure that keys are separated before starting key paring activities.
When pairing a key, make sure that only the key being paired is in close proximity to the ignition switch 
antenna.
Placing two keys close to the ignition switch antenna can cause the key pairing process to fail.

## Slide 7

Keyed System Immobiliser types - 
Key Ignition Models

## Slide 8

TPMS operation is part of immobiliser system
TLyre
 Pressure Monitoring System (TPMS) Description
⚠️ 
WARNING
The tyre pressure monitoring system is not to be used as a tyre pressure gauge when adjusting the tyre pressures. For correct tyre pressures, always check the tyre pressures when the tyres are cold using an accurate tyre pressure gauge.
Use of the TPMS system to set inflation pressures may lead to incorrect tyre pressures, leading to loss of motorcycle control and an accident.
Owners must only adjust tyre pressures when the tyres are cold using an accurate tyre pressure gauge and must not use the tyre pressure display on the instruments.
The tyre pressures shown on the instrument panel indicate the actual tyre pressure at the time of selecting the display. This may differ from the inflation pressure set when the tyres are cold because tyres become warmer during riding, causing the air in the tyre to expand and the pressure to increase. The cold inflation pressures specified by Triumph take account of this.
The TPMS will not transmit the tyre pressure data until the motorcycle is travelling at a speed greater than 12 mph (20 km/h). Two dashes will be visible in the display area until the tyre pressure signal is received.
TPMS Components
Instruments
 – Used to display the tyre pressure value, the tyre symbol, and the TPMS warning light.
Immobiliser/TPMS ECM
 – Receives the data from the tyre pressure sensors and sends the information to the instrument pack.
Tyre pressure sensor
 – Situated inside the front and rear wheel. Each sensor has its own unique ID number and must be recorded in the spaces provided in the Owner’s Handbook. These sensors measure the air pressure inside the tyre and transmit pressure data to the instruments.
The wheel sensor is a sealed unit and must not be opened. The battery inside the sensor is not replaceable and a new sensor must be fitted when the battery voltage becomes too low.
Pressures embedded in the calibration for specific model
Drop of 6psi = light on
315MHZ RF– JP key + 
tpms
434MHZ RF– ROW key + 
tpms

## Slide 9

Keyed TPMS Pairing Flow - Keyed

## Slide 10

TPMS Data Screen
Note: 
The wheel sensors go into a sleep mode seven minutes after the wheels become stationary. If the wheel sensors are in sleep mode, no data will be displayed against tyre pressure and temperature. 
To wake the sensors, the bike must be ridden at a speed greater than 18 mph (30 km/h) for at least 30 seconds.

## Slide 11

2 x different frequencies and part numbers to suit - Keys
Care must be taken to ensure that the correct frequency is ordered for the correct model.               It is recommended to use vin lock EPC 

## Slide 12

FOR MAXIMUM RIDER CONVENIENCE, THE SYSTEM RECOGNISES THE PROXIMITY OF THE KEYLESS FOB TO ENABLE IGNITION VIA START BUTTON
KEYLESS ELECTRONIC STEERING LOCK BUTTON ON RIGHT HAND SWITCH CUBE
KEYLESS FUNCTION CAN BE DISABLED FOR EVEN GREATER SECURITY
ADDITIONAL SECURITY FEATURE UNIQUE TO TRIUMPH
KEYLESS IGNITION AND STEERING LOCK

**Notes:**
> Triumph’s keyless ignition and steering lock system is fitted as standard, 
> This recognises the proximity of the keyless fob and then enables the ignition via the switch cube mounted start button
> There is also the ability to disable the key’s wireless transmission function at the touch of a button 
> for even greater security – a unique feature to Triumph

## Slide 13

The latest Keyless chipset includes a timing check to safeguard against relay attacks (RF repeaters used by thieves to clone the signal and steal the car / motorcycle).
The system checks for the time taken to return the handshake message, so unless the fob is directly talking to the security module, it would take too long and fail, so the bike would not unlock.
If a repeater was being used by a potential thief, the lag/delay would not be able to imitate the speed of the handshake from the original fob. 
Time of Flight – Additional Security 

**Notes:**
> RF = Radio Frequency

## Slide 14

Keyless
 Overview facts  
Two types of key. Smart and passive (434 ROW + 315MHZ JP market) 
Transponder in both types of key 
Comms / paired with KCU or CCU rather than RCU (receiver control unit) / aka Immobiliser 
Max of 3 keys registered per bike
TPMS also is paired to the KCU or KCU depending on model.
TDT required to pair keys / immobiliser / TPMS
Cut keys available to order from Triumph 
for certain models only (see 
epc
 for details). 
As a rule, generally smart ‘keyless’ keys do not have blank key blade support, whereas immobilisers and seat locks do.
Pairing is required between KCU / ESL / 
The 
Add New Key function 
allows the user to pair one key to the 
immobiliser
 system at a time, provided the maximum number of paired keys has not been reached. An attack delay of 5 minutes must pass for each key pairing.
The 
Re-Register All Keys function 
erases all keys from 
immobiliser
 system memory, except the key used to turn the motorcycle ignition ON at the start of the process. The function then allows multiple keys to be paired, up until the maximum number of allowed keys has been 
reached. 
An attack delay of 5 minutes must pass for each key pairing. On some motorcycles, an attack delay of 5 minutes must also pass before existing key pairings can be 
erased.

## Slide 15

When
 to use Add/Reregister?
Common confusion when using the TDT is when to:
Use the 
Add New Key 
function to:
Pair new keys when the maximum number of paired keys has not been reached.
Use the 
Re-Register All Keys 
function to:
Pair new keys if the motorcycle’s lock set has been replaced.
Pair new/replacement keys when some/all keys have been lost.
Pair new/replacement keys when the maximum number of paired keys has been reached.
Important: Make sure that keys are separated before starting key paring activities.
When pairing a key, make sure that only the key being paired is in close proximity to the LF 
antenna.
Placing two keys close to the antenna can cause the key pairing process to fail.

## Slide 16

Smart Key Battery Requirements – CR2032 (Duracell)
It is important that a high quality lithium CR 2032 battery is fitted. We recommend Duracell brand batteries (
https://www.duracell.co.uk/product/lithium-coin-2032-batteries
/) are used, but any similar high quality branded battery is acceptable in the case that Duracell are not available in your market
. This helps ensure quality and performance and battery size accuracy. Some low quality battery sizes are slightly smaller in size, therefore connection to it and therefore reliability is affected.
Important! Annual Service Item to replace a battery! Possible to measure battery voltage using a multi meter!
1. Status symbol light
2. ON/OFF button

**Notes:**
> Open key, replace battery, and close.  
> Note:
>  torque sensitive bolt to secure battery cover – over-torquing WILL break it. Not warranty! Standard key = Passive Key
> IMPORTANT: Unique selling point and security.  The UHF transmission can be switched off on the Triumph key. No other motorcycle manufacturer has this currently.
> Tiger 1200
> Triumph Academy

## Slide 17

TPMS Questions
Questions with the answers:
Why should tyre pressures always be checked when the tyres are cold?
Because tyres become warmer during riding, causing the air to expand and the pressure to increase.
What might happen if you use the TPMS system to set inflation pressures?
It may lead to incorrect tyre pressures, which can result in loss of motorcycle control and an accident.
At what speed will the TPMS transmit tyre pressure data?
When the motorcycle is travelling at a speed greater than 12 mph (20 km/h).
What is the purpose of the tyre pressure sensor inside the wheels?
Each sensor measures the air pressure inside the tyre and transmits the pressure data to the instruments.
Why must the wheel sensor not be opened or replaced except when the battery is too low?
Because the wheel sensor is a sealed unit; the battery inside is not replaceable, and a new sensor must be fitted when the battery voltage drops.

## Slide 18

Establishing Communications with Key
The key recognition process is initiated by the KCU energising the external LF antenna(e). There are two methods of communication from the key to the KCU, either via UHF (for “smart” keys) or LF (as a backup method for “smart” keys and used for “non-smart” keys). 
“non-smart” keys.                                                      “smart” keys
The key recognition is based on a mutual identification and authentication between the transponder and the RCU KCU or CCU. 
The key recognition process must remain transparent for the rider, and therefore the time taken to authenticate the key should be as short as practicable. The overall time before the key authentication result is available should be a maximum of approximately 5 seconds. The nominal time before the key authentication result is available however is 200ms. 
See example 1 and 2 om following slides 
The first key identification process should be of “smart” keys (via 
UHF
, then 
LF
), followed by any paired “non-smart” keys (via LF only). In addition, if multiple LF antennas are present, the key identification process should poll for each key via each antenna, before attempting to identify a different key. 
Point of interest - In a motorcycle keyless ignition system, UHF (ultra-high frequency) and LF (low frequency) are two distinct communication bands. LF, typically around 125 kHz, is used for the initial authentication, as it offers better range for close-proximity detection and is less prone to interference. UHF, either 315 or 434 MHz range, is used for active communication once the system is engaged, allowing for longer range and more secure data transfer. In short, LF handles proximity sensing, while UHF supports the ongoing communication once the key is near.

## Slide 19

Example – keyless system ignition-on process
YELLOW - 
What customer perceives as being the state of bike. 
BLUE 
– Actual state of bike.
User presses either “power” or “start” button
Keyless control unit (KCU) wakes up
KCU checks for recognised key being available and for matching ESL identification.
If the KCU finds a recognised key and confirms the ESL identification, it will apply power to the “12v ignition” input to all other components
All other components wake up simultaneously, except ECU which will only wake up if the kill switch is in the “run” position
When ECU wakes, it queries key authentication state from KCU (KCU responds key is authenticated)
ECU and KCU then exchange security keys as final step of immobiliser functionality
If ECU-KCU exchange is OK, engine can be started.
BIKE IS “OFF”
BIKE IS “ON”
BIKE CAN START

**Notes:**
> YELLOW - What customer 
> perceives as being the 
> state of bike.

## Slide 20

Wake Up Sequence – 
note don’t mix item number up with stage number
(Use with previous slide)
7
3
4
3
6
2
2
1
Power Button
5
Run Position
Check
2
8
6
.    Ignition Circuit (12v controlled via KCU)
Ign
 System
1. Transponder chip
2. Electronic steering lock
3. LF Antenna (front)
4. Keyless ECM
5. Engine ECM
6. LF Antenna (rear)

**Notes:**
> Use the previous
>  slide to identify the 8 wake up sequence stages. 
> Item 4 Includes instrument wake up.
> When KCU wakes the immobiliser light will flash and you will have access to immobiliser diagnostics. 
> ‘Play’ this slide in ppt view for best understanding.

## Slide 21

Important Note
If passive key is used to power the bike up then a 90 second time limit is applied to the ignition supply.  Therefore if a download is started in this scenario it may fail.
Same applies if smart key goes out of range.
Example, if a rider switches his ignition on using his passive key in close proximity to LF antenna, and then removes the key away from the LF antenna , 90 seconds later the ignition will turn itself off .  Similarly , if a rider switches the ignition on using his smart key , and then walks away with the smart key outside of the one metre proximity range , for more than 90 seconds , then again, the calibration strategy will switch the ignition off .  
Technicians should be aware of this , especially during downloads , as if the ignition switches itself off during the download stage it will automatically fail the download 

## Slide 22

In Summary 
In summary, the Triumph key system allows up to three keys paired to the motorcycle’s ECM, with both passive and smart key options. Pairing is irreversible, and a security delay ensures each pairing process is deliberate. Only paired keys activate the bike, and erasing keys is also done via the diagnostic tool, though erased keys remain inactive in memory until overwritten. In short, it balances security, precise pairing, and controlled key management.
Important Note: 
The display indicating how many keys are already paired may not be available on certain models. Where this is the case, the 'Key(s) Learned' counter will remain at zero regardless of how many keys are paired. 
On certain models, the number paired keys will not be reported until after a key has been paired. 
The immobiliser will reject any attempt to pair keys once the maximum number of paired keys is reached.
If some of the keys that are already paired are lost and the maximum number of paired keys is already reached, use the re-register all keys function

## Slide 23

General Key and Keyless Information Points commonly overlooked - 5 Questions 
What tool is used to erase or add keys to the keyless ECM?
Answer:
 The Triumph diagnostic tool.
2. What is the maximum number of keys that can be paired to the keyless ECM at one time?
Answer:
 A maximum of three keys can be paired.
3. Why is it recommended to pair smart keys before passive keys?
Answer:
 It is recommended so that smart keys are paired first, ensuring proper order in the pairing process.
4. What happens to a paired key once it is locked to its keyless ECM?
Answer:
 The key is permanently locked to that ECM and cannot be paired to any other keyless ECM.
5. How long is the security time delay for the first key pairing after using the Re-Register All Keys function?
Answer:
 The security time delay is ten minutes (600 seconds).

## Slide 24

In Summary 
In summary, the Triumph key system allows up to three keys paired to the motorcycle’s ECM, with both passive and smart key options. Pairing is irreversible, and a security delay ensures each pairing process is deliberate. Only paired keys activate the bike, and erasing keys is also done via the diagnostic tool, though erased keys remain inactive in memory until overwritten. In short, it balances security, precise pairing, and controlled key management.
Important Note: 
The display indicating how many keys are already paired may not be available on certain models. Where this is the case, the 'Key(s) Learned' counter will remain at zero regardless of how many keys are paired. 
On certain models, the number paired keys will not be reported until after a key has been paired. 
The immobiliser will reject any attempt to pair keys once the maximum number of paired keys is reached.
If some of the keys that are already paired are lost and the maximum number of paired keys is already reached, use the re-register all keys function

## Slide 25

General Key and Keyless Information Points commonly overlooked - 5 Questions 
What tool is used to erase or add keys to the keyless ECM?
Answer:
 The Triumph diagnostic tool.
2. What is the maximum number of keys that can be paired to the keyless ECM at one time?
Answer:
 A maximum of three keys can be paired.
3. Why is it recommended to pair smart keys before passive keys?
Answer:
 It is recommended so that smart keys are paired first, ensuring proper order in the pairing process.
4. What happens to a paired key once it is locked to its keyless ECM?
Answer:
 The key is permanently locked to that ECM and cannot be paired to any other keyless ECM.
5. How long is the security time delay for the first key pairing after using the Re-Register All Keys function?
Answer:
 The security time delay is ten minutes (600 seconds).

## Slide 26

The following three slides summarise the contents of the Immobiliser Diagnostics menu, depending on model will determine what the TDT menu will show, they are:
KEY MODELS ONLY (NOT 400CC) 
– Menu = 
Read stored DTC‘s + configure  
ALL KEYLESS MODELS 
- Menu = 
Build data + Read stored DTC’s + Configure 
400CC ONLY 
– Menu = 
Build data + read DTC’s + Live Data + Adjust 
There can be a huge amount of information found in these menus , however some of this information is applicable to the manufacturer only .  The following slides help to identify which is the most useful information to dealers , and which is applicable to the manufacturer only  indicated by 
‘Manufacturer reference only’ 
TDT Immobiliser menu summary 

## Slide 27

Configure - 
Pairing System Components 
The Triumph immobiliser system has to be electronically linked (known henceforth as paired) with other components in the engine management system and with the ignition key, which contains a transponder chip. If all the components are correctly paired, the immobiliser will allow the engine to start. The diagnostic software is the only way these components can be paired and for faults associated with the system to be diagnosed and cleared. The diagnostic software is capable of pairing components for both standard (key ignition) and keyless ignition immobiliser systems using the TDT only.
KEY MODELS ONLY (NOT 400CC) 
– Menu = Read stored DTC‘s + configure  
Read DTC’s
A very useful information source for technicians.  Listing both a code and description for the stored DTC.  Refer to the relevant Triumph service manual for additional information on individual DTCs and for pinpoint tests to fully diagnose and repair the fault. For supported/more recent models, 
the DTC can link directly to the relevant pin point check within the service manual for much faster diagnostics. 
Show example screen 
usin
 Tech Bulletin 255.

## Slide 28

The key signal function test can be used on models with keyless ignition
The function test can be started by clicking the Start button.
When started, the function test will periodically check for detected keys. The test provides three coloured lights for the following:
• UHF (Ultra High Frequency key detection)
• LF (Low Frequency key detection)
• LF Antenna (LF Antenna Status).
The status reported by the coloured lights is refreshed every 2 to 3 seconds while the function test is running.
The coloured light and text displayed in the status bar at the bottom of the Test Details screen will alternate between displaying the test status and test results as follows:
• Amber = Test running
• Red = No keys detected
• Green = Key detected (by either UHF or LF).
The test can be stopped at any time by clicking the Stop button
Key Signal Function Test - Keyless Ignition Models

## Slide 29

The UHF coloured light provides indication of whether or not a paired, active smart key is being detected by the motorcycle's keyless ignition system. The smart key must be paired to the keyless ECM, and must be in Active mode to be detected by UHF.
Paired smart keys can typically be detected at a range of up to one metre from the motorcycle when in active mode.
When the function test is running:
• A red light indicates that no key was detected by UHF method at the last attempt.
• A green light indicates that a paired, active smart key was detected by UHF method at the last attempt
UHF Key Detection

## Slide 30

The LF coloured light provides indication of whether a compatible key is being detected by the LF antenna.
The LF antenna will detect any key that is compatible with keyless ignition, regardless of whether or not the key has been paired with the keyless ECM.
Compatible keys must be placed in close proximity of the LF antenna (typically within 25 mm) to be detected.
When the function test is running:
• A red light indicates that no key was detected by the LF antenna at the last attempt.
• A green light indicates that a compatible key was detected by the LF antenna at the last attempt
LF Antenna Status
The LF Antenna light provides indication of the status of the LF antenna.
When the function test is running:
• A red light indicates that a LF antenna fault is present.
• A green light indicates that the LF antenna is functioning normally.
LF Key Detection

## Slide 31

Cooker Knob Isolator Switch - Ignition Master Switch Link 
US models have an isolator switch.  Models outside of US have a loop-out plug.
Good to know for diagnostics!

## Slide 32

Important Keyless Notes
Bike will allow TDT connection to immobiliser diagnostics for 30 seconds without a key present. It allows connection window of 30 secs but once connected it will stay connected.
So KCU will wake with no key but only gives access to TDT Immobiliser diagnostics
NB Immobiliser light sequence flashes (see table)

## Slide 33

Keyless Facts for Diagnostics
Q1. How often does smart key and KCU contact each other?
 A. Once, on start up only.  
Q2 If the communication failed how is the above message is displayed? 
A If no key detected, the immobiliser LED flashes the appropriate sequence.  ‘Key not found' error message is not shown.
Q3 How do you clear ‘Key not found’ error message with bike running? 
Key not found error no longer appears.
Q4 What error message is displayed if an owner uses a passive key to start the bike (or smart key in passive mode)?
None.

**Notes:**
> The old system used to look for the key 10s after pulling away. If it finds it, it will wait 20s before checking again. If it finds it at that time, it will wait 40s…
> The duration doubles, up to a limit of 20 mins (1200 seconds).
> If the key is ever NOT found, it will keep looking every 10s, if it finds it again the process restarts.
> Previously a “missing” key would always be shown for 20 minutes (minimum). Now, the minimum time is 10s.

## Slide 34

Q5 What error message is displayed if an owner starts the engine using a smart key with in active mode, then switches it to passive mode after starting the engine in order to save key battery life?
A. No error message is shown.  However, bike will not re-start in this condition if the ignition is switched off.
Q6 Triumph keyless fobs use a CR2032. What is the voltage, and service limit voltage of the battery.?
CR2032 is a 3v battery with a 2v* service limit.  This is measured as the battery is under load during communication and a rolling average is taken. 
A cold battery may result in a lower measured charge and so a “low battery” warning might be observed intermittently as the overall state goes down.
Q7 What DTC is logged when a battery goes below the 2v threshold?
A. None, Low batteries do not flag a DTC. As this 
is a predictable/expected scenario over the course of the life of a bike.
The user would see a warning on the dash saying “key fob low battery” but it does not store this.
Q8 Following a keyless error message "HOLD TO RESET" message displayed. What is this? 
A. This means if the joystick centre is pressed then the warning message will clear, the warning light however will remain lit.
Keyless Facts for Diagnostics

**Notes:**
> * Below 2.9v in reality may cause issues.

## Slide 35

Case Study Situation 
Case Study
 Situation:
A customer comes to his bike, the bike will not power on as normal, does not crank or start, nor do the instruments illuminate, the electronic steering lock is fully engaged and will not disengage. 
They take the bike to the dealer for diagnostics (on the back of a truck!)
2.        The dealer inspects the bike, and should be given a selection of possible options / approaches as steps to resolve the situation.
Replace the bike battery
Replace key fob
Conduct a download
replace the electronic steering lock
replace the keyless control unit
Replace the instrument pack
or 
other
3.         The ‘
other
’ options should include 
‘reading’ the immobiliser flash sequence on the instruments
. Include further incorrect answers also such as:
replace key fob battery
replace wiring to 
kcu
replace the starter switch gear
check switch gear connection etc 
If correct answer is chosen as an option, then the flash sequence table should be illuminated.  
Inform user at this stage: 
The flash sequence seen on bike is 1 long flash plus 3 short flashes
The technician should then be given a list of options of what this means various reasons may be given, 
ie
 they need to choose the right one from the table.

## Slide 36

Q - Where can techs find this info? – 
TOL
Owners handbook
Internet, it’s a generic code 
Ask others 
In the manual 
From TTI
4. The next option the dealer should be given is how to access further information / 
dtc
 about this flash sequence 
using 
only
 the triumph diagnostic tool 
as the bike doesn’t power on?
The options should include:
This is not possible, as steering lock is inoperative and the instruments won't switch on
This is not possible unless the electronic steering lock is replaced
This is not possible unless the instrument is replaced or swapped
This is possible following a complete download to the KCU
This is possible for just for a 30 second ‘window’, once a connection has been made and established, the connection will continue.
5. Once connection is established, the technician finds the 
dtc
 reads 
C1137
 – use the 
dtc
 table to determine the cause and remedy
6. Ie 
The technician should then have to list the correct repair from the table. 
Reminder 
to use link from DTC to service manual for access to the fault finding table (if supported by that model).

## Slide 37

Bonus Question:
 one chance at getting right only! 
But correct answer to be given following the attempt.
Hypothesise on a second related problem 
Q - If the same symptom scenario occurred, BUT no TDT access to KCU was possible (
ie
 for 
the 30 sec 
window), also no flash sequence on instruments (only the standard immobiliser sequence). What could this mean?  
A = Likely KCU not seeing input from switch gear. 
Include incorrect answers like:
Instruments may have incorrect software
The LED in the instruments might be inoperative
A theft relay attack may have occurred and the bike has automatically shut down
The TDT software is out of date and requires updating 
Once correct answer selected, the answer can be expanded on 
ie
: 
Possible Inoperative start switch/button or poor connection to start switch/button. Techs should get multi meter to check switch operation, as this would be the only way to check correct operation and circuit connection (
ie
 TDT diagnostics not possible in this instance).

## Slide 38

Case Study Situation 
dtc
 table – (AR note - any 
dtc
 can apply but not ones with red line)  

## Slide 39

Keyless Ignition and Immobiliser System CASE STUDY - 
see separate word file
1. Fuse box 1
2. Electronic steering lock
3. Electronic steering lock connector
4. Instruments
5. Engine 
subharness
6. Chassis ECM
7. Right hand switch housing connector
8. Right hand switch housing
9. LF antenna
10. LF antenna connector
11. LF antenna
12. LF antenna connector
13. Engine ground
14. Fuel filler cap
15. Keyless control unit

## Slide 40

The following material has been removed and should be produced as a printable, reference resource
Icon for removal from original ref only

## Slide 41

KeyLess
 Components Locations-drag n drop names – 
ideas?
(see following slide for locations)
Key (passive and active)
TPMS
Fuse box 
Electronic steering lock
Electronic steering lock connector
Instruments
Engine sub harness
Chassis ECM / immobiliser
Right hand switch housing connector
Right hand switch housing
LF antenna
LF antenna connector
LF antenna
LF antenna connector
Engine ground
Fuel filler cap
Keyless control unit / immobiliser
Remove

## Slide 42

ECMs Location Example – (expand acronyms) 
ideas?
SCU
CCU
ABS
KCU
ECU
Instruments
Headlight
Remove

## Slide 43

‘Typical’ overview Electrical Architecture communication paths example – NB remove drawing detail
(Lee Gretton) – Identify Keyless related components exercise + highlight accordingly 
ideas? 
Slide should help technicians understand the basic architecture of the system and what components and communication paths are involved
Remove

## Slide 44

For second option instead of previous slide 
ideas?
1. Fuse box 1
2. Electronic steering lock
3. Electronic steering lock connector
4. Instruments
5. Engine 
subharness
6. Chassis ECM
7. Right hand switch housing connector
8. Right hand switch housing
9. LF antenna
10. LF antenna connector
11. LF antenna
12. LF antenna connector
13. Engine ground
14. Fuel filler cap
15. Keyless control unit
Slide should help technicians understand the basic architecture of the system and what components and communication paths are involved
Remove

## Slide 45

Refined summary to be linked with circuits on previous pages. 
Ideas? 
Overview of wake up sequence
The wake-up sequence has eight stages:
First, the user presses the power button. 
Then, the keyless control unit (KCU) wakes up
KCU checks for a recognized key tied to the electronic steering lock. 
Once the key is confirmed, the KCU supplies 12-volt power to 12v ignition input to all other associated components. 
After that, all components wake up, except the ECU, which waits for the kill or ignition switch to go to the run position . 
Once the ECU wakes up, it queries the key authentication status from the KCU. 
After authentication, the ECU and KCU exchange security keys for immobilizer verification. 
If ECU and KCU exchange is successful, the engine is ready to start.
Remove

## Slide 46

TDT Menu Overview (key and keyless) 
covered in detail in later slides 
Remove

## Slide 47

Pressures embedded in the calibration for specific model
Drop of 6psi = TPMS light on
315MHZ RF– JP key + 
tpms
434MHZ RF– ROW key + 
tpms
TPMS Is part of 
Imobiliser
 Systems (same as previous slide)
TLyre
 Pressure Monitoring System (TPMS) Description
⚠️ 
WARNING
The tyre pressure monitoring system is not to be used as a tyre pressure gauge when adjusting the tyre pressures. For correct tyre pressures, always check the tyre pressures when the tyres are cold using an accurate tyre pressure gauge.
Use of the TPMS system to set inflation pressures may lead to incorrect tyre pressures, leading to loss of motorcycle control and an accident.
Owners must only adjust tyre pressures when the tyres are cold using an accurate tyre pressure gauge and must not use the tyre pressure display on the instruments.
The tyre pressures shown on the instrument panel indicate the actual tyre pressure at the time of selecting the display. This may differ from the inflation pressure set when the tyres are cold because tyres become warmer during riding, causing the air in the tyre to expand and the pressure to increase. The cold inflation pressures specified by Triumph take account of this.
The TPMS will not transmit the tyre pressure data until the motorcycle is travelling at a speed greater than 12 mph (20 km/h). Two dashes will be visible in the display area until the tyre pressure signal is received.
TPMS Components
Instruments
 – Used to display the tyre pressure value, the tyre symbol, and the TPMS warning light.
Immobiliser/TPMS ECM
 – Receives the data from the tyre pressure sensors and sends the information to the instrument pack.
Tyre pressure sensor
 – Situated inside the front and rear wheel. Each sensor has its own unique ID number and must be recorded in the spaces provided in the Owner’s Handbook. These sensors measure the air pressure inside the tyre and transmit pressure data to the instruments.
The wheel sensor is a sealed unit and must not be opened. The battery inside the sensor is not replaceable and a new sensor must be fitted when the battery voltage becomes too low.
Remove

## Slide 48

Keyless TPMS Pairing Flow – Keyless (same as keyed)
Remove

## Slide 49

TPMS Data Screen
Note: 
The wheel sensors go into a sleep mode seven minutes after the wheels become stationary. If the wheel sensors are in sleep mode, no data will be displayed against tyre pressure and temperature. 
To wake the sensors, the bike must be ridden at a speed greater than 18 mph (30 km/h) for at least 30 seconds.
Remove

## Slide 50

2 x different frequencies and part numbers to suit - Keys
Remove

## Slide 51

2 x different frequencies and part numbers to suit - TPMS
Remove

## Slide 52

Establishing Communications with Key – 
Example 1
Attempt
Key
Method
Antenna
1
Smart key 1,
UHF,
LF antenna 1 
2
Smart key 1,
UHF,
LF antenna 2 
3
Smart key 1,
LF,
LF antenna 1 
4
Smart key 1,
LF,
LF antenna 2 
5
Non-smart key 1,
LF,
LF antenna 1 
6
Non-smart key 1,
LF,
LF antenna 2 
7
Non-smart key 2,
LF,
LF antenna 1 
8
Non-smart key 2,
LF,
LF antenna 2 
Example 1 - one “smart” key and two “non-smart” keys paired 
(this is the OE condition)
:
UHF – Ultra High Frequency
LF – Low Frequency
Attempt
 = KCU search criteria.  This means the first thing the KCU will do is look for the first registered smart key, via UHF through LF antenna 1.  If it doesn't find anything, it will do the same thing via LF antenna 2.  If nothing found, it will look for it in LF via antenna 1 and so on, working down the table.
Remove

**Notes:**
> UHF – Ultra High Frequency
> LF – Low Frequency
> Attempt
>  = KCU search criteria.  This means the first thing the KCU will do is look for the first registered smart key, via UHF through LF antenna 1.  If it doesn't find anything, it will do the same thing via LF antenna 2.  If nothing found, it will look for it in LF via antenna 1 and so on, working down the table.

## Slide 53

Establishing Communications with Key – 
Example 2
Attempt
Key
Method
Antenna
1
Smart key 1,
UHF,
LF antenna 1 
2
Smart key 1,
UHF,
LF antenna 2 
3
Smart key 2,
UHF,
LF antenna 1 
4
Smart key 2,
UHF,
LF antenna 2 
5
Smart key 1,
LF,
LF antenna 1 
6
Smart key 1,
LF,
LF antenna 2 
7
Smart key 2,
LF,
LF antenna 1 
8
Smart key 2,
LF,
LF antenna 2 
9
Non-smart key 1,
LF,
LF antenna 1 
10
Non-smart key 1, 
LF,
LF antenna 2 
Example 2 - two “smart” keys and one “non-smart” key paired 
(if customer decides to purchase a second smart key)
:
If using the last
 options in the table, there may be a detectable delay BUT less than 5 seconds.
Remove

**Notes:**
> If using the last
>  option in the table, there may be a detectable delay BUT less than 5 seconds.

## Slide 54

Antenna and Key Location Example-Proximity requirement 1m if Smart key switched 
ON. 
20mm if key switched 
OFF
1. Transponder chip
2. Electronic steering lock
3. LF Antenna (front)
4. Keyless ECM
5. Engine ECM
6. LF Antenna (rear) Primary MUST be used for key pairing
Remove

**Notes:**
> LFA = Low Frequency Antenna.

## Slide 55

Summary – maybe something like…
ideas?
Remove

## Slide 56

General Key and Keyless Information Points commonly overlooked 
All of the motorcycle’s available keys should be obtained before performing any key pairing operations. Starting a key paring operation without having obtained all of the motorcycle’s keys will render any spare keys inactive. In some circumstances, absent spare keys may also be rendered permanently unusable.
Lost or unwanted keys can be erased, and additional/replacement keys added using the Triumph Diagnostic Tool. 
A maximum of three keys can be paired to the keyless ECM at any one time. This can be any combination of smart keys and passive keys. It is not possible to pair further keys when the maximum of three paired keys is reached. 
When pairing a combination of smart keys and passive keys, it is recommended that any smart keys are paired first, followed by the passive keys. 
A paired key can have three different states, active, inactive and erased.  
Once a key is paired it is regarded as active. At this point the key is permanently locked to its paired keyless ECM and cannot be paired to any other keyless ECM – ever! 
A paired key is required to allow the motorcycle to power ON in order to perform key pairing operations. All available paired keys should be obtained before starting these operations.
Paired keys can be erased using the Re-Register All Keys function on the Triumph diagnostic tool. When this function is used, the key being used to power the motorcycle will remain paired and active. Any other paired keys will be registered as inactive.
Remove

## Slide 57

General Information Points (continued) 
Note: Keys pair to RCU, CCU or KCU (aka Immobiliser) depending on model
This is covered in a later section
When using the Re-Register All Keys function, a ten minute (600 second) security time delay is applied to the first key pairing. Further key pairings are subject to a five minute (300 second) time delay. 
Inactive keys can be either paired and reactivated, or replaced by new keys and overwritten. 
Any inactive keys that are overwritten are then stored as erased in the keyless ECM memory. A maximum of three erased keys can be stored. 
Erasing more keys after the maximum of three erased keys has been reached, will result in the erased keys being overwritten. Erased keys that are overwritten are then rendered permanently unusable. 
Stored erased keys can be paired and reactivated providing that the maximum number of three paired keys has not been reached. When a key is reactivated, it is moved from its ‘erased’ memory slot to a vacant ‘active’ memory slot.
Note: Only rear LF antenna can be used to pair keys 
Remove

## Slide 58

3 titles to be covered – examples From Rocket 3 GT Manual Calibration download flow chart 
Remove

## Slide 59

From Rocket 3 GT Manual 
Calibration download flow chart 
– see pdf service manual for chart  
Remove

## Slide 60

From Rocket 3 GT Manual 
Failed Download Recovery Chart 
see pdf service manual for chart 
Simplified version 
idea
EXAMPLE?
Check Key and Ignition:
Ensure paired key is in range.
Press power on.
Decision: Do instruments/headlights turn on?
Yes: Proceed to normal keyless ECM download.
No: Move to Stage 2.
Partial Keyless ECM Download:
Connect diagnostic tool.
Select correct calibration (manual selection).
Do not confirm yet.
Press power.
Within 10 seconds, confirm the download.
Follow on-screen instructions; cancel at 100%.
Re-register All Keys:
Go to chassis diagnostics.
Pair Electronic Steering Lock (if fitted):
Press power within 10 seconds, go to immobiliser diagnostics.
In configure tab, re-register all keys, starting with smart key.
Full Keyless ECM Download:
Ensure key is nearby, turn ignition on.
Complete the full ECM download, following prompts.
Finish once completed.
Pair Engine ECM with Immobiliser:
Switch start/stop to RUN.
Go to immobiliser diagnostics and pair engine ECM.
Final Steps:
Turn ignition off for 60 seconds.
Verify each key starts engine.
Check all ECMs for errors and clear as needed.
Remove

## Slide 61

ALL KEYLESS MODELS 
- Menu = Build data + Read stored DTC’s + Configure 
Build Data 
screen will display the following information.
• 
Vehicle Identification Number (VIN) 
– should match vin of bike. Only reprogrammable for new ECMs. Not reprogrammable once written.
• 
Part Number - Programmed vin into ECM 
– Manufacturer reference only 
• Serial Number 
– Manufacturer reference only 
• Boot Software ID
 – Manufacturer reference only 
• Application Software ID
 – Manufacturer reference only 
• Configuration ID1
 – Manufacturer reference only 
• Configuration ID2
 – Manufacturer reference only 
• Configuration ID3
 – Manufacturer reference only 
• Configuration ID4
 – Manufacturer reference only 
• Date of Last Application Download –  
A useful recorded date of when last download took place giving  indication as to when bike last had TDT connection / diagnostic session / was present at dealer.
Configure
– same as previous slide 
Read DTC’s 
– same as previous slide
Function Tests 
– see diagnostics (next section)  
Missing from guide
Remove

## Slide 62

400CC ONLY 
– Menu = Build data + read DTC’s + Live Data + Adjust 
Build Data 
(models fitted with a keyless ECM only) 400cc Single Cylinder Models
The Build Data screen will display the following information.
• 
ECM Type 
– Manufacturer Name of ECM
• 
Application Flash-File Name 
- Manufacturer reference only 
• 
Application Software Part Number 
– Manufacturer reference only 
• 
Application Software Issue Level 
– Manufacturer reference only 
• 
Part Number 
– Manufacturer reference only 
• 
ECM Serial Number 
– Manufacturer reference only 
• 
VIN
– should match vin of bike. Only reprogrammable for new ECMs. Not reprogrammable once written.
• 
Manufacturer Hardware Part Number 
– Manufacturer reference only 
• 
Last Programming Date 
– A useful recorded date of when last download took place giving  indication as to when bike last had TDT connection / diagnostic session / was present at dealer.
Live Data 
(models fitted with a keyless ECM only) 
400cc 
Single Cylinder Models
The Live Data screen will display the following information.
• 
Key(s) Learned 
– Number of keys learned to that immobiliser.
• 
Engine Start Permitted 
– Yes / No determined by status of immobiliser 
• 
Transponder Valid 
– Yes / No determined by status of transponder in key
• 
Authentication
 – Yes / No determined by status of key pairing 
Adjust 
(models fitted with a keyless ECM only) 
400cc 
Single Cylinder Models
• Key Pairing - See Pairing Keys in user guide - link
• ECM/Immobiliser Pairing - See ECM/Immobiliser Pairing in user guide - link
• Write VIN (if available) - See Write Immobiliser VIN 
obly
 for new spares condition 
ecm
 / cant be overwritten
Read DTC’s 
(models fitted with a keyless ECM only) 
400cc 
Single Cylinder Models
DTC detail is slightly different for the 400cc models listing, a code, failure code, description, failure description and DTC status. A very useful information source for technicians.  Refer to the relevant Triumph service manual for additional information on individual DTCs and for pinpoint tests to fully diagnose and repair the fault. 
Does 
dtc
 link to service manual?
Remove

## Slide 63

Diagnostic Process Reminder
Remove

## Slide 64

The Diagnostic Process – What is it? 
One chance to get right
Gather information
Understand the system involved
Determine test processes
Carry out tests and record results
Replace / repair as necessary*
Test 
Remove

**Notes:**
> [10 MINUTES]
> Trainers should be aware that diagnostic process is often lacking in technicians who have worked their way up from service techs. This is an opportunity to underline good, logical fault finding to help efficiency, customer satisfaction and a reduction on distributors’ dealer support resources.
> Go through the list asking delegates for examples of what they think each bullet point might mean:
> Work through the relevant systems
> Gather information: talking to the customer about what faults happen and when. When did the problem start? Are there any other issues? Are there any other accessories fitted? Any MIL? Fault codes? Test ride?
> Understand the system: Important to understand the relevant system so you know what bits are attached to what. 
> Determine a test procedure: Once you know the system(s) involved you can work through them from start to finish to make lists of possible causes. Then you can decide tests for each possible cause and 
> prioritise
>  them with likelihood and ease of test being high priority.
> Always refer to the Service Manual accordingly to help with the understanding of the system and relevant fault finding.
> Tests should then be carried out and all results recorded. Don’t procrastinate.
> Once the fault is found it can be repaired – remembering to test the repair’s effectiveness thoroughly.
> * Prior authorization may be required.

## Slide 65

Diagnostic Reminders
Always consider ALL DTCs in all ECUs.
Always avoid swapping parts from other ‘good’ bikes. Just because they look the same, does not mean they operate or are configured the same.
This is especially critical for “immobiliser” components, which are not just “configured” but also “paired”.
Avoid going from having one bike with problems to two bikes with problems.
Over 2 hours diagnostics. STOP!  Ask for assistance from Subsidiary or CWT.
Remove

## Slide 66

Six Step Diagnostic Process!
Use of Service Manuals
Glossary of terms
Plug types and numbering
Pin Point Tests
Schematics
Interactive Dynamic Wiring Diagrams
Electrical Diagnostic Reminder list all helpful TTI assets 
plus tech news 255!  
Remove

**Notes:**
> 5 Appears – Glossary, pin point tests, plug types with pin numbers, schematics, interactive dynamic wiring diagram.

## Slide 67

Key pairing failure possible causes
Key pairing can take time to see new key / metal side away from LFA. 
Maybe dismount antenna. Persevere!
Front antenna only there for keyless range around bike
Note battery tenders may affect key pairing due to electrical noise etc…
Remove

## Slide 68

Instrument Panel Flash Sequences
Remove
