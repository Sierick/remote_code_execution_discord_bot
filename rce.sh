#!/bin/bash

echo "rce.sh running"

number="1"

while [ $number -eq 1 ]
do
	input=$(cat /home/natesbot/Bots/pythonoutput.txt)
	leninput=${#input}
	if [ "$leninput" -ne "0" ]
	then
		echo "" > /home/natesbot/Bots/pythonoutput.txt
		$input > /home/natesbot/Bots/bashoutput.txt
	else
		sleep 0.1
	fi
done
