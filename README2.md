Exoskeleton Hand for Stroke Patient (Micropython Code)

Group Project for my First Year at Manchester Metropolitan University

# Project Brief 

  - Design and manufacture an exoskeleton hand for a stroke patient's weak / non working hand so they can successfully pick up, hold, and place down an object. For our cohort the hand had to be capable of grabbing a paper cup.

# How it works

  - It works by a motor contracting, pulling elastic threaded through 3D printed rings sewn onto the palm of a glove. This causes the fingers to curl around the paper cup and grab it.

# What the code does
  
  - The code is a fixed sequence that plays when the device is switched on:
  - 1. The device waits 5 seconds to allow time to make sure the hand is positioned correctly
  - 2. A motor then spins at a set speed to turn a gear which pulls the elastic, retracting it into its housing and curling the fingers inwards for 3 seconds
  - 3. The process then waits for 5 seconds
  - 4. The motor then spins in the opposite direction at the same speed for the another 3 seconds so the hand returns to its original position
  - 5. The process then stops.

# Hardware used

  - Raspberry Pi Pico
  - LM317T Voltage Regulator
  - L298N Motor Driver
  - 4 x AA Battery Power supply
  - DC Motor

# How to run

  - Load the 'main code.py' file onto the Raspberry Pi Pico (eg. by uploading it using Thonny IDE)
  - The code will run automatically when the device is powered on

# What Went Wrong

  - As the project was being assembled towards the end of our time frame, the motor driver was destroyed due to incorrect placement of capacitors.
  - This meant the code could not be tested with a motor

# How we overcame the issue

  - We instead had to come up with a makeshift version of the hand that closed when it was powered on, then we took the batteries out and flipped them round, reversing the DC Motor's polarity meaning it would spin in the opposite direction and open the hand back up
  
# Result

  - The hand did grip the paper cup, lift it up, and release it

# Limitations and Improvements

  - We were limited by a lack of time to test parts, resulting in not having the time to replace parts when they failed
  - We could have improved the project by adding sensors so the hand automatically gripped the cup instead of needing a manual input

# My contribution

  - I wrote all of the code to move the motors
  - I tested the timings with the small LED on the Raspberry Pi Pico, the LED turning on was when the motor would spin, and turned off when it would stop
  - I assisted in soldering the electronics together and connecting them to the breadboard
  - I assisted in designing the cogs and the gearbox casing for the hand

