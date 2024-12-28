import pandas as pd
import os

# 读取Excel数据
file_path = 'C:/Users/liu-i/Desktop/商品表/pdf/黑河特产/New Microsoft Excel Worksheet.xlsx'
output_html = 'C:/Users/liu-i/Desktop/商品表/pdf/黑河特产/output.html'
image_folder = 'C:/Users/liu-i/Desktop/商品表/pdf/黑河特产/png/'  # 存放图片的文件夹

# 读取Excel文件
data = pd.read_excel(file_path)

# 生成HTML
html_content = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商品展示</title>
    <style>
        table { width: 80%; margin: auto; border-collapse: collapse; text-align: center; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        img { width: 100px; height: auto; cursor: pointer; transition: 0.3s; }
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.8); }
        .modal img { margin: auto; display: block; width: 50%; }
        .close { position: absolute; top: 20px; right: 30px; color: white; font-size: 30px; cursor: pointer; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">商品展示表</h2>
    <table>
        <tr>
            <th>图片</th>
            <th>商品条码</th>
            <th>商品名称</th>
            <th>单位</th>
            <th>售价</th>
        </tr>
"""

# 添加表格数据
for _, row in data.iterrows():
    image_path = os.path.join(image_folder, row['图片'])
    html_content += f"""
        <tr>
            <td><img src="{image_path}" alt="{row['商品名称']}" onclick="openModal(this.src)"></td>
            <td>{row['商品条码']}</td>
            <td>{row['商品名称']}</td>
            <td>{row['单位']}</td>
            <td>{row['售价']:.2f}</td>
        </tr>
    """

# 添加HTML结束部分
html_content += """
    </table>
    <div class="modal" id="myModal" onclick="closeModal()">
        <span class="close" onclick="closeModal()">&times;</span>
        <img id="modalImg" src="" alt="放大图片">
    </div>
    <script>
        function openModal(src) {
            document.getElementById('myModal').style.display = 'block';
            document.getElementById('modalImg').src = src;
        }
        function closeModal() {
            document.getElementById('myModal').style.display = 'none';
        }
    </script>
</body>
</html>
"""

# 将内容写入HTML文件
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML文件已生成：{output_html}")
