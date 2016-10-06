#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int N;
    cin >> N; cin.ignore();
    int C;
    cin >> C; cin.ignore();
    vector<int> budget;
    int sum = 0;
    for (int i = 0; i < N; i++) {
        int B;
        cin >> B; cin.ignore();
        sum+=B;
        budget.push_back(B);
    }
    if(sum<C) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        sort(budget.begin(), budget.end());
        for(int i=0; i<budget.size()-1; i++) {
            int promedio = C / (budget.size()-i);
            if(budget[i] < promedio) {
                cout << budget[i] << endl;
                C-=budget[i];
            } else {
                cout << promedio << endl;
                C-=promedio;
            }
        }
        cout << C << endl;
    }
}