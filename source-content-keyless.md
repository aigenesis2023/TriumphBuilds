# Source content extraction — KEYLESS INST DES.pptx

> Verbatim text extraction. Layout notes and SME instructions included where present.
> Slides marked [PLACEHOLDER] have no usable text — visual/image content only.
> Slides marked [SME NOTES] are developer instructions, not learner-facing content.

---

## Slide 1 — [SME NOTES]

Introduction and Welcome
What the course aims to do (next slide)
Link to supporting PDF
Reference the TDT guide and the specific SSMs on TOL

---

## Slide 2 — Course Purpose

The purpose of this eLearning course is to give a more detailed insight into both key and keyless immobiliser systems that Triumph motorcycles use. For a more general appreciation of the Triumph Diagnostic Tool and user instructions relating to these systems, technicians are recommended to refer to the diagnostic tool user guide that can be found on Triumph Online (TOL) Service and Technical section.

---

## Slide 3 — [SME NOTES]

Navigation
Links to each section – becoming available to open in sequence so jumping back is possible, but not skipping forward.

---

## Slide 4 — Key vs Keyless Immobiliser Comparison (Section Intro)

Key vs Keyless Immobiliser Comparrison
In this section we will compare the two types of security system in general terms.
While this will concern the two basic types it should be remembered that there are in fact four different approaches that have been, or are currently, used on Triumph motorcycles
In each case the technician should remember that the customer experience of these systems is one of turning on and starting the motorcycle, but there is a complex security system behind the user interface.

---

## Slide 5 — Similarities of Key and Keyless Immobiliser

They are both means to isolate engine run/start in the event of a theft attempt
Both include a mechanical steering lock function
Both contain the TPMS systems (where fitted as an option)

---

## Slide 6 — 4 Types of Immobiliser [INCOMPLETE]

There are 4 types of immobiliser system used across the model range
Comment…?

> ⚠ SME note says "Comment…?" — content appears incomplete. Flag for SME.

---

## Slide 7 — KEY System vs KEYLESS System

**KEY System –**
In a traditional key-operated motorcycle ignition system, the rider inserts a physical key into the ignition slot.
The antenna ring, integrated around the key barrel, reads the RFID (Radio Frequency Identification) signal embedded in the key.
Once the key is turned, the antenna relays this data to the receiver control unit (RCU), which interfaces with the immobilizer system.
Upon verifying the correct key, the immobilizer disengages, allowing the ECU (electronic control unit) to activate the electronic fuel injection system (efi).
With fuel delivery enabled, the engine control system enables efi, and the motorcycle is allowed to start.

**KEYLESS System –**
In contrast, a keyless motorcycle ignition system relies on proximity technology.
The rider carries a smart fob, which emits a secure radio frequency signal. When the rider approaches within a 1m radius, the onboard receiver unit detects the fob's signal.
As the rider presses the start button, the system autonomously authenticates the fob with a secure set of handshake sequences.
Once validated, the RCU or CCU (chassis control unit) or KCU (keyless control unit), this will depend on system and model, authorizes the efi ECU to enable ignition and fuel delivery.
Thus, the motorcycle starts without physical key insertion, relying instead on encrypted proximity communication.

Principal Differences of Key and Keyless Immobiliser / Ignition System

---

## Slide 8 — Feature Comparison Table: Key vs Keyless

> ⚠ Text extraction missed this — content is in a PPTX table with image placeholders at top for key photos. Full content from visual review:

Two image placeholder boxes at top (one for Key system photo, one for Keyless system photo).

| Feature | Key Ignition System | Keyless Ignition System |
|---|---|---|
| Authentication Method | Physical RFID key detection | Proximity-based encrypted fob communication |
| Security | Moderate (key can be lost or copied) | High (encryption and proximity add security) |
| Complexity of Use | Simple, traditional operation | Slightly more complex, automatic detection |
| Reliability | Proven, long-term technology | Dependent on battery in fob |
| Convenience | Requires manual key insertion | Seamless, no physical action needed |
| Vulnerability to Theft | Key duplication possible | Potential fob hacking, relay attacks unless key is 'off' |
| Cost | Lower, simple mechanical components | Higher, advanced electronic modules |
| Maintenance | Low, minimal wear parts | Medium, fob battery replacement required |

