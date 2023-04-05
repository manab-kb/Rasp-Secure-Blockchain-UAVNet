echo off
set hostnam=%1
set pass=password
set usrnam=username
putty.exe -ssh %usrnam%@%hostnam%.scss.tcd.ie -pw %pass%
