# 屏幕输入主串和子串，求子串在主串中出现的次数
# 1.计算字符串中子串出现的次数。
a = input('请输入字符串')
b = input('请输入子串')

count_ = (lambda a, b:
          a.count(b, 0, -1) + 1
          if a[-1] == b
          else a.count(b, 0, -1))
(a, b)

print('字串出现的次数', count_)
