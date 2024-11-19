# NOTHING HAPPENS AFTER THE WHILE LOOP
# I think this is because the `exit 1` in routine
# (see weird.sh) makes this script exit as well.
# Not sure how to fix that.

source spin.sh

# Link file descriptor #6 with stdout to save it
exec 6>&1

# Redirect stdout and stderr to files
exec 1>stdout.txt 2>stderr.txt

# Fencepost: complete routine once
routine
count=1

# Keep calling routine until $? shows exit code 1
while [[ $? -eq 0 ]]; do
    routine
    count=$(($count + 1))
done

# Restore stdout and close file descriptor #6
exec 1>&6 6>&-

cat stdout.txt
cat stderr.txt

echo "The routine took $count runs to fail."
