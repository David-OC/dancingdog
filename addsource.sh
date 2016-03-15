FLAG=1

if ! type python2 2>&1 > /dev/null ; then
    echo "Python 2 is not installed, exiting.."
    exit 1
fi

if [ -n "$BASH_VERSION" ]; then
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
	echo "source $SCRIPT_DIR/command_not_found_bash" >> $HOME/.bashrc
	echo "Added source to .bashrc"
	FLAG=0
fi

if [ -n "$ZSH_VERSION" ]; then
    CURRENT_DIR=${(%):-%x}
    SCRIPT_DIR="$( cd "$( dirname "${CURRENT_DIR}" )" && pwd )"
	echo "source $SCRIPT_DIR/command_not_found_zsh" >> $HOME/.zshrc
	echo "Added source to .zshrc"
	FLAG=0
fi
[ $FLAG -ne 0 ] && echo "Could not find either bash nor zsh, exiting.." && exit 1
