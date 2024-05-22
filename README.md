# cydbg
## How to Use
1. Install [pdm](https://pdm-project.org/en/stable/#installation) if it is not installed;
2. In this directory, run `pdm sync`;
3. Run `pdm compile`, if need DEBUG mode, type `y` and enter; or directly enter;
4. After compilation, run `pdm main`
## Notes
- This little project currently supports windows and linux only;
- Python version must be at leat above 3.10;
- If you're using windows, VS version must be at lease 2019 16.9, and C++ AddressSanitizer should be installed;
- If you're using linux, run `export LD_PRELOAD=/usr/lib/gcc/x86_64-linux-gnu/{your gcc version}/libasan.so` before running `pdm main`;
- Windows is now unabled to be run with ASan, if you need run it with DEBUG mode, please delete `/fsanitizer=address` in `setup.py`, line 45;
- If you're using VSCode, you can use [Python C++ Debugger](https://marketplace.visualstudio.com/items?itemName=benjamin-simmonds.pythoncpp-debug) to try it.
