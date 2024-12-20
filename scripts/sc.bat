@echo off
setlocal enabledelayedexpansion

set "destination=apple"
for /d %%D in (*) do (
    if /i not "%%~nxD"=="%destination%" (
        echo Processing folder: %%~nxD
        for %%F in ("%%D\*") do (
            set "filename=%%~nxF"
            set "newname=%%~nxD_!filename!"
            echo Renaming "%%F" to "!newname!"
            ren "%%F" "!newname!"
            echo Moving "%%D\!newname!" to "%destination%\"
            move "%%D\!newname!" "%destination%\"
        )
    )
)

echo Operation completed.
pause