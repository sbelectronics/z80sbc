# Scott's Z80SBC

(c) Scott M Baker, smbaker@smbaker.com

## Description

This is a Z80 Single Board Computer with the following features:

* Z80 CPU
* RC-2014 Compatible Expansion Connector
* Eight TIL311 Displays, or a 2x16 LCD/VFD Module
* 20-Key Keypad for cherry MX Blue Keyswitches
* Two serial ports (Z80 SIO/2)
* 24-bit Parallel IO Connector (Z80 PIO)
* Counter/Timer chip, optionally usable as a baud rate generator for the SIO/2
* 512 KB of banked RAM
* 512 KB of banked ROM
* Single stepper, with automated slow stepping feature
* Flexible IO address decoding using programmable logic devices

As the Z80 is only able to address 64KB or memory, the RAM and ROM are banked. Typically the excess is used as a ROM disk and RAM disk when running the RomWBW CPM distribution.

## Resources

The following github repositories will be useful:

* [http://www.smbaker.com/scotts-z80sbc-z80-single-board-computer](http://www.smbaker.com/scotts-z80sbc-z80-single-board-computer), project website
* [https://github.com/sbelectronics/z80sbc](https://github.com/sbelectronics/z80sbc), Scott's Z80SBC repository containing schematics, code for the programmable logic devices, etc.
* [https://github.com/sbelectronics/RomWBW](https://github.com/sbelectronics/RomWBW), my fork of the RomWBW CP/M distribution.

## Schematics

The schematics are available in the schematics directory for the github repo.

* [Schematic revision 0.20](https://github.com/sbelectronics/z80sbc/blob/master/schematics/z80sbc-0.20.pdf)

## Acknowledgments

Sergey Kiselev's Zeta-2 Single Board computer was used as the inspiration for several parts of this designed, including the banked memory scheme. 

The RomWBW CP/M distribution was essential in getting CP/M running on this board.