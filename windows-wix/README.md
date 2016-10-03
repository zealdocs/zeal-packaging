## Instructions for building an .msi file

Placeholders for actual paths:
* `%ZEAL_PKG_DIR%`

1. Download the [WiX Toolset](http://wixtoolset.org/) (v3.9 R2 was used when developing
   the .wxs file for Zeal)
2. Compile Zeal.
3. Use `windeployqt` to get all runtime dependencies in one place:
```
windeployqt --dir %ZEAL_PKG_DIR%
```
4. In `%ZEAL_PKG_DIR%` remove all files (Qt plugins) not listed in `zeal.wxs`.
5. Copy `bin/zeal.exe` to the deployment directory.
6. Copy `ssleay32.dll` and `libeay32.dll` to the deployment directory.
7. Set the environment variables:
  * ZEAL_VERSION (for example "0.1.0")
  * ZEAL_PKG_DIR
8. Run `candle.exe zeal.wxs`.
9. Run `light.exe -ext WixUIExtension zeal.wixobj`.
