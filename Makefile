
LIST= rich -n -w 88 -F


MODULES= cli/00-dump-argv/ cli/10-argv cli/20-argparse cli/30-typer

MAINS= ${MODULES:=/__main__.py}

LISTINGS= 00-main.rich 10-main.rich 20-main.rich 30-main.rich

all: $(LISTINGS)

00-main.rich: cli/00-dump-argv/__main__.py
	$(LIST) $< > $@


10-main.rich: cli/10-argv/__main__.py
	$(LIST) $< > $@


20-main.rich: cli/20-argparse/__main__.py
	$(LIST) $< > $@


30-main.rich: cli/30-typer/__main__.py
	$(LIST) $< > $@


clean:
	/bin/rm -f *.rich
