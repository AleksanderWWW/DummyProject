.PHONY: run clean

setup: requirements.txt
	pip install -r requirements.txt

run_single:
	python app.py --number 0
	python app.py --number 4
	python app.py --number -5
	python app.py --number 10

run_multiple:
	python app.py numbers.json 4 6 10 11 45 10000

clean:
	rm -rf __pycache__
