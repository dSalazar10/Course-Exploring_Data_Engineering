#!/bin/bash
echo "Enter the Spark Master's Private IP Address:"
read SIP
chmod 400 spark-key.pem
scp -i spark-key.pem sparkify_log_small.json hadoop@$SIP:/home/hadoop/sparkify_log_small.json
scp -i spark-key.pem bootstrap_emr.sh hadoop@$SIP:/home/hadoop/bootstrap_emr.sh
ssh -i spark-key.pem hadoop@$SIP