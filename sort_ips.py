def sort_ips(input_file, output_file, format_str):
    """
    处理IP文件：去重、排序并格式化输出。
    
    :param input_file: 输入文件名（4.txt 或 6.txt）
    :param output_file: 输出文件名（ipv4.txt 或 ipv6.txt）
    :param format_str: 输出格式字符串
    """
    try:
        # 读取IP地址
        with open(input_file, 'r') as file:
            ips = file.readlines()

        # 去除空格和换行符，去重，并排序
        # 使用set去除重复项，然后通过sorted排序
        ips = sorted(set(ip.strip() for ip in ips if ip.strip()))

        # 写入新的文件，格式为 "ip#移动1" 或 "[ip]#移动1"，并添加序号
        with open(output_file, 'w') as file:
            for index, ip in enumerate(ips, start=1):
                file.write(format_str.format(ip, index) + "\n")

        print(f"IPs sorted, deduplicated, and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")


if __name__ == "__main__":
    # 处理 IPv4 文件
    sort_ips("4.txt", "ipv4.txt", "{}#移动{}")  # IPv4格式：ip#移动1

    # 处理 IPv6 文件
    sort_ips("6.txt", "ipv6.txt", "[{}]#移动{}")  # IPv6格式：[ip]#移动1
