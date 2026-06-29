import os
import shutil

def organize_folder():
    print("=== FILE ORGANIZER CLI ===")
    
    target_dir = input("Enter the full path of the folder to organize: ").strip()
    
    if not target_dir or not os.path.exists(target_dir):
        print("\n❌ Error: Invalid directory path.\n")
        return

    extensions_map = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Video': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
    }

    print(f"\n📂 Scanning: {target_dir}")
    print("-" * 40)

    try:
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            
            if os.path.isdir(file_path):
                continue
                
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder_name, extensions in extensions_map.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(target_dir, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"📦 Moved: {filename} -> {folder_name}/")
                    moved = True
                    break
            
            if not moved and file_ext:
                other_folder = os.path.join(target_dir, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"📦 Moved: {filename} -> Others/")

        print("-" * 40)
        print("✅ Directory structural sorting complete.\n")
        
    except Exception as e:
        print(f"\n❌ Operational Fault: {e}\n")

if __name__ == '__main__':
    organize_folder()