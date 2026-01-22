tag=$(shell grep version setup.py | cut -d"'" -f2)

usage:
	@echo Usage:
	@echo
	@echo make tag - tag $(tag) and push

tag:
	git tag -a $(tag) -m 'tag $(tag)'
	git push --follow-tags
