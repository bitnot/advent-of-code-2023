.PHONY: all, day01_test, day02_test

all: day01_test day02_test

day01_test:
	@echo 'Day 1 Part 1, sample'
	python3 ./day01/part01.py < day01/01_sample.txt

	@echo 'Day 1 Part 1, input'
	python3 ./day01/part01.py < day01/input.txt

	@echo 'Day 1 Part 2, sample'
	python3 ./day01/part02.py < day01/02_sample.txt

	@echo 'Day 1 Part 2, input'
	python3 ./day01/part02.py < day01/input.txt

day02_test:
	@echo 'Day 2 Part 1, sample'
	python3 ./day02/part01.py < day02/01_sample.txt

	@echo 'Day 2 Part 1, input'
	python3 ./day02/part01.py < day02/input.txt

	@echo 'Day 2 Part 2, sample'
	python3 ./day02/part02.py < day02/01_sample.txt

	@echo 'Day 2 Part 2, input'
	python3 ./day02/part02.py < day02/input.txt

day03_test:
	@echo 'Day 3 Part 1, sample'
	python3 ./day03/part01.py < day03/01_sample.txt

	@echo 'Day 3 Part 1, input'
	python3 ./day03/part01.py < day03/input.txt

	@echo 'Day 3 Part 2, sample'
	python3 ./day03/part02.py < day03/01_sample.txt

	@echo 'Day 3 Part 2, input'
	python3 ./day03/part02.py < day03/input.txt

day04_test:
	@echo 'Day 4 Part 1, sample'
	python3 ./day04/part01.py < day04/01_sample.txt

	@echo 'Day 4 Part 1, input'
	python3 ./day04/part01.py < day04/input.txt
