#include<iostream>

using namespace std;

int main()
{
	string s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles";
	int pre = 0;//比对的数字大小
	int i = 0;
	while (i < s.size())
	{
		if (int(s[i])>=48 && int(s[i])<=57)
		{
			int temp = 0;
			while (i < s.size() && isdigit(s[i])) {
				temp = temp * 10 + s[i] - '0';
				i++;
			}
			if (temp <= pre)
				return false;
			pre = temp;
		}
		else {
			i++;
		}
	}
	return true;
}