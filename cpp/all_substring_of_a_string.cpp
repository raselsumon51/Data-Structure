#include<bits/stdc++.h>
using namespace std;

void subString(char str[], int n)
{
	for (int i = 0; i <n; i++)
	{
		for (int j = 0; j < n - i; j++)
		{
			for (int k = j; k <= j+i; k++)
				cout << str[k];
			cout << endl;
		}
	}
}

int main()
{
	char str[] = "abcd";
	subString(str, strlen(str));
	return 0;
}
