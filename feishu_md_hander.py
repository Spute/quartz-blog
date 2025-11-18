import os
import re

def replace_md_image_links(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 ![](...)，其中...包含static/，提取文件名
    pattern = r'!\[\]\([^\)]*static/([^\)\s]+)\)'
    matches = list(re.finditer(pattern, content))
    if not matches:
        return False

    new_content = content
    for match in matches:
        old = match.group(0)
        filename = match.group(1)
        new = f'![[{filename}]]'
        print(f'修改: {old} >>> {new}\n')
        new_content = new_content.replace(old, new)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def replace_md_first_line_as_title(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        return False
    first_line = lines[0]
    if first_line.lstrip().startswith('#'):
        # 提取标题内容
        title = first_line.lstrip('#').strip()
        new_lines = [f"---\ntitle: {title}\n---\n"] + lines[1:]
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"第一行以#开头，已替换为YAML头：title: {title}")
        return True
    return False

def fix_title_colon(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if len(lines) >= 3 and lines[0].strip() == '---' and lines[2].strip() == '---':
        # 检查第二行是否为 title: ...
        if lines[1].startswith('title: '):
            title = lines[1][7:].strip()
            if '：' in title or ':' in title:
                # 替换所有中英文冒号为 --
                new_title = title.replace('：', '--').replace(':', '--')
                lines[1] = f'title: {new_title}\n'
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print(f"已将title中的冒号替换为--: {title} -> {new_title}")
                return True
    return False

def process_all_md_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                print(f"处理文件: {md_path}")
                replace_md_image_links(md_path)
                replace_md_first_line_as_title(md_path)
                fix_title_colon(md_path)

if __name__ == "__main__":
    # md_path = r"D:\coding\quartz\content\产品体验记\Wan2.2-Animate_ 统一的角色动画和视频人物替换模型.md"
    # fix_title_colon(md_path)
    # replace_md_image_links(md_path)
    # replace_md_first_line_as_title(md_path)
    output_directory = r"D:\coding\quartz\content"
    process_all_md_files(output_directory)