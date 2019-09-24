rm -f data*
gfortran plane-wave.f -o plane-wave
chmod +x plane-wave
./plane-wave
./plane-wave-anim.sh
