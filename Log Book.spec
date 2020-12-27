# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py', 'display.py', 'file_manip.py'],
             pathex=['/Users/kylehurd/Documents/PythonCode/Skydive_Log_Book'],
             binaries=[],
             datas=[('assets/info.txt', 'assets'), ('assets/log.csv', 'assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Log Book',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
