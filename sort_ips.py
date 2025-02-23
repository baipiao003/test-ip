import os
import re

# 名称映射表
NAME_MAPPING = {
    "LAX": "洛杉矶",
    "HKG": "香港"
}

def get_location_name(filename):
    """
    根据文件名中的标识符获取对应的输出名称。
    """
    for key, name in NAME_MAPPING.items():
        if key in filename:
            return name
    return "未知"

def sort_ips(input_files, output_file, format_str):
    """
    处理多个IP文件：读取、合并、去重、排序并格式化输出。
    
    :param input_files: 输入文件列表
    :param output_file: 输出文件名
    :param format_str: 输出格式字符串
    """
    try:
        # 读取所有输入文件的内容，并记录每个IP的来源文件
        all_ips = []
        for input_file in input_files:
            if os.path.exists(input_file):
                with open(input_file, 'r') as file:
                    ips = file.readlines()
                location_name = get_location_name(input_file)  # 获取当前文件的地点名称
                all_ips.extend([(ip.strip(), location_name) for ip in ips if ip.strip()])
            else:
                print(f"Skipping {input_file}: File does not exist.")

        # 去除重复的IP地址（基于IP本身去重），并排序
        all_ips = sorted(set(all_ips))

        # 写入新的文件，格式化输出并添加序号
        with open(output_file, 'w') as file:
            for index, (ip, location_name) in enumerate(all_ips, start=1):
                file.write(format_str.format(ip, location_name, index) + "\n")

        print(f"IPs sorted, deduplicated, and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    # 定义输入文件和对应的输出文件及格式
    ipv4_files = ["4-HKG.txt", "4-LAX.txt"]
    ipv6_files = ["6-HKG.txt", "6-LAX.txt"]

    # 处理 IPv4 文件
    sort_ips(ipv4_files, "ipv4.txt", "{}#移动-{}{}")
    # 处理 IPv6 文件
    sort_ips(ipv6_files, "ipv6.txt", "[{}]#移动-{}{}")
