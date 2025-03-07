#!/bin/bash
echo "Resetting persistent queue project..."
sudo pkill -f supervisord
rm -rf logs/ data/
mkdir -p data/files logs && chmod 777 data/files logs
echo "Cleanup done!"