---

## Slide 9 — [PLACEHOLDER]

Summary of the Immobiliser Systems

> ⚠ No body content extracted — likely image/diagram only.

---

## Slide 10 — Assessment: Some Principal Differences (Drag & Drop)

For which immobiliser systems are these components / facts true? Drag to the correct box:

**Categories:**
- Key Systems
- Keyless Systems

**Items:**
- RCU (Receiver Control Unit)
- CCU (Chassis Control Unit)
- KCU (Keyless Control Unit)
- Max memorised keys: 4
- Max memorised keys: 3

---

## Slide 11 — Assessment: Differences in Components (Drag & Drop)

Which components belong to which immobiliser system? Drag to the correct box:

**Categories:**
- Keyed Immobiliser System
- Keyless Immobiliser System
- All Immobiliser Systems

**Items:**
- Passive Key
- Active Key
- KCU (or CCU)
- RCU
- TPMS function
- Electronic Steering lock
- Mechanical Steering lock
- LF Antenna
- Fuel Filler Cap
- Antenna Ring

---

## Slide 12 — Key Type Immobiliser Systems

Those models that rely on a physical key to turn the motorcycle on also use a transponder recognition system to ensure that a theft that relies on the overcoming the mechanical security of the key barrel will still be thwarted by a second, electronic layer of security that means critical functions (engine management and starting) will not respond.

---

## Slide 13 — Key System Details

Transponder in key 125KHz
Comms / paired with RCU (receiver control unit) / Immobiliser
Keys must be separated with RCU via antenna ring
Max 4 keys per bike (depending on model)
TPMS also is paired to the RCU (if fitted)
TDT required to pair keys / immobiliser / TPMS
Cut keys available to order from Triumph for certain models only (see epc for details). As a rule, generally smart 'keyless' keys do not have blank key blade support, whereas immobilisers and seat locks do.
If all keys lost, replacement immobiliser, keys and lockset will be required

---

## Slide 14 — Keyless Intro

Many models are now available with a keyless ignition system, where the motorcycle can be turned on without having to insert the key in a traditional ignition switch.
The rider carries the actual key with them in proximity to the motorcycle, which has two low frequency antennae that can detect the UHF radio frequency emitted by the key.
Typically this function is controlled by a dedicated control module that is connected to the CAN bus: The KCU (keyless control unit)*
* Some early Tiger 1200 models incorporated the function into the CCU (chassis control unit)

---

## Slide 15 — [DRAFT ARTEFACT — DISCARD]

> ⚠ Visual review confirms this is an unfinished draft: the SME copy-pasted the same paragraph into three floating text boxes at different positions across the canvas while assembling the content. Not a finished slide. All real content appears on slides 16 and 17 — design from those instead.

---

## Slide 16 — Key to Control Unit Communication

> Visual review: slide has photos of both key types (non-smart traditional key left, smart oval fob right) plus four content blocks. Design uses real key photos as assets.

The key recognition process is initiated by the KCU energising the external LF antenna(e). There are two methods of communication from the key to the KCU, either via UHF (for "smart" keys) or LF (as a backup method for "smart" keys and used for "non-smart" keys).

The key recognition process must remain transparent for the rider, and therefore the time taken to authenticate the key should be as short as practicable. The overall time before the key authentication result is available should be a maximum of approximately 5 seconds. The nominal time before the key authentication result is available however is 200ms.

The first key identification process should be of "smart" keys (via UHF, then LF), followed by any paired "non-smart" keys (via LF only). In addition, if multiple LF antennas are present, the key identification process should poll for each key via each antenna, before attempting to identify a different key.

---

## Slide 17 — Key to Control Unit Communication: Point of Interest (LF vs UHF)

> Visual review: clean two-column layout. LF detail left, UHF detail right, summary sentence bottom. Standalone "Point of Interest" breakout slide.

**Point of interest –** In a motorcycle keyless ignition system, UHF (ultra-high frequency) and LF (low frequency) are two distinct communication bands.

LF, typically around 125 kHz, is used for the initial authentication, as it offers better range for close-proximity detection and is less prone to interference.

UHF, either 315 or 434 MHz range, is used for active communication once the system is engaged, allowing for longer range and more secure data transfer.

In short, LF handles proximity sensing, while UHF supports the ongoing communication once the key is near.

