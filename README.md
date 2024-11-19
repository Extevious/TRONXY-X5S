Board : STM32F103
Bootloader : 28KiB
and USB communication : TRUE
Enable extra low-level configuration options : TRUE
GPIO pins to set at micro-controller startup : !PA14

The "make flash" command does not work on the SKR mini E3. Instead,
after running "make", copy the generated "out/klipper.bin" file to a
file named "firmware.bin" on an SD card and then restart the SKR
mini E3 with that SD card.
