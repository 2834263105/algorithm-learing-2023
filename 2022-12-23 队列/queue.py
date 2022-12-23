class solution:
    def queue(self, s: str, k: int) -> str: #s是字符串，k代表字符串的前k个字母
        if k == 1:      #每次只能取字符串的首字母移动到末尾
            answer = s
            for _ in range(len(s) - 1):  #经过0次到n-1次的移动从而得到n个不同的字符串
                s = s[1:] + s[0]
                answer = min(answer, s)  #找到n个字符串中字典序最小的字符串
            return answer                #返回该字符串
        return ''.join(sorted(s))        #将返回的字符串按升序排列好

