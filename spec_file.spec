# spec_file.spec

# Modifica 'tu_aplicacion' y 'icono.ico' según tus nombres de archivos y ubicaciones.
import sys
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(["Main.py"],
             pathex=["/home/neutron/Documentos/Proyectos/Martlab2.0"],
             binaries=[],
             datas=[("window1.py", "."),("window2.py", "."),("window3.py", "."),("window4.py", "."),("window5.py", "."),("window6.py", "."),("Login.py", "."),("recursos_rc.py", "."),("ventanas.py", ".")],
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
          [],
          exclude_binaries=True,
          name="tu_aplicacion",
          icon="/home/neutron/Documentos/Proyectos/Martlab2.0/icono.ico",  # Ruta al icono.ico, opcional
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_debug_dlls=False,
          upx_packer="upx")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               upx_debug_dlls=False,
               upx_packer="upx",
               name="tu_aplicacion")
