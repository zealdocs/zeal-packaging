## Instructions for building MSI installer.

Placeholders (or environment variables) for actual values:

* `%ZEAL_PKG_DIR%` - a path to the directory where all files should be placed before packing.
* `%ZEAL_VERSION%` - the application version which is being packed.

Requirements:

* [WiX Toolset](http://wixtoolset.org/)

Steps:

1. Compile Zeal.
2. Use `windeployqt` to get all runtime dependencies in one place:

  ```shell
  > windeployqt --dir %ZEAL_PKG_DIR%
  ```

3. In `%ZEAL_PKG_DIR%` remove all files (Qt plugins) not listed in `zeal.wxs`.
4. Copy `bin/zeal.exe` to the deployment directory.
5. Copy `ssleay32.dll` and `libeay32.dll` to the deployment directory.
6. Run the following commands:

  ```shell
  > candle.exe -dZealVersion=%ZEAL_VERSION% -dZealPackageDir=%ZEAL_PKG_DIR% zeal.wxs
  > light.exe -ext WixUIExtension zeal.wixobj
  ```
