file="Makefile"

if [ -e "$file" ]; then
  cp ~/ft_destructor/fix_leaks.py .
  python3 fix_leaks.py
  rm -rf fix_leaks.py
  cp -r ~/ft_destructor/ft_destructor .
  cd ft_destructor
  make
  cd ..
else
  echo "Makefile not found"
fi