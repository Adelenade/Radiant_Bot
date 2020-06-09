ask() {
    local prompt reply default
    prompt="y/n"
    default="y"
    while true; do
        echo -n "$1 [$prompt] "
        read reply </dev/tty
        if [ -z "$reply" ]; then
            reply=$default
        fi
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
            *) echo "Please type [Y]es or [N]o"
        esac
    done
}

progress_bar()
{
    local PROG_BAR_MAX=${1:-30}
    local PROG_BAR_DELAY=${2:-1}
    local PROG_BAR_TODO=${3:-"."}
    local PROG_BAR_DONE=${4:-"|"}
    local i

    echo -en "["
    for i in `seq 1 $PROG_BAR_MAX`
    do
        echo -en "$PROG_BAR_TODO"
    done
    echo -en "]\0015["
    for i in `seq 1 $PROG_BAR_MAX`
    do
        echo -en "$PROG_BAR_DONE"
        sleep ${PROG_BAR_DELAY}
    done
    echo
}

if !ask "You are going to run the Radiant Bot please make sure you set your token before in /src/main.py"
then
    echo -e "\nOh too bad :( Please please come back soon :D !"
    exit
fi

progress_bar 10
echo -e "\nLet's gooooooooooooooooooo\n"

python3 /src/main.py
