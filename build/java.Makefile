JC := javac
JR := java
FLAGS := -Werror

EXE := Conjecture

# Build java bytecode file.
build : *.java
	$(JC) $(FLAGS) *.java

# Run executable.
run : $(EXE).class
	$(JR) $(EXE)

# Remove bytecode files.
.PHONY : clean
clean :
	rm -f *.class