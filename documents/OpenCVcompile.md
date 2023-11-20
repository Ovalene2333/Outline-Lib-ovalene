# Compile the opencv in Ubuntu

## Say before compile

As it widely known that many software only gives us the sourse code so that we need to compile it than get the exacutable files(like exe,or binary file with out the file extension)

## Compile

### Prepare

#### Uninstall the old version

`<this chapter is from https://developer.ridgerun.com/wiki/index.php/Compiling_OpenCV_from_Source>`

```
shell
sudo apt purge libopencv-dev libopencv-python libopencv-samples libopencv*
```

#### Install the requirments

```
shell
sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev python3-pip python3-numpy
```

#### build and compile

```
zsh
# now you are in the dir you download your sourse code
cd opencv-4.6.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
# add some arguments and back
make -j8
# compile,may take minutes,you can launch the Genshin impact when your computer compiling the code.
sudo make install 
# install
```
