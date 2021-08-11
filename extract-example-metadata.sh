#!/bin/bash

echo "# Python SDK for vRNI - Examples" > EXAMPLES.md

EXAMPLE_FILES="examples/*.py"
for example in $EXAMPLE_FILES
do
    echo "Processing $example file..."
    # see if example header is present
    LINE=`grep "Example:" $example`
    if [ -n "$LINE" ]
    then
        EXAMPLE_NAME=`echo $LINE | sed -e 's/^# Example:\ *//'`
        echo "## ${example}" >> EXAMPLES.md
        echo "### ${EXAMPLE_NAME}" >> EXAMPLES.md

        # sed -n '1!p' = cut first line ("START Description")
        # sed '$d' = cut last line ("END Description")
        # sed 's/^..//' = remove the comments "# "
        EXAMPLE_DESC=`sed -n '/START Description/,/END Description/p' $example | sed -n '1!p' | sed '$d' | sed 's/^..//'`
        echo $EXAMPLE_DESC >> EXAMPLES.md
    fi
done