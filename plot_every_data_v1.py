import os
import argparse
import matplotlib.pyplot as plt

# 创建解析器对象
parser = argparse.ArgumentParser(description='读取地址参数')

# 添加地址参数
parser.add_argument('address', type=str, help='要读取的地址参数')

# 解析命令行参数
args = parser.parse_args()
address = args.address
count = 0
# 遍历目录及其子文件夹中的所有.txt文件
for root, dirs, files in os.walk(address):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            
            # 解析.txt文件内容
            x = []
            y = []
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    values = line.strip().split('\t')
                    if len(values)==2:
                        x.append(float(values[0]))
                        y.append(float(values[1]))
                    else:
                        print("non_standard_format")
                        break
            count += 1

            # 生成图像并保存为PNG格式，以读入文件名命名
            save_dir = os.path.join(root, 'output')
            os.makedirs(save_dir, exist_ok=True)  # 创建output文件夹
            save_name = os.path.splitext(file)[0] + '.png'
            save_path = os.path.join(save_dir, save_name)
            plt.plot(x, y)
            plt.xlabel('Raman Shift $cm^{-1}$')
            plt.ylabel('Intensity(a.u)')
            plt.xticks([200,400,520,600,720,880,1000])
            plt.title(file)
            plt.savefig(save_path)
            plt.close()
            print(f"deal with file {save_name}")
        #    % print(f"生成图像: {save_name}")
        print(f"finish file number{count}")
        
        