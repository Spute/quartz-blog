import os
import re
from datetime import datetime

# -------- 修改这里：测试单文件路径（可选） --------
# 例如：TEST_FILE = r"/path/to/file.md"
TEST_FILE = "content\无广告、零上传：纯本地运行的在线图片转换网站.md"               # None 表示不启用单文件模式
TEST_FILE = None               # None 表示不启用单文件模式
# --------------------------------------------------

# -------- 修改这里：目标文件夹路径（目录模式下） --------
TARGET_DIR = r"content"
# --------------------------------------------------

SKIP_FILENAME = "文章写作模版"  # 不带 .md 后缀的名字


def get_file_created_time(path):
    stat = os.stat(path)
    created_ts = stat.st_ctime
    return datetime.fromtimestamp(created_ts).strftime("%Y-%m-%d")

def process_md_file(path):
    filename = os.path.splitext(os.path.basename(path))[0]

    # 跳过指定文件
    if filename == SKIP_FILENAME:
        print(f"[跳过指定文件] {path}")
        return

    created_time = get_file_created_time(path)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 匹配 frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)

    # ---------------------------
    # ① 无 frontmatter → 创建
    # ---------------------------
    if not fm_match:
        new_frontmatter = f"---\ndate: {created_time}\n---\n"
        new_content = new_frontmatter + content
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[创建 frontmatter + 添加 date] {path}")
        return

    # ---------------------------
    # ② 有 frontmatter → 检查是否存在 date
    # ---------------------------
    frontmatter = fm_match.group(1)
    body = content[fm_match.end():]

    # 已经存在日期 → 不修改
    if re.search(r"^date\s*:", frontmatter, re.MULTILINE):
        print(f"[保留已有 date] {path}")
        return

    # 不存在 → 添加 date 字段
    new_frontmatter = f"date: {created_time}\n" + frontmatter
    new_content = f"---\n{new_frontmatter}\n---\n{body}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[添加 date 字段] {path}")


def process_directory():
    for root, _, files in os.walk(TARGET_DIR):
        for name in files:
            if name.lower().endswith(".md"):
                process_md_file(os.path.join(root, name))


def main():
    if TEST_FILE:
        if os.path.exists(TEST_FILE) and TEST_FILE.lower().endswith(".md"):
            print(f"[单文件模式] 正在处理：{TEST_FILE}")
            process_md_file(TEST_FILE)
        else:
            print(f"[错误] TEST_FILE 不存在或不是 .md 文件：{TEST_FILE}")
    else:
        print("[目录模式] 开始处理整个目录...\n")
        process_directory()


if __name__ == "__main__":
    main()
