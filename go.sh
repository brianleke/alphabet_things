#!/bin/bash

usage(){
	echo "Illegal number of parameters. Must parse one parameter as follows:"
	echo -e "Usage: $0 [Argument]"
}

[ "$#" != "1" ] && ( usage && exit 1 )

python main.py "$1"

