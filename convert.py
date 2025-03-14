import nbformat
from nbconvert import MarkdownExporter
import os

def convert_notebook_to_markdown(notebook_path):
    # 读取 Notebook 文件
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # 创建 Markdown 导出器
    exporter = MarkdownExporter()

    # 导出为 Markdown 格式
    markdown, resources = exporter.from_notebook_node(notebook)

    # 生成 Markdown 文件的路径
    base_name = os.path.splitext(notebook_path)[0]
    markdown_path = f"{base_name}.md"

    # 将 Markdown 内容写入文件
    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return markdown_path

# 获取当前文件夹路径
current_folder = os.getcwd()

# 遍历当前文件夹中的所有文件和文件夹
for filename in os.listdir(current_folder):
    if filename.endswith('.ipynb'):
        convert_notebook_to_markdown(filename)