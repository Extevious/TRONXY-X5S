## TRONXY X5S SETUP AND CONFIG

For anyone that is using this as a reference, feel free to leave feedback on optimizations, fixes, features, or general ideas/comments.

## MAINSAIL/KLIPPER

### BIGTREETECH SKR Mini E3 V2.0

| Properties                                       | Values                     |
| ------------------------------------------------ | :------------------------- |
| **Enable extra low-level configuration options** | `true`                     |
| **Micro-controller Architecture**                | `STMicroelectronics STM32` |
| **Processor model**                              | `STM32F103`                |
| **Bootloader offset**                            | `28KiB bootloader`         |
| **Clock Reference**                              | `8 MHz crystal`            |
| **Communication interface**                      | `USB (on PA11/PA12)`       |
| **GPIO pins to set at micro-controller startup** | `!PA14`                    |
|                                                  |                            |

> **Note:** The "make flash" command does not work on the SKR Mini E3 V2. Instead,
> after running "make", copy the generated "out/klipper.bin" file to a
> file named "firmware.bin" on an SD card and then restart the SKR
> mini E3 with that SD card.

---