---

## Slide 18 — Assessment: Keyless Ignition Q1 (MCQ)

**Question:** What allows a rider to start a motorcycle fitted with a keyless ignition system?

**Options:**
- The key transmits its identity wirelessly. ✅
- The ignition switch reads a magnetic strip inside the key.
- The motorcycle stores the rider's fingerprint.
- The key must physically fit into the barrel of the ignition switch and the teeth be in the correct format.

**Feedback:** Correct. The key communicates wirelessly with the motorcycle when it is within range.

---

## Slide 19 — Assessment: Keyless Ignition Q2 (MCQ)

**Question:** Which of the following are involved in recognising a valid key? (Select all that apply.)

**Options:**
- ✅ LF antenna(s)
- ✅ The key (transponder)
- ✅ Keyless Control Unit (KCU)
- Engine oil pressure switch
- Clutch switch

**Feedback:** The LF antenna initiates communication, the key responds, and the KCU authenticates the key before allowing operation.

---

## Slide 20 — Assessment: Keyless Ignition Q3 (MCQ)

**Question:** What is the purpose of the communication between the key and the KCU?

**Options:**
- To check the key is of the correct type.
- To exchange a mutual authentication before enabling the system. ✅
- To upload service history to the motorcycle.
- To synchronise the instruments.

**Feedback:** Correct. The motorcycle only enables operation after successfully authenticating the key.

---

## Slide 21 — Example: Keyless System Ignition-On Process

YELLOW – What customer perceives as being the state of bike. BLUE – Actual state of bike.

1. User presses either "power" or "start" button
2. Keyless control unit (KCU) wakes up
3. KCU checks for recognised key being available and for matching ESL identification.
4. If the KCU finds a recognised key and confirms the ESL identification, it will apply power to the "12v ignition" input to all other components
5. All other components wake up simultaneously, except ECU which will only wake up if the kill switch is in the "run" position
6. When ECU wakes, it queries key authentication state from KCU (KCU responds key is authenticated)
7. ECU and KCU then exchange security keys as final step of immobiliser functionality
8. If ECU-KCU exchange is OK, engine can be started.

---

## Slide 22 — Wake Up Sequence Diagram

Wake Up Sequence – note don't mix item number up with stage number (Use with previous slide)

**System components:**
1. Transponder chip
2. Electronic steering lock
3. LF Antenna (front)
4. Keyless ECM
5. Engine ECM
6. LF Antenna (rear)
6. Ignition Circuit (12v controlled via KCU)

Power Button / Run Position / Check

> ⚠ Diagram slide — numbered components with stage flow. Pairs with slide 21.

---

## Slide 23 — Important Note: 90-Second Ignition Timeout

If passive key is used to power the bike up, then a 90 second time limit is applied to the ignition supply. Therefore, if a download is started in this scenario it may fail.
Same applies if smart key goes out of range.

Example: if a rider switches his ignition on using his passive key in close proximity to LF antenna and then removes the key away from the LF antenna, 90 seconds later the ignition will turn itself off. Similarly, if a rider switches the ignition on using his smart key and then walks away with the smart key, outside of the one metre proximity range, for more than 90 seconds, then again, the calibration strategy will switch the ignition off.

Technicians should be aware of this, especially during downloads, as if the ignition switches itself off during the download stage it will automatically fail the download

---

## Slide 24 — Key Pairing

Both types of key have transponders that have a unique code which the immobiliser system must recognise as being an authorised key. This is called key pairing.

Keys supplied with the motorcycle from new will obviously already be paired, but it may be necessary to pair other keys to the immobiliser system (either in the immobiliser, the RCU, the KCU or the CCU, depending on the model and the system it uses).

This is done using the TDT (Triumph Diagnostic Tool).

---

## Slide 25 — Key Pairing Note: Add New Key vs Re-Register All Keys

The Add New Key function allows the user to pair one key to the immobiliser system at a time, provided the maximum number of paired keys has not been reached. An attack delay of 5 minutes must pass for each key pairing for security.

The Re-Register All Keys function erases all keys from immobiliser system memory, except the key used to turn the motorcycle ignition ON at the start of the process. The function then allows multiple keys to be paired, up until the maximum number of allowed keys has been reached. An attack delay of 5 minutes must pass for each key pairing. On some motorcycles, an attack delay of 5 minutes must also pass before existing key pairings can be erased.

