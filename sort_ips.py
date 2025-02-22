import os
import re

def sort_ips(input_file, output_file, format_str):
    """
    处理IP文件：去重、排序并格式化输出。
    
    :param input_file: 输入文件名
    :param output_file: 输出文件名
    :param format_str: 输出格式字符串
    """
    try:
        # 读取IP地址
        with open(input_file, 'r') as file:
            ips = file.readlines()

        # 去除空格和换行符，去重，并排序
        ips = sorted(set(ip.strip() for ip in ips if ip.strip()))

        # 写入新的文件，格式化输出并添加序号
        with open(output_file, 'w') as file:
            for index, ip in enumerate(ips, start=1):
                file.write(format_str.format(ip, index) + "\n")

        print(f"IPs sorted, deduplicated, and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")


if __name__ == "__main__":
    # 定义输入文件和对应的输出文件及格式
    input_files = [
        ("4-LAX.txt", "ipv4.txt", "{}#移动-洛杉矶{}"),
        ("4-HKG.txt", "ipv4.txt", "{}#移动-香港{}"),
        ("6-LAX.txt", "ipv6.txt", "[{}]#移动-洛杉矶{}"),
        ("6-HKG.txt", "ipv6.txt", "[{}]#移动-香港{}")
    ]

    # 遍历文件列表，处理每个文件
    for input_file, output_file, format_str in input_files:
        if os.path.exists(input_file):  # 检查文件是否存在
            sort_ips(input_file, output_file, format_str)
        else:
            print(f"Skipping {input_file}: File does not exist.")
