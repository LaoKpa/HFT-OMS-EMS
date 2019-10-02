// A simple program that computes the square root of a number
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

class ArrayList
{
private:
	int size;
	int max_size;
	int *arr;

	bool resize();

public:
	int get(int i);
	int pop();
	int push(int a);
	ArrayList(int in_size)
	{
		if (in_size == -1)
		{
			size = 10;
		}
		else
		{
			size = in_size;
		}
		arr = new int[size];
	}
};

int ArrayList::get(int i)
{
	if (i < 0 || i >= size)
	{
		return -1;
	}
	return arr[i];
};

int ArrayList::pop()
{
	if (size == 0)
	{
		return -1;
	}
	size = size - 1;
	return arr[size];
};

int ArrayList::push(int a) {
	if(size==max_size) {
		if(!resize()) {
			return -1;
		}
	}
};

bool ArrayList::resize() {
		

}

main(int argc, char *argv[])
{
	if (argc < 2)
	{
		fprintf(stdout, "Usage: %s number\n", argv[0]);
		return 1;
	}
	double inputValue = atof(argv[1]);
	double outputValue = sqrt(inputValue);
	fprintf(stdout, "The square root of %g is %g\n",
			inputValue, outputValue);
	return 0;
}