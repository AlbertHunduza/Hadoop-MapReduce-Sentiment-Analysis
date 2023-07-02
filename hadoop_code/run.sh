rm -r out
rm -r hdfs
mkdir hdfs
hdfs dfs -put inpt.txt hdfs/inpt.txt
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -files mapper.py \
    -mapper "python3 mapper.py" \
    -file reducer.py \
    -reducer "python3 reducer.py" \
    -input hdfs/inpt.txt \
    -output out
cat out/part-00000
