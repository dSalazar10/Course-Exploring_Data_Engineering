echo "Enter the Bastion Host's Public IP Address:"
read BIP
PROJ=$PWD
cd ~/Downloads/
chmod 400 bastion-key.pem
echo $'Copying the Jenkins Key and Login Script...\n'
scp -i bastion-key.pem spark-key.pem ubuntu@$BIP:/home/ubuntu/spark-key.pem
scp -i bastion-key.pem $PROJ/spark-login.sh ubuntu@$BIP:/home/ubuntu/spark-login.sh
scp -i bastion-key.pem $PROJ/bootstrap-emr.sh ubuntu@$BIP:/home/ubuntu/bootstrap-emr.sh
scp -i bastion-key.pem $PROJ/sparkify_log_small.json ubuntu@$BIP:/home/ubuntu/sparkify_log_small.json
echo $'Logging Into Secure Shell...\n'
ssh -i bastion-key.pem ubuntu@$BIP
#rm bastion-key.pem