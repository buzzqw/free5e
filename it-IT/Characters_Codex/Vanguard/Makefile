TEXINPUTS := ../../../tools/latex/dnd//:
LATEX := TEXINPUTS=$(TEXINPUTS) lualatex

.PHONY: all clean

all: Vanguard.pdf

Vanguard.pdf: Vanguard.tex
	mkdir -p build
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=build Vanguard.tex
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=build Vanguard.tex
	cp build/Vanguard.pdf Vanguard.pdf

clean:
	rm -rf build Vanguard.pdf
