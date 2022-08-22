# Buildozer Requierement (UBUNTU)

A list of programs needed by buildozer to work on ubuntu and compile your app

```
sudo apt install zip
sudo apt install unzip
sudo apt install libtool
sudo apt install autoconf
sudo apt install python3
sudo apt install python3-pip
pip install kivy
pip install buildozer
pip install javac
pip install cython==0.29.19
sudo apt install git
sudo apt install default-jre
sudo apt install default-jdk
sudo apt install python3-setuptools
sudo apt-get install build-essential
sudo apt install libsqlite3-dev
sudo apt install sqlite3
sudo apt install bzip2
sudo apt install libbz2-dev
sudo apt install zlib1g-dev
sudo apt install libssl-dev
sudo apt install openssl
sudo apt install libgdbm-dev
sudo apt install libgdbm-compat-dev
sudo apt install liblzma-dev
sudo apt install libreadline-dev
sudo apt install libncursesw5-dev
sudo apt install libffi-dev
sudo apt install uuid-dev
sudo apt-get install -y libffi7
sudo apt-get install libffi-dev
```

Then (change path by the find result) :
```
find /usr/lib -name "libffi.so*"
sudo ln -s /usr/lib/x86_64-linux-gnu/libffi.so.7 /usr/lib/x86_64-linux-gnu/libffi.so.6
```
and cython
```
echo "cython3 \$@" | sudo tee -a /bin/cython
sudo chmod 755 /bin/cython
```
and sdkmanager

Go here : https://developer.android.com/studio#downloads

Select linux command line sdk download file, accept the terms, and copy the link of download button (replace bellow)
```
cd ~ && url="https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip" && filename=$(basename "$url") && wget $url && unzip $filename && export PATH=~/cmdline-tools:~/cmdline-tools/bin:$PATH
```
