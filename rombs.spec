# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['rombs.py'],
             pathex=['C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('mm_grid.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\mm_grid.png',"DATA")]
a.datas += [('rombs_0.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_0.png',"DATA")]
a.datas += [('rombs_1.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_1.png',"DATA")]
a.datas += [('rombs_2.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_2.png',"DATA")]
a.datas += [('rombs_3.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_3.png',"DATA")]
a.datas += [('rombs_4.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_4.png',"DATA")]
a.datas += [('rombs_5.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_5.png',"DATA")]
a.datas += [('rombs_6.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\rombs_6.png',"DATA")]
a.datas += [('micro.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\micro.png',"DATA")]
a.datas += [('ruler2.png','C:\\Users\\berdnikov\\YandexDisk\\Yura\\assistant\\labs\\PycharmProjects\\untitled\\ruler2.png',"DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='rombs',
          debug=False,
          strip=False,
          upx=True,
          console=False )
