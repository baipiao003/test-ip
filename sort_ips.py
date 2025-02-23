import os
import re

def sort_ips(input_files, output_file, format_str):
    """
    处理多个IP文件：读取、合并、去重、排序并格式化输出。
    
    :param input_files: 输入文件列表
    :param output_file: 输出文件名
    :param format_str: 输出格式字符串
    """
    try:
        # 读取所有输入文件的内容
        all_ips = []
        for input_file in input_files:
            if os.path.exists(input_file):
                with open(input_file, 'r') as file:
                    ips = file.readlines()
                all_ips.extend(ips)
            else:
                print(f"Skipping {input_file}: File does not exist.")

        # 去除空格和换行符，去重，并排序
        all_ips = sorted(set(ip.strip() for ip in all_ips if ip.strip()))

        # 写入新的文件，格式化输出并添加序号
        with open(output_file, 'w') as file:
            for index, ip in enumerate(all_ips, start=1):
                file.write(format_str.format(ip, index) + "\n")

        print(f"IPs sorted, deduplicated, and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    # 定义输入文件和对应的输出文件及格式
    ipv4_files = ["4-HKG.txt", "4-LAX.txt"]
    ipv6_files = ["6-HKG.txt", "6-LAX.txt"]

    # 处理 IPv4 文件
    sort_ips(ipv4_files, "ipv4.txt", "{}#移动-{}")
    # 处理 IPv6 文件
    sort_ips(ipv6_files, "ipv6.txt", "[{}]#移动-{}")
