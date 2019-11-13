////////////////////////////////////////////////////////////////////////////
//
//    Tufts University, Comp 160 wordInterpret coding assignment  
//
//    main.cpp
//    word interpret
//
//    simple main to test wordInterpret
//    NOTE: this main is only for you to test wordInterpret. We will compile
//          your code against a different main in our autograder directory
//
////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include "interpret.h"

using namespace std;


int main(void) {
    string inputNums = "1234";
    if (wordInterpret(inputNums) != 3) {
        cout << "Noo!\n";
    } else {
        cout << "Yay!\n";
    }
    return 0;
}
