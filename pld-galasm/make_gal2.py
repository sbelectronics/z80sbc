PINS=["/IOREQ", "/RD", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "GND",
      "M1", "/LCDRDCS", "/SPARECS", "/CTCCS", "/SIOCS", "/PGREGCS", "/KCS3", "/KCS2", "/KCS1", "VCC"]

ADDRS={"/KCS1": (0x00, 7),
       "/KCS2": (0x02, 7),
       "/KCS3": (0x04, 7),
       "/PGREGCS": (0x70, 5),
       "/SIOCS": (0x80, 6),
       "/CTCCS": (0x84, 6),
       "/SPARECS": (0xB0, 7),
       "/LCDRDCS": (0x0B, 7)}

READONLY=["/KCS1", "/KCS2", "/KCS3"]
WRITEONLY=[]
NO_M1=["/SIOCS", "/CTCCS"]

from write_gal import write_gal

write_gal("Z80SBC_2", PINS, ADDRS, READONLY, WRITEONLY, NO_M1)
