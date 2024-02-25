#include<iostream>
#include<vector>
#include <queue>

using namespace std;

//1801. ��ѹ�����еĶ������� https://leetcode.cn/problems/number-of-orders-in-the-backlog/
//������Ŀ���ɡ�ע��stlϸ�ڡ�
int main()
{
	vector<vector<int>> ords = { {10, 5, 0},{15, 2, 1},{25, 1, 1},{30, 4, 0} };
	vector<vector<int>>* p = &ords;//?

	const int MOD = 1e9 + 7;
	priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> buyOrders;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> sellOrders;

	for (auto&& ords : ords)  //����ÿ�ݶ�������
	{
		int price = ords[0], amt = ords[1], otype = ords[2];
		if (otype == 0)  //buy
		{
			while (amt > 0 && !sellOrders.empty() && sellOrders.top().first <= price)//���Թ���
			{
				auto selltemp = sellOrders.top();
				sellOrders.pop();//Ϊʲô����ȫ������

				int sellamt = min(amt, selltemp.second);
				amt = amt - sellamt;
				selltemp.second -= sellamt;
				if (selltemp.second > 0)
					sellOrders.push(selltemp);
			}
			if (amt > 0)
				buyOrders.emplace(price,amt);//Ϊʲô����ĩ�˲���
		}
		else //sell
		{
			while (amt > 0 && !buyOrders.empty() && buyOrders.top().first >= price)
			{
				auto buytemp = buyOrders.top();
				buyOrders.pop();

				int buyamt = min(buytemp.second, amt);
				amt -= buyamt;
				buytemp.second -= buyamt;
				if (buytemp.second > 0)
					buyOrders.push(buytemp);
			}
			if (amt > 0)
				sellOrders.emplace(price, amt);
		}
	}

	int total = 0;
	//�������� �ǵ�ȡģ
	while (!buyOrders.empty())
	{
		total = (total + buyOrders.top().second) % MOD;
		buyOrders.pop();
	}
	while (!sellOrders.empty())
	{
		total = (total + sellOrders.top().second) % MOD;
		sellOrders.pop();
	}
	return total;
}