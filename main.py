from tqdm import tqdm
import os
import shutil
import config


def sync_folders(source_folder, target_folder, exclude_extensions=[]):
    # 確保目標資料夾存在，若不存在則建立
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍歷源資料夾中的所有檔案和子資料夾
    for root, dirs, files in os.walk(source_folder):
        # 在目標資料夾中建立相同的子資料夾結構
        relative_path = os.path.relpath(root, source_folder)
        target_dir = os.path.join(target_folder, relative_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # 複製源資料夾中的檔案到目標資料夾
        for file in tqdm(files, desc=f'Copying files in {relative_path}', unit='file'):
            if not any(file.endswith(ext) for ext in exclude_extensions):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)
                # 檢查目標資料夾中是否已經存在相同的檔案，如果不存在則複製
                if not os.path.exists(target_file):
                    shutil.copy2(source_file, target_file)


if __name__ == "__main__":
    sync_folders(config.SOURCE_FOLDER,
                 config.TARGET_FOLDER,
                 config.EXCLUDE_EXTENSIONS)
