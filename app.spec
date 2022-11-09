block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=["./env/lib/python3.10/site-packages"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)

a.datas += Tree('./public', prefix ='./public')

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Boilerplate App',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    windowed=True,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon = "public/Anime-Girl-Face-Meme-PNG-Image.webp"
)


app = BUNDLE(exe,
    name='myscript.app',
    icon='public/Anime-Girl-Face-Meme-PNG-Image.webp',
    bundle_identifier=None)
