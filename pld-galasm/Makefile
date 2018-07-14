all: z80sbc-1.jed z80sbc-2.jed

z80sbc-1.pld:
	python ./make_gal1.py > z80sbc-1.pld

z80sbc-1.jed: z80sbc-1.pld
	/home/smbaker/projects/misc/GALasm/src/galasm z80sbc-1.pld

z80sbc-2.pld:
	python ./make_gal2.py > z80sbc-2.pld

z80sbc-2.jed: z80sbc-2.pld
	/home/smbaker/projects/misc/GALasm/src/galasm z80sbc-2.pld

clean:
	rm -f *.pld *.jed *.pin *.fus *.chp
