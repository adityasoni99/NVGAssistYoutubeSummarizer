# youtube_summarizer_plugin.spec

# SPDX-FileCopyrightText: Copyright (c) 2025 YOUR_ORG. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# PyInstaller Spec File for G-Assist Plugin

block_cipher = None

a = Analysis(
    ['plugin.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='youtube_summarizer_plugin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False  # Set to True if you want to see console logs
)
