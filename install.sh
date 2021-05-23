#!/usr/bin/env bash

# Print box for loading bar.
# Get the width of the terminal.
cols=$(tput cols)
cols=$(($cols - 3))

# Print upper part uf load bar box.
echo -n '┌'
printf '─%.0s' $(seq 0 $cols)
echo  '┐'

# Print middle part uf load bar box.
echo -n '│'
printf ' %.0s' $(seq 0 $cols)
echo  '│'

# Print bottom part uf load bar box.
echo -n '└'
printf '─%.0s' $(seq 0 $cols)
echo  '┘'

# Move cursor one line up.
echo -ne '\033[2A'

# Draw again the leftside border.
echo -n '│ '

# Start main installation loop to draw progress bar.
echo -en '\033[s' # Save cursor's position to start of load bar.
installed=0

i=0
cols=$(($cols - 1))
size=$(($cols / 3))

while [ $installed != 1 ]; do

    # 1 . Create install directory for files.
    sleep 1
    # If creating file is succesful.
    if sudo mkdir /opt/checker 2> /dev/null ; then
        echo -ne '\033[92m'
        printf '▋%.0s' $(seq 0 $size)
        echo -ne '\033[m'
        echo -en '\033[s' # Store cursor's position progrss in loading bar.
        echo ""
        echo ""
        echo -en "\t🔥 Created installation dir /opt/checker "
    else
        echo -ne '\033[91m'
        printf '▋%.0s' $(seq 0 $size)
        echo -ne '\033[m'
        echo -en '\033[s'
        echo ""
        echo ""
        echo -en "\t🤢 Dir \033[91m/opt/checker\033[m already exists."
    fi    
    sleep 1

    echo -en '\033[u' # Reset cursor to saved position above.

    # 2. Clone repository into installation directory.
    if sudo git -C /opt/checker clone https://github.com/DiegoCol93/CLI_Checker.git 2> /dev/null; then
        echo -ne '\033[92m'
        printf '▋%.0s' $(seq 0 $size)
        echo -ne '\033[m'
        echo -en '\033[s'
        echo ""
        echo ""
        echo ""
        echo -en "\t🔥 Cloned repoository in /opt/checker"
    else
        echo -ne '\033[91m'
        printf '▋%.0s' $(seq 0 $size)
        echo -ne '\033[m'
        echo -en '\033[s'
        echo ""
        echo ""
        echo ""
        echo -en "\t🤮 Couldn't clone repository in \033[91m/opt/checker.\033[m"
    fi    

    echo -en '\033[u' # Reset cursor to saved position above.

    # 3. Create symbolic link to script for running checker command.
    #
    #      This is done to allow you to run the checker command
    #      from anywhere in your machine.
    #
    if sudo ln -s /opt/checker/CLI_Checker/checker /usr/local/bin/checker 2> /dev/null ; then
        echo -ne '\033[92m'
        printf '▋%.0s' $(seq 0 $(($size - 1)))
        echo -ne '\033[m'
        echo ""
        echo ""
        echo ""
        echo ""
        echo -en "\t🔥 Created symlink:\n" \
             "\t\tfrom : /usr/local/bin/checker \033[92m────────────┐\033[m\n" \
             "\t\tto   : /opt/checker/CLI_Checker/checker \033[92m──┘\033[m\n"
    else
        echo -ne '\033[91m'
        printf '▋%.0s' $(seq 0 $(($size - 1)))
        echo -ne '\033[m'
        echo -en '\033[s'
        echo ""
        echo ""
        echo ""
        echo ""
        echo -e "\t🥶 Couldn't create Symbolic \033[91m/usr/local/bin/checker\033[m.\n"
        break
    fi    

    (( installed++ ))
    echo ""
    echo -e "CLI_Checker v0.01 has been installed \033[92msuccesfully\033[m."
    echo -e "You may now run:\n"
    echo -e "\t\033[92mchecker\033[m\n"
    echo -e "to start the checker console."
    
done

if [ $installed != 1 ]; then
    echo "This could be caused because you already have the checker installed."
    echo " If this prevents you from launching the console."
    echo -e "Please run these commands to erase the files and try installing again.\n"
    echo -e "\tsudo rm /opt/checker/ -rf"
    echo -e "\tsudo rm /usr/local/bin/checker"
fi
