// File Name: premier_c.c
// Author: Ahisu Fortune
// Date: 19th of May, 2026
// Description: A dictionary of all my 'C++' knowledge
// Input Status: Required compulsorily

#include <iostream>
#include <string>
int main()
{
    std::string nameFirst;
    std::string nameLast;
    int age = 0;
    std::string course;
    int jambScore = 0;
    std::string institution;
    std::cin >> "What's your name? " >> nameFirst;
    std::cout << "Hello nameLast, Input more about yourself to move on.\n"
              << std::endl;
    std::cin >> "How old are you?: " >> age;

    std::cin >> "Input your course: " >> course;
    std::cin >> "Input your JAMB score: " >> jambScore;
    std::cin >> "What institution would you prefer? " >> institution;
    std::cout << nameFirst << ", you are " << age << "and are trying to study " << course << " with " << jambScore << " JAMB score at " << " institution" << std::endl;
}
