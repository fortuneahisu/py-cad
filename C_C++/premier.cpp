// File Name: premier_c.c
// Author: Ahisu Fortune
// Date: 19th of May, 2026
// Description: A dictionary of all my 'C++' knowledge
// Input Status: Required compulsorily

#include <iostream>
#include <string>

int main() {
  std::string nameFirst;
  std::string nameLast;
  int age = 0;
  std::string course;
  int jambScore = 0;
  std::string institution;

  std::cout << "What's your first name? ";
  std::cin >> nameFirst;
  std::cout << "What's your last name? ";
  std::cin >> nameLast;
  std::cout << "Hello " << nameFirst << ' ' << nameLast
            << ", input more about yourself to move on.\n";

  std::cout << "How old are you?: ";
  std::cin >> age;
  std::cout << "Input your course: ";
  std::cin >> course;
  std::cout << "Input your JAMB score: ";
  std::cin >> jambScore;
  std::cout << "What institution would you prefer? ";
  std::cin >> institution;

  std::cout << nameFirst << ", you are " << age << " and are trying to study "
            << course << " with " << jambScore << " JAMB score at "
            << institution << std::endl;
}
