# Very interesting that this way works. I guess that
# makes sense. Before, I was basically just importing
# a function so its exit command ended this program.
# Now, I'm making this script run another script.
# This also ends up cleaner bc I don't have to
# separately reroute stdout and stderr.

# Clean up before running again
rm std*.txt

count=0

while [[ 1 ]]; do
    # Increment count
    count=$(($count + 1))
    # Reroute stdout and stderr to files
    ./routine.sh >> stdout2.txt 2>> stderr2.txt
    # If previous script failed, print and exit
    if [[ $? -ne 0 ]]; then
        cat stdout2.txt
        cat stderr2.txt
        echo "The routine took $count runs to fail."
        break
    fi
done