#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, A;
    cin >> N >> A;
    for (int i = 0; i < N; i++)
    {
        char op;
        int B;
        cin >> op >> B;
        if (op == '+')
        {
            A = A + B;
        }
        else if (op == '-')
        {
            A = A - B;
        }
        else if (op == '*')
        {
            A = A * B;
        }
        else if (op == '/')
        {
            if (B == 0)
            {
                cout << "error" << endl;
                exit(0);
            }
            A = A / B;
        }
        cout << i + 1 << ':' << A << endl;
    }
}
