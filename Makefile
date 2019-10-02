.PHONY: clean-pyc clean-build build-cpp compile
.DEFAULT: all

DEBUG=True
HOST=localhost
APP_NAME=HFTApp

clean-py:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean-cpp:
	rm --force --recursive build/

build-cpp:
	cmake . -G "Unix Makefiles" -B ./build/

build-py: 
	pip install -r requirements.txt
	pip install .

compile:
	cd ./build/
	make

run:
	python -u -m $(HFTApp) --debug=$(DEBUG) --host=$(HOST)
	./build/$(APP_NAME)