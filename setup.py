from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], include_files=["src/"], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('src/main.py', base=base, targetName = 'Calculator')
]

setup(name='Calculator',
      version = '1.0',
      description = 'Simple Calculator',
      options = dict(build_exe = buildOptions),
      executables = executables)
