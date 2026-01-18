import os
import shutil

# Конфиг: какие расширения в какие папки класть
# Можно дополнять своими прямо в списке
MAPPING = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Applications': ['.exe', '.msi', '.dmg', '.apk'],
    'Media': ['.mp4', '.mp3', '.mov', '.mkv', '.wav'],
}

def main():
    # Берем путь, где лежит сам скрипт
    base_path = os.path.dirname(os.path.realpath(__file__))
    script_name = os.path.basename(__file__)

    print(f"--- Начинаю разбор файлов в: {base_path} ---")

    count = 0
    for filename in os.listdir(base_path):
        # Пропускаем сам скрипт и папки
        if filename == script_name or os.path.isdir(os.path.join(base_path, filename)):
            continue

        # Узнаем расширение
        ext = os.path.splitext(filename)[1].lower()
        
        target_folder = None
        for folder, extensions in MAPPING.items():
            if ext in extensions:
                target_folder = folder
                break
        
        # Если расширение нам неизвестно, кладем в 'Other'
        if not target_folder:
            target_folder = 'Other'

        # Создаем папку, если её нет
        target_path = os.path.join(base_path, target_folder)
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # Перемещаем файл
        try:
            # Если файл с таким именем уже есть, добавим (1), (2) и т.д.
            source = os.path.join(base_path, filename)
            destination = os.path.join(target_path, filename)
            
            if os.path.exists(destination):
                name, extension = os.path.splitext(filename)
                destination = os.path.join(target_path, f"{name}_new{extension}")

            shutil.move(source, destination)
            print(f"[OK] {filename} -> {target_folder}")
            count += 1
        except Exception as e:
            print(f"[ERROR] Не удалось переместить {filename}: {e}")

    print(f"\n--- Готово! Обработано файлов: {count} ---")

if __name__ == "__main__":
    main()