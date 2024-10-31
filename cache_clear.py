import os
import shutil

def clear_pycache():
    current_dir = os.getcwd()
    print(f"Clearing __pycache__ folders in {current_dir} and its subdirectories...")
    count = 0

    for root, dirs, files in os.walk(current_dir):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Cleared __pycache__ folder in {pycache_path}")
            count += 1

    print(f"\nCleared {count} __pycache__ folders.")

clear_pycache()
