""" 实现文件内容的对齐并写入新文件
【实现思路】
    1. 根据字符串的特点，使用re模块匹配到三个需要对齐的子字符串
    2. 对三个子字符串进行对齐操作
    3. 将三个对齐后的子字符串拼接起来
    4. 将拼接后的字符串追加写入新的文件
"""
import re

# 为了匹配到三个子字符串，设置三个pattern
pattern1 = r"name:.*;"
pattern2 = r";score:"
pattern3 = r";score:(.*)"

# 读取源文件
with open('source_file.txt', 'r') as f1:
    for line in f1.readlines():
        line = line.replace(" ", "")
        # 如果是空行，跳过
        if line.strip() != "":
            # 第一个子串：通过字符串截取的方式获得
            sub_str1_end = re.match(pattern1, line).span()[1] - 1
            sub_str1 = line[:sub_str1_end].ljust(20)
            # 第二个子串：固定的字符串
            sub_str2 = pattern2
            # 第三个子串：使用匹配的group()方法获得
            sub_str3 = re.search(pattern3, line).group(1).rjust(7)
            
            sub_str = sub_str1 + sub_str2 + sub_str3

            with open('new_file.txt', 'a') as f2:
                f2.writelines(f"{sub_str}\n")