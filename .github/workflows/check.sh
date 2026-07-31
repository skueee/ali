export errors=0

if ! [ -d "$HOME/.ali/bin" ]; then
    echo "ERROR: $HOME/.ali/bin does not exist after configuring"
    ((errors++))
fi

if ! [ -d "/opt/ali/bin" ]; then
    echo "ERROR: /opt/ali/bin does not exist after configuring"
    ((errors++))
fi

ali create testcommand "cat /etc/hostname"

if ! [ $(testcommand) == $HOSTNAME ]; then
    echo "ERROR: testcommand output is not correct"
    ((errors++))
fi

ali manage testcommand remove

if [ $(testcommand) == $HOSTNAME ]; then
    echo "ERROR: testcommand is not deleted correctly"
    ((errors++))
fi

sudo ali create supertestcommand "cat /etc/hostname" -g

if ! [ $(supertestcommand) == $HOSTNAME ]; then
    echo "ERROR: supertestcommand output is not correct"
    ((errors++))
fi

if [ $errors == 0 ]; then
    exit 0
else
    exit 1
