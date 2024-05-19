from PIL import Image
import os

# 设置目标文件夹路径
folder_path = 'C:\\Users\\13001\Desktop\hotmap'
# 设置目标尺寸
target_height = 256
target_width = 128

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为PNG格式图片
    if filename.endswith('.png'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)

        # 使用Pillow打开图片
        with Image.open(file_path) as img:
            # 调整图片尺寸
            resized_img = img.resize((target_width, target_height))

            # 保存调整尺寸后的图片覆盖原图片
            # 注意：如果您想保留原图，请将resized_img存储在另一个目录或使用不同的文件名
            resized_img.save(file_path)
            print(f'Resized {filename}')

print("All PNG images have been resized.")