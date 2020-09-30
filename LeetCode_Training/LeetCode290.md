给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct={}
        s_split=s.split()
        if len(s_split)!=len(pattern):
            return False
        for i,item in enumerate(pattern):
            if item not in dct:
                if s_split[i] in dct.values():
                    return False
                dct[item]=s_split[i]
            else:
                if dct[item]!=s_split[i]:
                    return False
            #print(item+' '+dct[item]+' '+s_split[i]+'\n')
        return True
```

```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] s_split=s.split(" ");
        HashMap<String,String> map=new HashMap<String,String>();
        if(s_split.length!=pattern.length()) return false;
        for(int n=0;n<pattern.length();n++){
            String c=pattern.substring(n,n+1);
            //System.out.println(c+" "+s_split[n]);
            if(!map.containsKey(c)){
                if(map.containsValue(s_split[n]))
                {
                    return false;
                }
                else 
                    map.put(c,s_split[n]);
            }
            else{
                if(!map.get(c).equals(s_split[n]))
                {
                    //System.out.println(n+" "+map.get(c)+" "+s_split[n]);
                    return false;
                }
            }
        }
        return true;
    }
}
```

