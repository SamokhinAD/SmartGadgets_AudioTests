#!/bin/bash
arecord -d 5 -f cd test.wav
if [ -f "test.wav" ]; then
    echo "Файл записан, микрофон работает."
else
    echo "Ошибка записи!"
fi