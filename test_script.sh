start=$(date +%s)
for i in {1..10}
do
	curl -s -X POST "https://us-central1-assignments-252803.cloudfunctions.net/function-1" -F 'img1=@/home/jsmayank/Pictures/Screenshot from 2019-06-20 11-02-53.png' > output
done
end=$(date +%s)
echo $start
echo $end
