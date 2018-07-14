all: z80sbc-1.pld z80sbc-2.pld

z80sbc-1.pld:
	python ./make_gal1.py > z80sbc-1.pld

z80sbc-2.pld:
	python ./make_gal2.py > z80sbc-2.pld

clean:
	rm -f *.pld *.jed *.pin *.fus *.chp *.so *.pdf *.abs *.sim *.wo
