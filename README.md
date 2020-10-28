# DSLR raspberry

## Device communication

Update you're system

```bash
sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y
```

Install packages

``` bash
sudo apt install -y build-essential git make autoconf libltdl-dev\
    libusb-dev libexif-dev libpopt-dev libxml2-dev libjpeg-dev \
    libgd-dev gettext autopoint libgphoto2-6 gphoto2
```

Test devices connection

``` bash
gphoto2 --auto-detect
```
received

``` bash
------------------------------------------
Canon EOS 5D Mark II           usb:001,006 
```
