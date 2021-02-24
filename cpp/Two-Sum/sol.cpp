/*
 * @Author: Yutong Xie
 * @Date: 2021-02-23 19:30:45
 * @LastEditTime: 2021-02-23 19:32:32
 * @Description: In User Settings Edit
 * @FileContent: Using hashmap to solve the two sum problem. 
 */

#include<iostream>
#include <vector>
#include <map>
using namespace std; 

class Solution{
    public:
    vector<int> twoSum(vector<int> &nums, int target){
        map<int, int> myMap;
        for (int i = 0; i < nums.size(); i++){
            int tmp = target - nums[i];
            if (myMap.find(tmp) != myMap.end()){
                vector<int> ans {myMap[tmp], i};
                return ans;
            }

            myMap[nums[i]] = i;
        } 
        throw invalid_argument("There is no solution.");
    }
};

void print_vec(const vector<int> & vec){
    for (int v: vec){
        cout << v << " "; 
    }
    cout << endl;

}
int main(){

    vector<int> vec {1,5,2,7,4};
    int target = 50;
    print_vec(Solution().twoSum(vec, target));
    
    return 0;
}