---

## Slide 26 — General Key and Keyless Information Points (commonly overlooked)

All of the motorcycle's available keys should be obtained before performing any key pairing operations. Starting a key pairing operation without having obtained all of the motorcycle's keys will render any spare keys inactive. In some circumstances, absent spare keys may also be rendered permanently unusable.

Lost or unwanted keys can be erased, and additional/replacement keys added using the Triumph Diagnostic Tool.

A maximum of three keys can be paired to the KCU/CCU at any one time. This can be any combination of smart keys and passive keys. It is not possible to pair further keys when the maximum of three paired keys is reached.

When pairing a combination of smart keys and passive keys, it is recommended that any smart keys are paired first, followed by the passive keys.

A paired key can have three different states, active, inactive and erased.

Once a key is paired it is regarded as active. At this point the key is permanently locked to its paired keyless ECM and cannot be paired to any other keyless ECM – ever!

A paired key is required to allow the motorcycle to power ON in order to perform key pairing operations. All available paired keys should be obtained before starting these operations.

Paired keys can be erased using the Re-Register All Keys function on the Triumph diagnostic tool. When this function is used, the key being used to power the motorcycle will remain paired and active. Any other paired keys will be registered as inactive.

---

## Slide 27 — General Information Points (continued)

Note: Keys pair to RCU, CCU or KCU (aka Immobiliser) depending on model — This is covered in a later section

When using the Re-Register All Keys function, a ten minute (600 second) security time delay is applied to the first key pairing. Further key pairings are subject to a five minute (300 second) time delay.

Inactive keys can be either paired and reactivated, or replaced by new keys and overwritten.

Any inactive keys that are overwritten are then stored as erased in the keyless ECM memory. A maximum of three erased keys can be stored.

Erasing more keys after the maximum of three erased keys has been reached, will result in the erased keys being overwritten. Erased keys that are overwritten are then rendered permanently unusable.

Stored erased keys can be paired and reactivated providing that the maximum number of three paired keys has not been reached. When a key is reactivated, it is moved from its 'erased' memory slot to a vacant 'active' memory slot.

Note: Only rear LF antenna can be used to pair keys

---

## Slide 28 — Assessment: Key Pairing Q1 (MCQ)

**Question:** What tool is used to erase or add keys to the keyless ECM?

- A. Triumph diagnostic tool ✅
- B. Dealer mode on the instrument panel
- C. The keyless ECM automatically learns new keys
- D. The immobiliser antenna programming tool

---

## Slide 29 — Assessment: Key Pairing Q2 (MCQ)

**Question:** What is the maximum number of keys that can be paired to the keyless ECM?

- A. One
- B. Two
- C. Three ✅
- D. Unlimited, until the ECM memory is full

---

## Slide 30 — Assessment: Key Pairing Q3 (MCQ)

**Question:** Why is it recommended to pair smart keys before passive keys?

- A. Smart keys must be paired first to maintain the correct pairing order. ✅
- B. Passive keys prevent smart keys from being recognised later.
- C. Smart keys require a fully charged motorcycle battery before pairing.
- D. Passive keys can only be paired after the motorcycle has been started.

---

## Slide 31 — Assessment: Key Pairing Q4 (MCQ)

**Question:** A technician attempts to pair a key that has previously been paired to another keyless ECM. What should they expect?

- A. The key will pair normally after deleting it from the old motorcycle.
- B. The key can be paired if the battery is removed first.
- C. The key cannot be paired because it is permanently locked to its original ECM. ✅
- D. The key will pair after cycling the ignition three times.

---

## Slide 32 — Assessment: Key Pairing Q5 (MCQ)

**Question:** After selecting "Re-Register All Keys", how long is the security delay before the first key can be paired?

- A. 60 seconds
- B. 5 minutes
- C. 10 minutes (600 seconds) ✅
- D. 30 minutes

---

## Slide 33 — Key Signal Function Test (TDT)

The key signal function test can be used on models with keyless ignition.
The function test can be started by clicking the Start button.
When started, the function test will periodically check for detected keys. The test provides three coloured lights for the following:
- UHF (Ultra High Frequency key detection)
- LF (Low Frequency key detection)
- LF Antenna (LF Antenna Status)

