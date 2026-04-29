/**
 * File Name: premier_c.c
 * Author: Ahisu Fortune
 * Date: 28th of May, 2025
 * Description: A dictionary of all my 'C' knowledge
 * Input Status: Required compulsorily
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nameFirst[40];
    char nameLast[40];
    int age = 0;
    char course[40];
    int jambScore = 0;
    float jambPercent = jambScore/400;

    printf("Enter your full name: ");
    scanf(" %s%s", nameFirst, nameLast);
    printf("Hello %s, Input more about yourself to move on.\n", nameLast);
    printf("How old are you?: ");
    scanf(" %d", &age);
    printf("Input your course: ");
    scanf(" %s", course);
    printf("Input your JAMB score: ");
    scanf(" %d", &jambScore);
    jambPercent = jambScore/400;
    printf("%s, you are %d and are trying to study %s with %d JAMB score percentage", nameLast, age, course, jambPercent);
}
