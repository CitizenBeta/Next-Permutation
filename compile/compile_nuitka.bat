mkdir nuitka
python -m nuitka --standalone --onefile --msvc=latest --show-memory --show-progress --output-dir=nuitka --remove-output ..\next_permutation.py
pause
