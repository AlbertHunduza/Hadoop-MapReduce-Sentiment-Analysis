rm -r output
rm -r hdfs
mkdir hdfs
hdfs dfs -put twitter.txt hdfs/twitter.txt
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -files mapper.py \
    -mapper "python3 mapper.py" \
    -file reducer.py \
    -reducer "python3 reducer.py" \
    -input hdfs/twitter.txt \
    -output output
cat output/part-00000
