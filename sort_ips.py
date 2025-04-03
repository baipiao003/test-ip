import os
from collections import defaultdict

# 名称映射表：将文件名中的标识符映射为对应的地点名称
NAME_MAPPING = {
    "LAX": "洛杉矶",
    "SJC": "圣何塞",
    "SEA": "西雅图",
    "DFW": "达拉斯",
    "FRA": "法兰克福",
    "NRT": "日本",
    "SIN": "新加坡",
    "TPE": "台北",
    "HKG": "香港"
}

def get_location_name(filename):
    """
    根据文件名中的标识符获取对应的输出名称。
    例如：文件名包含"LAX"时返回"洛杉矶"，包含"HKG"时返回"香港"。
    """
    for key, name in NAME_MAPPING.items():
        if key in filename:
            return name
    return "未知"

def sort_ips(input_files, output_file, format_str):
    """
    处理多个IP文件：读取、分组、分别排序并格式化输出。
    
    :param input_files: 输入文件列表
    :param output_file: 输出文件名
    :param format_str: 输出格式字符串
    """
    try:
        # 使用字典分组存储IP地址，键为地点名称
        ip_groups = defaultdict(list)

        # 读取所有输入文件的内容，并按来源地分组
        for input_file in input_files:
            if os.path.exists(input_file):
                with open(input_file, 'r') as file:
                    ips = file.readlines()
                location_name = get_location_name(input_file)  # 获取当前文件的地点名称
                ip_groups[location_name].extend([ip.strip() for ip in ips if ip.strip()])
            else:
                print(f"Skipping {input_file}: File does not exist.")

        # 对每个分组内的IP地址去重并排序
        for location in ip_groups:
            ip_groups[location] = sorted(set(ip_groups[location]))

        # 写入新的文件，按分组顺序输出并添加序号
        with open(output_file, 'w') as file:
            for location in sorted(ip_groups.keys()):  # 按地点名称排序
                index = 1  # 每个分组的序号从1开始
                for ip in ip_groups[location]:
                    file.write(format_str.format(ip, location, index) + "\n")
                    index += 1

        print(f"IPs sorted, deduplicated, and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error processing files: {e}")


if __name__ == "__main__":
    # 定义输入文件和对应的输出文件及格式
    ipv4_files = ["4-HKG.txt", "4-NRT.txt", "4-TPE.txt", "4-SIN.txt", "4-FRA.txt", "4-DFW.txt", "4-SJC.txt", "4-SEA.txt", "4-LAX.txt"]  # IPv4文件列表
    ipv6_files = ["6-HKG.txt", "6-FRA.txt", "6-LAX.txt"]  # IPv6文件列表

    # 处理 IPv4 文件，输出到 ipv4.txt
    sort_ips(ipv4_files, "ipv4.txt", "{}#移动-{}{}")
    # 处理 IPv6 文件，输出到 ipv6.txt
    sort_ips(ipv6_files, "ipv6.txt", "[{}]#移动-{}{}")
