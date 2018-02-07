cp -r locinfo ~/.locinfo
echo "\n#alias for locinfo" >> ~/.bash_profile
echo "alias locinfo='python ~/.locinfo/locinfo.py'" >> ~/.bash_profile
. ~/.bash_profile
