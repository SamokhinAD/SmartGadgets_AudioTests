import subprocess
import os
import sys

# Имитация IP-ададреса тестового устройства
TEST_DEVICE_IP = "192.168.1.101"

# Имитация директории, где хранятся логи
LOG_DIR = "./test_logs" 

# Проверяет доступность устройства с помощью команды ping.
def check_device_connection(ip):
    print(f"Проверка доступности устройства 1 ({ip})...")
    # Команда ping адаптирована для кросс-платформенности:
    # -c 1 для Linux/macOS, -n 1 для Windows.
    # Отправка 1 пакет
    param = '-n' if os.name == 'nt' else '-c'
    command = ['ping', param, '1', ip]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"[ОК] Устройство {ip} доступно.")
            return True
        else:
            print(f"[ОШИБКА] Устройство {ip} недоступно.")
            print(f"Детали: {result.stdout.splitlines()}")
            return False
    except subprocess.TimeoutExpired:
        print(f"[ОШИБКА] Таймаут при проверке {ip}.")
        return False

def clear_test_logs(directory):
    print(f"Очистка директории логов ({directory})...")
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Новая директория создана.")
        return True

    # Удаление содержимого директории если это файл, а НЕ ПАПКА
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for file in files:
            os.remove(os.path.join(directory, file))
        print(f"[ОК] Удалено логов: {len(files)}.")
        return True
    except Exception as e:
        print(f"[ОШИБКА] Не удалось очистить логи: {e}")
        return False

def setup_environment():
    print("--- Запуск Автоматических Настроек Тестовой Среды ---")
    
    # Проверка подключения
    connectivity_ok = check_device_connection(TEST_DEVICE_IP)
    
    # Очистка логов
    logs_cleared = clear_test_logs(LOG_DIR)
    
    print("\n--- Отчет о Готовности ---")
    if connectivity_ok and logs_cleared:
        print("[ОК] Тестовая среда успешно настроена. Можно запускать тесты.")
        return 0
    else:
        print("[ОШИБКА] Настройка тестовой среды выявила ошибки.")
        return 1

if __name__ == "__main__":
    sys.exit(setup_environment())

# Для запуска: python Auto_Environ_Setup.py