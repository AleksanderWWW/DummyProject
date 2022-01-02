.PHONY: run clean

setup: requirements.txt
	pip install -r requirements.txt

run:
	python app.py --number 0
	python app.py --number 4
	python app.py --number -5
	python app.py --number 10

clean:
	rm -rf __pycache__
