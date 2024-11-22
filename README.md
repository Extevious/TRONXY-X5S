# MAINSAIL/KLIPPER

### BIGTREETECH SKR mini E3 V2.0

**Enable extra low-level configuration options** : _true_

**Micro-controller Architecture** : _STMicroelectronics STM32_

**Processor model** : _STM32F103_

**Bootloader offset** : _28KiB bootloader_

**Clock Reference** : _8 MHz crystal_

**Communication interface** : _USB (on PA11/PA12)_

**GPIO pins to set at micro-controller startup** : _!PA14_

**_Note:_** _The "make flash" command does not work on the SKR mini E3. Instead,
after running "make", copy the generated "out/klipper.bin" file to a
file named "firmware.bin" on an SD card and then restart the SKR
mini E3 with that SD card._
