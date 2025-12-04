import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

def calculate_rms(data):
    """Расчет среднеквадратичной амплитуды (RMS)."""
    return np.sqrt(np.mean(data**2))

def analyze_audio(file_path:str):
    """Загрузка, анализ и визуализация аудиофайла wav."""
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return

    try:
        sample_rate, data = wavfile.read(file_path)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Такой if-модуль позволяет взять только один канал, если файл стерео,
    # т.к. часто каналы дают похожие данные. В тестах для удобства исследуем
    # только один канал, но вообще можно анализировать оба в отдельности.
    if data.ndim > 1:
        data = data[:, 0]

    # Конвертируем в float для точности в расчетах (так как wav-ки сохраняют в int)
    if data.dtype != np.float32 and data.dtype != np.float64:
        data = data.astype(np.float32) / np.iinfo(data.dtype).max # Также нормализация (от -1 до 1)

    duration = len(data) / sample_rate
    rms = calculate_rms(data)

    print("--- Анализ аудиофайла ---")
    print(f"Файл: {os.path.basename(file_path)}")
    print(f"Частота дискретизации (Гц): {sample_rate}")
    print(f"Продолжительность (с): {duration:.2f}")
    print(f"RMS (Среднеквадратичная амплитуда): {rms:.4f}")
    
    # Визуализация
    time = np.linspace(0., duration, len(data))
    plt.figure(figsize=(12, 4))
    plt.plot(time, data)
    plt.title(f'Временной график: {os.path.basename(file_path)}')
    plt.xlabel("Время (секунды)")
    plt.ylabel("Амплитуда")
    plt.grid(True)
    plt.savefig(f"audio_plot.png")
    plt.show()

if __name__ == "__main__":
    path_name = str(input("Введите путь к аудиофайлу: "))
    analyze_audio(path_name)

# Для запуска: python Acoustic_Data_Analyzer.py
