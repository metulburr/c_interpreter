an attempt at making a c interpreter


example:
```
MAIN >>> std::cout << "test" << std::endl;
c_interpreter.cpp: In function ‘int main()’:
c_interpreter.cpp:5:1: error: ‘cout’ is not a member of ‘std’
 std::cout << "test" << std::endl;
 ^
c_interpreter.cpp:5:24: error: ‘endl’ is not a member of ‘std’
 std::cout << "test" << std::endl;
                        ^
MAIN >>> PROC
PROC >>> #include <iostream>
PROC >>> MAIN
test
MAIN >>> std::cout << "line 2" << std::endl;
test
line 2
MAIN >>> NAME
NAME >>> using namespace std;
NAME >>> MAIN
test
line 2
MAIN >>> cout << "line 3" << endl;
test
line 2
line 3
MAIN >>> EXEC
test
line 2
line 3
MAIN >>> FUNC
FUNC >>> void test(){
FUNC >>> cout << "in test func" << endl;
FUNC >>> }
FUNC >>> EXEC
test
line 2
line 3
FUNC >>> MAIN
test
line 2
line 3
MAIN >>> test();
test
line 2
line 3
in test func
MAIN >>> 
```





#currently
#PROC to enter preprocessor mode
#MAIN to enter main function
#FUNC to enter a new function
#NAME to enter a new namespace
#EXEC to compile and execute
#CLEAR to clear the buffer
