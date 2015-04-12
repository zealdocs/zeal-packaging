## Instructions for building an .msi file

1. Download the [WiX Toolset](http://wixtoolset.org/) (v3.9 R2 was used when developing
   the .wxs file for Zeal)
2. Compile Zeal.
3. Set the environment variables:
  * ZEAL_VERSION (for example "0.1.0")
  * ZEAL_BIN_DIR (for example "..\..\build-zeal-Desktop_Qt_5_4_1_MinGW_32bit-Release\bin")
  * QTDIR (for example "C:\Qt\5.4\mingw491_32")
  * QTTOOLSDIR (for example "C:\Qt\Tools\mingw491_32")
4. Run `candle.exe zeal.wxs`
5. Run `light.exe -ext WixUIExtension zeal.wixobj`
