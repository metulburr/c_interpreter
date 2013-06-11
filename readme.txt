an attempt at making a c interpreter


EXAMPLE:
MAIN >>> MAIN
MAIN >>> PROC
PROC >>> #include <iostream> 
PROC >>> NAME using namespace std;
NAME >>> FUNC
FUNC >>> void test(){
FUNC >>> cout << "in test()" << endl;
FUNC >>> }
FUNC >>> MAIN
MAIN >>> test();
in test()
MAIN >>> cout << "after test" << endl;
in test()
after test
MAIN >>> for (int i=0; i < 5; i++){cout << i << endl;}
in test()
after test
0
1
2
3
4
MAIN >>> 





#currently
#EXEC to compile and execute
#CLEAR to clear the buffer
