#!/bin/bash

function quit {
	exit
}
function checkHostAlive {
	echo $1
	ping -q -c 1 $1
	rc=$?
	if [[ $rc -eq 0 ]]; then
		echo 'SUCK IT!'
	else
		echo 'No Connection'
	fi
}
checkHostAlive oakland.edu
echo "done"
quit

