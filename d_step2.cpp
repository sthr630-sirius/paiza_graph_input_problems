/*
degree euler graph
*/
#include<iostream>
#include<vector>
using namespace std;
int main(){
  int n, m;
  cin >> n >> m;
  int a, b;
  vector<vector <int> > g(n);
  for (int i=0; i<m; i++){
    cin >> a >> b;
    g.at(a-1).push_back(b);
    g.at(b-1).push_back(a);
  }
  
  for (int i=0; i<n; i++){
    cout << g.at(i).size();
    if (i<n-1) cout << " ";
    else cout << endl;
  }

  return 0;
}


