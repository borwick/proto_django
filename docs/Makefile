SOURCES := $(wildcard *.text)
FILES := $(SOURCES:.text=.html)
.PHONY: help clean all

help:
	@echo "options: clean all"

clean:
	-rm *.html

all: $(FILES)

%.html: %.text
	multimarkdown $< > $@
