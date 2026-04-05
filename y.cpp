#include<iostream>
#include<vector>

int main()
{
    std::vector<int> arr = {1,2,3,4,5,6,7,8,9};
    for(int i = 0; i < arr.size(); i++)
    {
        std::cout << arr[i] << std::endl;
    }
    return 0;
}