The status reported by the coloured lights is refreshed every 2 to 3 seconds while the function test is running.

The coloured light and text displayed in the status bar at the bottom of the Test Details screen will alternate between displaying the test status and test results as follows:
- Amber = Test running
- Red = No keys detected
- Green = Key detected (by either UHF or LF)

The test can be stopped at any time by clicking the Stop button.

Key Signal Function Test – Keyless Ignition Models

---

## Slide 34 — UHF Key Detection

The UHF coloured light provides indication of whether or not a paired, active smart key is being detected by the motorcycle's keyless ignition system. The smart key must be paired to the keyless ECM, and must be in Active mode to be detected by UHF.

Paired smart keys can typically be detected at a range of up to one metre from the motorcycle when in active mode.

Note: The LF antennae detect UHF keys as well as the LF keys.

When the function test is running:
- A red light indicates that no key was detected by UHF method at the last attempt.
- A green light indicates that a paired, active smart key was detected by UHF method at the last attempt.

UHF Key Detection

---

## Slide 35 — LF Key Detection + LF Antenna Status

**LF Key Detection**
The LF coloured light provides indication of whether a compatible key is being detected by the LF antenna.
The LF antenna will detect any key that is compatible with keyless ignition, regardless of whether or not the key has been paired with the keyless ECM.
Compatible keys must be placed in close proximity of the LF antenna (typically within 25 mm) to be detected.

When the function test is running:
- A red light indicates that no key was detected by the LF antenna at the last attempt.
- A green light indicates that a compatible key was detected by the LF antenna at the last attempt.

**LF Antenna Status**
The LF Antenna light provides indication of the status of the LF antenna.

When the function test is running:
- A red light indicates that a LF antenna fault is present.
- A green light indicates that the LF antenna is functioning normally.

---

## Slide 36 — Cooker Knob / Isolator Switch Tip

Cooker Knob Isolator Switch – Ignition Master Switch Link

Useful Tip:
US models have an isolator switch.
Models outside of US have a loop-out plug.

---

## Slide 37 — Key Pairing Failure: Possible Causes

Key pairing failure possible causes:
- Key pairing can take time to see new key / metal side away from LF antenna. Maybe dismount antenna. Persevere!
- Front antenna only there for keyless range around bike
- Note battery tenders may affect key pairing due to electrical noise etc…

---

## Slide 38 — Important Keyless Notes: 30-Second TDT Window

Bike will allow TDT connection to immobiliser diagnostics for 30 seconds without a key present. It allows connection window of 30 secs but once connected it will stay connected.
So KCU will wake with no key but only gives access to TDT Immobiliser diagnostics.
NB Immobiliser light sequence flashes (see table)

---

## Slide 39 — Instrument Panel Flash Sequences [PLACEHOLDER]

No text content. Flash sequence table — image/diagram only.

---

## Slide 40 — TPMS

The Tyre Pressure Monitoring System (TPMS) function is incorporated into the RCU, Immobiliser, CCU or KCU, depending on the model.
In short, whichever control unit contains the immobiliser function.

---

## Slide 41 — TPMS Operation

Tyre Pressure Monitoring System (TPMS) Description

⚠️ WARNING
The tyre pressure monitoring system is not to be used as a tyre pressure gauge when adjusting the tyre pressures. For correct tyre pressures, always check the tyre pressures when the tyres are cold using an accurate tyre pressure gauge.

Use of the TPMS system to set inflation pressures may lead to incorrect tyre pressures, leading to loss of motorcycle control and an accident.

Owners must only adjust tyre pressures when the tyres are cold using an accurate tyre pressure gauge and must not use the tyre pressure display on the instruments.

The tyre pressures shown on the instrument panel indicate the actual tyre pressure at the time of selecting the display. This may differ from the inflation pressure set when the tyres are cold because tyres become warmer during riding, causing the air in the tyre to expand and the pressure to increase. The cold inflation pressures specified by Triumph take account of this.

The TPMS will not transmit the tyre pressure data until the motorcycle is travelling at a speed greater than 12 mph (20 km/h). Two dashes will be visible in the display area until the tyre pressure signal is received.

