#include <iostream>

using namespace std;

class TaroJiroDividing {
    public:
        int getNumber(int A, int B) {
            int numbers = 0;
            if(B>A) {
                int temp = A;
                A = B;
                B = temp;
            }
            if(A%B==0) {
                int temp = B;
                while(temp%2==0) {
                    ++numbers;
                    temp /= 2;
                }
                ++numbers;
                if(A%2==1 && B%2==1 && A!=B) {
                    --numbers;
                }
            }
            return numbers;
        }
};

int main(){
    TaroJiroDividing t;
    cout << t.getNumber(8,4) << endl;
    cout << t.getNumber(4,7) << endl;
    cout << t.getNumber(12,12) << endl;
    cout << t.getNumber(24,96) << endl;
    cout << t.getNumber(1000000000,999999999) << endl;
    cout << t.getNumber(27,9) << endl;
    cout << t.getNumber(1,1) << endl;
    return 0;
}
