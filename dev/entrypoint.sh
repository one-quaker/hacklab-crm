#!/bin/bash

while [ "true" ]; do
    if [[ $DEBUG == "1" ]]; then
        echo "Developer mode"
    else
        echo "Production mode"
        if [[ $MODE == "bot" ]]; then
            $ENV_PYTHON_BIN bot.py
        elif [[ $MODE == "web" ]]; then
            make collectstatic && make migrate && make run
        fi
    fi
    /bin/sleep 10
done
