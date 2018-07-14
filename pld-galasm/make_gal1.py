PINS=["/IOREQ", "/WR", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "GND",
      "M1", "/LCDWRCS", "/PIOCS", "/DISPBKCS", "/DISPDPCS", "/DISP4CS", "/DISP3CS", "/DISP2CS", "/DISP1CS", "VCC"]

ADDRS={"/DISP1CS": (0x00, 7),
       "/DISP2CS": (0x02, 7),
       "/DISP3CS": (0x04, 7),
       "/DISP4CS": (0x06, 7),
       "/DISPDPCS": (0x08, 7),
       "/DISPBKCS": (0x0A, 7),
       "/PIOCS": (0x88, 6),
       "/LCDWRCS": (0x0B, 7)}

READONLY=[]
WRITEONLY=["/DISP1CS", "/DISP2CS", "/DISP3CS", "/DISP4CS", "/DISPDPCS", "/DISPBKCS"]
NO_M1=["/SIOCS", "/CTCCS"]

from write_gal import write_gal

write_gal("Z80SBC_2", PINS, ADDRS, READONLY, WRITEONLY, NO_M1)
