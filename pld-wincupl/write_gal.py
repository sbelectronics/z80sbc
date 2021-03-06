NOT_CHAR="!"
AND_CHAR="&"

AND_TERM=" " + AND_CHAR + " "

def compute_addr(addr):
    (addr, bits) = addr
    parts = []
    for i in range(0,bits):
       bit=7-i
       if (addr & 0x80):
          parts.append("A%d" % bit)
       else:
          parts.append(NOT_CHAR+"A%d" % bit)
       addr = addr << 1
    return AND_TERM.join(parts)

def compute_addr_range(addr):
    (addr, bits) = addr
    return "%02X-%02X" % (addr, addr + ((1<<(8-bits)) -1))

def write_gal_old(name, pins, addrs, readonly, writeonly, no_m1):
    print "GAL16V8   ; Works with GAL16V8 and ATF16V8"
    print "%-10s; Autogenerated" % name 

    print ""

    for pin in pins[:10]:
#        if "CS" in pin:
#            pin=pin[1:]
        print "%-10s" % pin,

    print ""

    for pin in pins[10:]:
#        if "CS" in pin:
#            pin=pin[1:]
        print "%-10s" % pin,
    print ""

    print ""

    for pin in pins:
        if "CS" in pin:
#            dpin=pin[1:]
            dpin=pin
            if pin in readonly:
                print dpin, "=", compute_addr(addrs[pin]), "* /RD * /IOREQ * M1"
            elif pin in writeonly:
                print dpin, "=", compute_addr(addrs[pin]), "* /WR * /IOREQ * M1"
            elif pin in no_m1:
                print dpin, "=", compute_addr(addrs[pin])
            else:
                print dpin, "=", compute_addr(addrs[pin]), "* /IOREQ * M1"

    print ""

    print "DESCRIPTION"

    print ""

    for pin in pins:
        if "CS" in pin:
            print "Chip Select %s at addresses" % pin, compute_addr_range(addrs[pin]),
            if pin in readonly:
                print "RDONLY",
            if pin in writeonly:
                print "WRONLY",
            print ""

def write_gal(name, pins, addrs, readonly, writeonly, no_m1):
    print "name %s;" % name.replace("_",'-').lower()
    print "device g16v8;"
    print "partno x;"
    print "date 1/1/1980;"
    print "designer smbaker;"
    print "company sbsoftware;"
    print "revision 1;"
    print "assembly x;"
    print "location x;"

    print ""

    for i,pin in enumerate(pins,1):
        if (pin == "/RD"):
            pin="RD"
        if (pin == "/WR"):
            pin="WR"
        if (pin == "/IOREQ"):
            pin="IOREQ"
        print "PIN %d = %s;" % (i, pin.replace("/","!"))

    print ""

    for pin in pins:
        if "CS" in pin:
            addr=addrs[pin]
            dpin=pin[1:]
            if pin in readonly:
                print dpin, "=", compute_addr(addr), "& !RD & !IOREQ & M1 ;"
            elif pin in writeonly:
                print dpin, "=", compute_addr(addr), "& !WR & !IOREQ & M1 ;"
            elif pin in no_m1:
                print dpin, "=", compute_addr(addr), ";"
            else:
                print dpin, "=", compute_addr(addr), "& !IOREQ & M1 ;"

    print ""

    for pin in pins:
        if "CS" in pin:
            addr = addrs[pin]
            print "/* Chip Select %s at addresses" % pin, compute_addr_range(addr),
            if pin in readonly:
                print "RDONLY",
            if pin in writeonly:
                print "WRONLY",
            print "*/"

