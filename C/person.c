#include <stdio.h>

typedef struct {
	char * name;
	int age;
} person;

int main() {
	person john;

	john.name = "Parker";
	john.age = 27;
	printf("%s is %d years old.\n", john.name, john.age);
}