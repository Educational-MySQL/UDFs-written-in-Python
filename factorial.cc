#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    if(argc != 2) {
        printf("Argument count is wrong");
        return EXIT_FAILURE;
    }
    
    std::string command("python factorial.py");
    
    command += " ";
    command += argv[1];
    
    FILE * in = popen(command.c_str(), "r");
    char buf[100];
    fread(buf, 100, 1, in);
    pclose(in);
    
    std::cout << buf << std::endl;

    return 0;
}
