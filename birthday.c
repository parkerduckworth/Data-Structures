#include <stdio.h>

typedef struct {
	char * name;
	int age;
} person;

void birthday(person * p){
	p->age++;
}

int main() {
	person parker;
	parker.name = "Parker";
	parker.age = 27;

	printf("%s is %d years old.\n", parker.name, parker.age);
	birthday(&parker);
	printf("Happy birthday! %s is now %d years old.\n", parker.name, parker.age);

	return 0;
}