
LIST= rich -ng -w 80 -a heavy -F


SRC= cli/example0/__main__.py \
     cli/example1/__main__.py \
     cli/example2/__main__.py

LISTINGS= example0.rich example1.rich example2.rich

all: $(LISTINGS)

example0.rich: cli/example0/__main__.py
	$(LIST) $< > $@

example1.rich: cli/example1/__main__.py
	$(LIST) $< > $@

example2.rich: cli/example2/__main__.py
	$(LIST) $< > $@

#.py.rich: 
#	$(LIST) $< > $@