**TPMS Components:**
Instruments – Used to display the tyre pressure value, the tyre symbol, and the TPMS warning light.
Immobiliser Control Unit – Receives the data from the tyre pressure sensors and sends the information to the instrument pack.
Tyre pressure sensor – Situated inside the front and rear wheel. Each sensor has its own unique ID number and must be recorded in the spaces provided in the Owner's Handbook. These sensors measure the air pressure inside the tyre and transmit pressure data to the instruments.
The wheel sensor is a sealed unit and must not be opened. The battery inside the sensor is not replaceable and a new sensor must be fitted when the battery voltage becomes too low.

Pressures embedded in the calibration for specific model
Drop of 6psi = light on
315 MHz RF – JP key + TPMS
434 MHz RF – ROW key + TPMS

---

## Slide 42 — Keyed TPMS Pairing Flow [PLACEHOLDER]

Visual flow diagram only. No text content.

---

## Slide 43 — TPMS Data Screen

Note:
The wheel sensors go into a sleep mode seven minutes after the wheels become stationary. If the wheel sensors are in sleep mode, no data will be displayed against tyre pressure and temperature.
To wake the sensors, the bike must be ridden at a speed greater than 18 mph (30 km/h) for at least 30 seconds.

---

## Slide 44 — Key Frequencies: 2 Different Frequencies

2 x different frequencies and part numbers to suit – Keys
Care must be taken to ensure that the correct frequency is ordered for the correct model. It is recommended to use VIN lock EPC.

---

## Slide 45 — TPMS Questions (Q&A Reference)

**Q:** Why should tyre pressures always be checked when the tyres are cold?
**A:** Because tyres become warmer during riding, causing the air to expand and the pressure to increase.

**Q:** What might happen if you use the TPMS system to set inflation pressures?
**A:** It may lead to incorrect tyre pressures, which can result in loss of motorcycle control and an accident.

**Q:** At what speed will the TPMS transmit tyre pressure data?
**A:** When the motorcycle is travelling at a speed greater than 12 mph (20 km/h).

**Q:** What is the purpose of the tyre pressure sensor inside the wheels?
**A:** Each sensor measures the air pressure inside the tyre and transmits the pressure data to the instruments.

**Q:** Why must the wheel sensor not be opened or replaced except when the battery is too low?
**A:** Because the wheel sensor is a sealed unit; the battery inside is not replaceable, and a new sensor must be fitted when the battery voltage drops.

---

## Slide 46 — Case Study Storyboard Part 1 [SME NOTES]

**Situation:**
A customer comes to his bike, the bike will not power on as normal, does not crank or start, nor do the instruments illuminate, the electronic steering lock is fully engaged and will not disengage.
They take the bike to the dealer for diagnostics (on the back of a truck!)

2. The dealer inspects the bike, and should be given a selection of possible options / approaches as steps to resolve the situation.
- Replace the bike battery
- Replace key fob
- Conduct a download
- Replace the electronic steering lock
- Replace the keyless control unit
- Replace the instrument pack
- or other

3. The 'other' options should include 'reading' the immobiliser flash sequence on the instruments. Include further incorrect answers also such as:
- Replace key fob battery
- Replace wiring to KCU
- Replace the starter switch gear
- Check switch gear connection etc

If correct answer is chosen as an option, then the flash sequence table should be illuminated.
Inform user at this stage: The flash sequence seen on bike is 1 long flash plus 3 short flashes.
The technician should then be given a list of options of what this means — various reasons may be given, they need to choose the right one from the table.

---

## Slide 47 — Case Study Storyboard Part 2 [SME NOTES]

**Q** – Where can techs find this info?
- TOL
- Owners handbook
- Internet, it's a generic code
- Ask others
- In the manual
- From TTI

4. The next option the dealer should be given is how to access further information / DTC about this flash sequence using only the triumph diagnostic tool as the bike doesn't power on?

The options should include:
- This is not possible, as steering lock is inoperative and the instruments won't switch on
- This is not possible unless the electronic steering lock is replaced
- This is not possible unless the instrument is replaced or swapped
- This is possible following a complete download to the KCU
- This is possible for just for a 30 second 'window'; once a connection has been made and established, the connection will continue.

5. Once connection is established, the technician finds the DTC reads C1137 – use the DTC table to determine the cause and remedy
6. The technician should then have to list the correct repair from the table. Reminder to use link from DTC to service manual for access to the fault finding table (if supported by that model).

