PYTHON ?= python3
MEDIA_ROOT := ./_media
MPLCONFIGDIR := $(abspath _out/matplotlib)
FIGURE_SOURCE_ROOT := past-exam-of-the-mathematics-course-of-the-university-of-cambridge
FIGURE_SOURCES := $(shell find $(FIGURE_SOURCE_ROOT) -type f -name '*.py' | sort)
FIGURES := $(addprefix $(MEDIA_ROOT)/,$(FIGURE_SOURCES:.py=.png))

.PHONY: all clean media

all: media

media: $(FIGURES)

# The phase trajectory reuses the adjacent transport-model generator.
$(MEDIA_ROOT)/$(FIGURE_SOURCE_ROOT)/2013/iii/paper-71-phase-trajectory.png: $(FIGURE_SOURCE_ROOT)/2013/iii/paper-71-phase-trajectory.py $(FIGURE_SOURCE_ROOT)/2013/iii/paper-71-fields.py

$(MEDIA_ROOT)/%.png: %.py pyproject.toml Makefile
	mkdir -p -- ./$(dir $@)
	mkdir -p $(MPLCONFIGDIR)
	cd ./$(dir $@) && MPLBACKEND=Agg MPLCONFIGDIR=$(MPLCONFIGDIR) $(PYTHON) $(abspath $<)

clean:
	rm -f -- $(FIGURES)
