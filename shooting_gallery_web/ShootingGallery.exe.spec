# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\name\\Desktop\\WebShooting\\app\\entry_points\\test_core_bootstrap.py'],
    pathex=['C:\\Users\\name\\Desktop\\WebShooting\\app\\entry_points'],
    binaries=[],
    datas=[('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\PIL', 'PIL'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\numpy', 'numpy'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\cv2', 'cv2'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\httpx', 'httpx'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\idna', 'idna'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\pygrabber', 'pygrabber'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\httpcore', 'httpcore'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\certifi', 'certifi'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\h11', 'h11'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\patoolib', 'patoolib'), ('C:\\Users\\name\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'ipaddress'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\screeninfo', 'screeninfo'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\fastapi', 'fastapi'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\uvicorn', 'uvicorn'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\starlette', 'starlette'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\annotated_doc', 'annotated_doc'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\anyio', 'anyio'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\pydantic', 'pydantic'), ('C:\\Users\\name\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\http', 'http'), ('C:\\Users\\name\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\logging', 'logging'), ('C:\\Users\\name\\Desktop\\WebShooting\\.venv\\Lib\\site-packages\\click', 'click')],
    hiddenimports=['pydantic.dataclasses', 'typing_extensions', 'uuid', 'colorsys', 'ipaddress--distpath=dist'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ShootingGallery.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
