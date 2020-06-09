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

if ask "You are going to run the Radiant Bot please make sure you set your token before in /src/main.py"
then
    echo -e "\nLet's gooooooooooooooooooo\n"
fi

for i in {001..100}; do
    sleep 1
    printf "\r $i %"
done

python3 src/main.py