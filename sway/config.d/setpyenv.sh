#!/bin/bash

# This script sets Python environment variable representing in which environment is active
# Accepts 1 parameter

case "$1" in
    "g")
        echo "global.env" > ~/.config/.currpyenv
        ;;
    "t")
        echo "nlptrans.env" > ~/.config/.currpyenv
        ;;
    "n")
        echo "gnn.env" > ~/.config/.currpyenv
        ;;
    "c")
        echo "compvis.env" > ~/.config/.currpyenv
        ;;
    "l")
        echo "llmcoder.env" > ~/.config/.currpyenv
        ;;
    "m")
        echo "multilspy.env" > ~/.config/.currpyenv
        ;;
    *)
        echo "" > ~/.config/.currpyenv
        ;;
esac
