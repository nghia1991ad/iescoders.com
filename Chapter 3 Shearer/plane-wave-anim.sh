#!/usr/bin/bash
gnuplot << eof
set term gif animate
set output "animate.gif"
n=9    #n frames
set xrange [0:102]
set yrange [-2:2]
i=0
list = system('ls data*')
do for [file in list] {
	plot file w lines lt 1 lw 1.5 t sprintf("t=%i sec",i/10)
	i = i + 1
}
set output
eof
