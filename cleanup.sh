#!/bin/sh

TARGET_DIR="./db"

if [ -d "$TARGET_DIR" ]; then
    echo "🧹 Cleaning up: removing $TARGET_DIR ..."
    rm -rf "$TARGET_DIR"
    echo "✔️ $TARGET_DIR deleted."
else
    echo "ℹ️ No $TARGET_DIR directory found. Nothing to remove."
fi
