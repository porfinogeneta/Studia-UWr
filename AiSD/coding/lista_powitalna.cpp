// WJA
#include <iostream>
#include <vector>
int main() {
  
  int a, b;
  std::cin >> a >> b;
  std::vector<int> nums;
  for (int i = a; i <= b; ++i){
    if (i % 2024 == 0){
      nums.push_back(i);
    }
  }
  if (!nums.empty()){
    for (int n : nums){
      std::cout << n << " ";
    }
  }
  std::cout << std::endl;
  return 0;
}