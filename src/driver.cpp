#include <iostream>
#include <string>
#include <cstdio>
#include <ctime>

/**
 * Application driver
 * TODO:
 * Compile automatically outside of folder 
 */

using namespace std;

int main()
{
    cout << "Starting app... \n";

    clock_t t_start = clock();

    /**
     * Run all ops here + runtime to beginning
     * TODO:
     * 1) Connect to InteractiveBrokers API
     * 2) Run trading test suite
     * 3) Analytics, etc. 
     */

    auto output = "Runtime: " + to_string((clock() - t_start)/(double)CLOCKS_PER_SEC) + "\n";
    cout << output;
}