---

## Slide 48 — Case Study Storyboard Part 3 [SME NOTES]

Bonus Question: one chance at getting right only! But correct answer to be given following the attempt.
Hypothesise on a second related problem.

**Q** – If the same symptom scenario occurred, BUT no TDT access to KCU was possible (i.e. for the 30 sec window), also no flash sequence on instruments (only the standard immobiliser sequence). What could this mean?

**A** = Likely KCU not seeing input from switch gear.

Include incorrect answers like:
- Instruments may have incorrect software
- The LED in the instruments might be inoperative
- A theft relay attack may have occurred and the bike has automatically shut down
- The TDT software is out of date and requires updating

Once correct answer selected, the answer can be expanded on i.e.: Possible Inoperative start switch/button or poor connection to start switch/button. Techs should get multi meter to check switch operation, as this would be the only way to check correct operation and circuit connection (i.e. TDT diagnostics not possible in this instance).

---

## Slide 49 — Instrument Panel Flash Sequences [PLACEHOLDER]

Flash sequence table — image/diagram only.

---

## Slide 50 — Case Study DTC Table [PLACEHOLDER]

Case Study situation DTC table – (AR note – any DTC can apply but not ones with red line)
Image/table only.

---

## Slide 51 — Case Study: Wiring Diagram / Component Reference [PLACEHOLDER]

Keyless Ignition and Immobiliser System CASE STUDY

Component reference:
1. Fuse box 1
2. Electronic steering lock
3. Electronic steering lock connector
4. Instruments
5. Engine subharness
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

---

## Slide 52 — Keyless Facts for Diagnostics (Section Intro)

The following questions all have useful to remember answers.
The answers to the following questions can be found in the attached PDF document [LINK]

Keyless Facts for Diagnostics

---

## Slide 53 — Keyless Facts Q1

**Q1.** How often do the smart key and KCU contact each other?

- A. Once, during start-up only. ✅
- B. Every 30 seconds while the ignition is on.
- C. Continuously whenever the key is nearby.
- D. Every time the rider touches the handlebars.

---

## Slide 54 — Keyless Facts Q2

**Q2.** If communication fails, how is this indicated?

- A. The immobiliser LED flashes the appropriate sequence. A "Key not found" message is not displayed. ✅
- B. The TFT immediately displays "Key not found."
- C. The engine stops immediately.
- D. The horn sounds repeatedly until the key is found.

---

## Slide 55 — Keyless Facts Q3

**Q3.** How is a "Key not found" message cleared while the engine is running?

- A. Once communication is restored, the message no longer appears. ✅
- B. Switch the ignition off and back on.
- C. Hold the joystick centre button for five seconds.
- D. Remove and refit the smart key battery.

---

## Slide 56 — Keyless Facts Q4

**Q4.** What message is displayed when starting the motorcycle using a passive key (or a smart key operating in passive mode)?

- A. No error message is displayed. ✅
- B. "Passive key detected."
- C. "Key battery low."
- D. "Limited key mode."

---

## Slide 57 — Keyless Facts Q5

**Q5.** A rider starts the motorcycle using a smart key, then switches it into passive mode to conserve the key battery. What happens?

- A. No error message is shown. However, the motorcycle will not restart after the ignition is switched off. ✅
- B. The engine stops immediately.
- C. A "Key battery low" warning appears.
- D. Passive mode is cancelled automatically.

---

## Slide 58 — Keyless Facts Q6

**Q6.** Which statement about the CR2032 battery used in Triumph keyless fobs is correct?

- A. It is a 3 V battery with a 2 V service limit. ✅
- B. It is a 1.5 V battery that should be replaced below 1 V.
- C. It is a rechargeable 3.7 V lithium battery.
- D. Battery voltage is measured with no electrical load applied.

---

## Slide 59 — Keyless Facts Q7

**Q7.** What DTC is logged if the key battery voltage falls below the 2 V service limit?

- A. No DTC is logged. ✅
- B. Immobiliser communication fault.
- C. Low battery DTC stored in the KCU.
- D. CAN communication fault.

---

## Slide 60 — [DUPLICATE of Slide 59]

Identical to slide 59. Drop one.
