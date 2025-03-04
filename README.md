## TRONXY X5S SETUP AND CONFIG

For anyone that is using this as a reference, feel free to leave feedback on optimizations, fixes, features, or general ideas/comments.

## KLIPPER

Instead of updating the .cfg files directly through a web UI (such as Mainsail), this git repo is used.

### First-time setup:

1. `ssh` into the host using a linux terminal, such as WSL or a device running a linux distro.
2. Install the `git` package using a package manager (if it doesn't already exist).
3. `cd` into the directory with all the klipper .cfg files, ex: `cd printer_data/config`.
4. `git clone` this repo.
5. Import the `main.cfg` file in `printer.cfg`, or import individual files manually.
6. Optional: `git checkout Testing` to switch to the `Testing` branch.
7. Issue a `RESTART` in the web UI.

### Updating files when changes are made to this repo:

1. `ssh` into the host using a linux terminal, such as WSL or a device running a linux distro.
2. `cd` into the directory that was created when this repo was cloned, ex: `cd printer_data/config/TRONXY-X5S`.
3. `git pull -r` all files.
4. Issue a `RESTART` in the web UI.

### BIGTREETECH SKR Mini E3 V2.0

| Properties                                       | Values                     |
| ------------------------------------------------ | -------------------------- |
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
