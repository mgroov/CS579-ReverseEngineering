all: shellcode.S
	as shellcode.S -o shellcode.o
	ld shellcode.o -o shellcode --oformat=binary
	rm shellcode.o

test: shellcode_tester.c
	gcc shellcode_tester.c -o shelltest -z execstack -no-pie
	gdb ./shelltest

clean:
	rm shellcode
	rm shelltest
