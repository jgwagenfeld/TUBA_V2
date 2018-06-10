#!/usr/bin/env bash


echo $(pwd)
for d in ${0%/*/}
do
     (cd "$d" && Allclean)
done


exit 0
