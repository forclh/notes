import os
import shutil
import tempfile
import time


class TempDirectory:
    def __enter__(self):
        self.path = tempfile.mkdtemp()
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.path)
        return False


# 使用
with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    with open(os.path.join(tmp_dir, "test.txt"), "w") as f:
        f.write("hello")
        time.sleep(1)
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
