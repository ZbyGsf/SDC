import numpy as np
import matplotlib.pyplot as plt

# def plot_three_color_heatmap(matrix):
#     # 处理矩阵
#     processed_matrix = np.where(matrix < 1, 0, np.where(matrix > 1, 2, matrix))
#     # 定义颜色映射
#     cmap = plt.cm.colors.ListedColormap(['red', 'green', 'black'])
#     # 设置图形大小
#     plt.figure(figsize=(10, 6))
#     # 绘制热力图
#     plt.imshow(processed_matrix, cmap=cmap, aspect='auto')
#     # 显示颜色条
#     plt.colorbar(ticks=[0, 1, 2], label='Value')
#     # 显示图表
#     plt.show()

# # 示例用法
# matrix = np.random.uniform(0, 2, size=(24, 400)) # 用随机矩阵作为示例
# plot_three_color_heatmap(matrix)