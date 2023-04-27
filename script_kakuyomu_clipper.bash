echo "kakuyomu-clipper shell script start"

target=( 1 2 3 4 5 20 39 40 42 69 70 71 73 74 75 77 79 80 81 83 84 87 90 96 120 121 122 126 128 199 200 203 204 214 259 260 281 284 291)
type='nearest-k'
docsize=5
offset=256
nsize=100

for item in "${target[@]}";
do
  echo "cliping... type=$type target=$item size=$docsize offset=$offset nsize=$nsize"
  python kakuyomu_clipper.py --type=$type --target=$item --size=$docsize --offset=$offset --n=$nsize
done
