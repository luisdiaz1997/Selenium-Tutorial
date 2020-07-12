# Selenium-Tutorial
Simple tutorial for automated testing


## Clone this repository

'''bash
git clone https://github.com/luisdiaz1997/Selenium-Tutorial
'''

## Download Miniconda on your system

https://docs.conda.io/en/latest/miniconda.html

### For Linux

'''bash
bash <(wget -qO- https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
'''

### For Mac

'''bash
bash <(wget -qO- https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh)
'''

### install

'''bash
conda env create -f selenium.yml
'''

##Download Gecko webdriver (For Firefox)

'''bash
sudo apt install firefox-geckodriver
'''

Or download from this [website](https://github.com/mozilla/geckodriver/releases)

and move it to:

'''bash
/usr/local/bin
'''

you might need sudo to do this
