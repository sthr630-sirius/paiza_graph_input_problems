/*
degree euler graph
*/
#include<iostream>
using namespace std;
int main(){
  int n, m, v;
  int ans;
  int a, b;
  ans = 0;
  cin >> n >> m >> v;
  for (int i=0; i<m; i++){
    cin >> a >> b;
    if (v == a or v == b) ans++;
  }

  cout << ans << endl;

  return 0;
      
}
