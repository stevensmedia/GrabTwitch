all: setup.py
	python setup.py py2app

setup.py: GrabTwitch.py
	py2applet --make-setup GrabTwitch.py

clean:
	rm -f setup.py
	rm -rf dist
	rm -rf build