THREAD=$1

epoches=0
mismatch=0

mkdir -p mismatches

summary() {
	echo "Total (in batch): $epoches Mismatches: $mismatch"
	printf "Exit?(y/N): "
	read a
	if [ $a = 'y' ]
	then
		exit
	fi
}

trap summary 2 1

while true
do
	make -j $THREAD 2>/dev/null

	for i in `seq 1 64`
	do
		suffix=(.o1.gcc.sha .o2.gcc.sha .o3.gcc.sha .o0.clang.sha
			.o1.clang.sha .o3.clang.sha .os.gcc.sha .os.clang.sha)
		for s in "${suffix[@]}"
		do
			if ! diff $i.o0.gcc.sha $i$s
			then
				echo "SHA256 mismatch!"
				cp $i.c mismatches/$mismatch.c
				mismatch=$(($mismatch + 1))
				break;
			fi
		done
	done

	epoches=$((epoches + 1))

	make clean
done
