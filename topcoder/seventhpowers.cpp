#include <string>

using namespace std;

class SeventhPowers {
public:
  int base [9] = { 1, 128, 2187, 16384, 78125, 279936, 823543, 2097152, 4782969};
  string reconstructA(int B) {
    string s = "";
    while (B > 0) {
      for(int i=8; i>=0; i--) {
	if(base[i] <= B) {
	  B -= base[i];
	  s = s + to_string(i+1);
	  break;
	}
      }
    }
    return s;
  }
};
