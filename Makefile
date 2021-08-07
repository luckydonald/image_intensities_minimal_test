MY_VAR := ${shell cat image_intensities/VERSION.txt}

clean:
	rm --verbose -rf **/*.so **/*.egg-info build **/*.log
	cd sources && make clean

upload: clean
	python setup.py sdist
	@echo UPLOADING VERSION $(MY_VAR)
	twine upload dist/image_intensities-${MY_VAR}.tar.gz

test: clean install
	pip install tox
	tox

install:
	cd image_intensities/image_intensities && make
