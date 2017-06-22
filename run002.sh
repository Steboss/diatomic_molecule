#!/bin/bash

echo "Submitting absolute calculations"

cd  absolute
for f in */ ; do
    cd  $f
    cd run002/cyclohexane/
    cd output
    sbatch ../cyclo.sh
    cd ../
    cd ../water
    cd output
    sbatch ../water.sh
    cd ../
    cd ../vacuum
    cd output
    sbatch ../vacuum.sh
    cd ../
    cd ../
    cd ../../
done

cd ../

echo "Submitting relative calculations"

cd relative
for f in */ ; do
    cd $f
    cd run002/cyclohexane/
    cd output
    sbatch ../cyclo.sh
    cd ../
    cd ../water
    cd output
    sbatch ../water.sh
    cd ../
    cd ../vacuum
    cd output
    sbatch ../vacuum.sh
    cd ../
    cd ../
    cd ../../
done

cd ../
echo "Done"
