.PHONY: clean-pyc clean-build build-cpp compile
.DEFAULT: all

DEBUG=True
HOST=localhost
APP_NAME=HFTApp

clean-py:
	@echo "\n\nStarting clean-py."
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	@echo "Python artifacts cleaned."

clean-cpp:
	@echo "\n\nStarting clean-cpp."
	rm --force --recursive build/
	find . -name '*.pdb' -exec rm --force {} +
	find . -name '*.obj' -exec rm --force {} +
	find . -name '*.exe' -exec rm --force {} +
	@echo "C++ artifacts cleaned."

build-cpp:
	@echo "\n\nStarting build-cpp."
	mkdir build/
	cd build/ && cmake .. -G "Unix Makefiles"
	@echo "C++ project built."

build-py: 
	@echo "\n\nStarting build-py."
	pip install -r requirements.txt
	@echo "Python project built."

compile: 
	@echo "\n\nStarting compile."
	cd ./build/ && make
	@echo "Project compiled."

run:
	@echo "\n\nRunning application."
	python -u -m HFTApp --debug=$(DEBUG) --host=$(HOST)
	./build/$(APP_NAME)
	@echo "Application exit. \n\n\n"

dockerify:
	docker build -t amirjankar/hft --build-arg BUILD_TS=$(shell date --iso=seconds) .