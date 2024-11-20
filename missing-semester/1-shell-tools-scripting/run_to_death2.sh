rm std*.txt

# Keep count
count=0

while [[ 1 ]]; do
    count=$(($count + 1))
    ./routine.sh >> stdout2.txt 2>> stderr2.txt
    if [[ $? -ne 0 ]]; then
        cat stdout2.txt
        cat stderr2.txt
        echo "The routine took $count runs to fail."
        break
    fi
done