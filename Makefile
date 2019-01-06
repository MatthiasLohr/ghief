
default:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build/ dist/ *.egg-info

upload:
	twine upload dist/*

bootstrap:
	virtualenv -p $$(which python3) venv
