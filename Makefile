
default:

clean:
	rm -rf build/ dist/ *.egg-info

wheel:
	python setup.py bdist_wheel

upload:
	python setup.py sdist upload --sign

