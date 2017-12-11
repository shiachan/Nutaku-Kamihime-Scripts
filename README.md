# Nutaku-Kamihime-Scripts
This is a small collection of scripts to automate the more painful parts of the game.

This is work in progress.

# Requirements #

-------------


Python 3+ and Requests(http://docs.python-requests.org/en/master/)

A way for you to look at post request while game is running (Example: chrome inspector)

# Files #

================


## Runable scripts ##

----------------


normal_gacha.py - This lets you gacha without the pain of selling off stuff when your inventory is full

sell_fodders_in_inventory_and_timed_present_box.py - this sells off N Weapon and Eidolon, R/SR Enhance Weapon and Eidolon

make_sr_slvl_4.py Takes 1 SLVL 1 SR non enhance fodder weapon and Enhances it to SLVL 4 with using 6 R non enhance fodder weapons

check_weapon_fodder.py - shows you how much non enhance SR/R you have


## Support scripts ##

---------------


conf.py - put the xsrf id and cookie here else script wont start.

heading.py - headers used to get response from game

heading_post headers used to post response to game

sell_fodder_no_loop - sells your fodder during normal_gacha.py's operation.

# Usage #

==============

1. Open Chrome Inspector and go to the network tab
2. Do something that will do a post request such as (Running 1 Gem gacha roll (10/1 roll or free is fine))
3. In the case that you doa Gem gacha roll, filter for "normal", look at headers tab> Request Headers
4. look for the values of "cookie:" and "x-xsrf-token:" and then fill the two fields in conf.py
5. Run check_weapon_fodder.py to check if it is ok, if it doesn't throw an error it should be fine.
