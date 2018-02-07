#! /bin/sh

set -e

help_message ()
{
    echo "This shell will use apt-get install"
    echo "python3 pip3 beatifulsoup4 xlrd xlwt HTMLParser"
}

if [ "$1" == "-h" ]; then
    help_message
    exit 0
fi

echo start to create crawler configtions

sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install beautifulsoup4
sudo pip3 install xlrd
sudo pip3 install xlwt
sudo pip3 install HTMLParser
sudo pip3 install requests

echo finsih to create crawler configtions

exit 0
