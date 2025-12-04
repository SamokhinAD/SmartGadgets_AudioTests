#!/bin/bash
find ./recordings -type f -name "*.wav" -mtime +7 -delete
echo "Старые записи удалены"