#### [剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

难度简单67收藏分享切换为英文接收动态反馈

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

**示例 1:**

```
输入: [1,2,3,4,5]
输出: True
```

 

**示例 2:**

```
输入: [0,0,1,2,5]
输出: True
```

 

**限制：**

数组长度为 5 

数组的数取值为 [0, 13] .

### 题解

自己的思路：将大小王0视作容错率，遍历有序数组，容错不足时返回false

题解优选：跳过大小王，判断max-min>=5？

```java
class Solution {
    public boolean isStraight(int[] nums) {
        int counter_0=0;
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0)
                counter_0++;
            else if(i>=1 && nums[i-1]!=0){
                counter_0-=nums[i]-nums[i-1]-1;
                if(counter_0<0 || nums[i]==nums[i-1])
                    return false;
            }
            //System.out.println("counter:"+counter_0+" nums[i]:"+nums[i]);
        }
        return true;
    }
}
```

