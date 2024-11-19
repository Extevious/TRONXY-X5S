<b>Enable extra low-level configuration options</b> : TRUE

<b>Micro-controller Architecture</b> : STMicroelectronics STM32

<b>Processor model</b> : STM32F103

<b>Bootloader offset</b> : 28KiB bootloader

<b>Clock Reference</b> : 8 MHz crystal

<b>Communication interface</b> : USB (on PA11/PA12)

<b>GPIO pins to set at micro-controller startup</b> : !PA14

The "make flash" command does not work on the SKR mini E3. Instead,
after running "make", copy the generated "out/klipper.bin" file to a
file named "firmware.bin" on an SD card and then restart the SKR
mini E3 with that SD card.
