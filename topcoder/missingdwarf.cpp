#include <vector>

using namespace std;

class MissingDwarf {
public:
  int getHeight(vector <int> otherHeights) {
    int h = otherHeights[0];
    int sum = h;
    for(int i=1; i<otherHeights.size(); i++) {
      if (otherHeights[i] > h) {
	h = otherHeights[i];
      }
      sum += otherHeights[i];
    }
    int missing = h + 1;
    sum += missing;
    int diff = 0;
    if (sum % 7 != 0) {
      diff = 7 - (sum % 7);
    }
    
    return missing + diff;
  }
};
