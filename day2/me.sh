#!/usr/bin/bash

cat ./input_test.txt | sed 's/ /+/' \
	|sed 's/\(A+Y\|B+Z\|C+X\)/6+\1/' \
	|sed 's/\(A+Z\|B+X\|C+Y\)/0+\1/' \
	|sed 's/\(A+X\|B+Y\|C+Z\)/3+\1/' \
	|tr 'ABCXYZ' '000123' | bc | paste -sd+ | bc

cat ./input.txt | sed 's/ /+/' \
	|sed 's/\(A+Y\|B+Z\|C+X\)/6+\1/' \
	|sed 's/\(A+Z\|B+X\|C+Y\)/0+\1/' \
	|sed 's/\(A+X\|B+Y\|C+Z\)/3+\1/' \
	|tr 'ABCXYZ' '000123' | bc | paste -sd+ | bc

cat ./input_test.txt | sed 's/ /+/' \
	|sed 's/\(.*X\)/0+\1/' \
	|sed 's/\(.*Y\)/3+\1/' \
	|sed 's/\(.*Z\)/6+\1/' \
	|sed 's/\(A+Y\|C+Z\|B+X\)/1/' \
	|sed 's/\(A+Z\|C+X\|B+Y\)/2/' \
	|sed 's/\(A+X\|C+Y\|B+Z\)/3/' \
	| bc | paste -sd+ | bc

cat ./input.txt | sed 's/ /+/' \
	|sed 's/\(.*X\)/0+\1/' \
	|sed 's/\(.*Y\)/3+\1/' \
	|sed 's/\(.*Z\)/6+\1/' \
	|sed 's/\(A+Y\|C+Z\|B+X\)/1/' \
	|sed 's/\(A+Z\|C+X\|B+Y\)/2/' \
	|sed 's/\(A+X\|C+Y\|B+Z\)/3/' \
	| bc | paste -sd+ | bc


