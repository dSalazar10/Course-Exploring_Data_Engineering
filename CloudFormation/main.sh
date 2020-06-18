#!/bin/bash
function PromptUser {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| Main Menu |"
    echo "~~~~~~~~~~~~~"
    echo "Stack: ${stackname}"
    echo ""
    echo "Select from the following options:"
    echo "1) Create Stack"
    echo "2) Update Stack"
    echo "3) Delete Stack"
    echo "4) Describe Stacks"
    echo "5) Validate Template"
    echo "6) Setup Stack"
    echo "7) Exit"
    echo "~:"
}
function CreateStack {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| CreateStk |"
    echo "~~~~~~~~~~~~~"
    echo ""
    aws cloudformation create-stack --stack-name $stackname --template-body file://$tempfile --parameters file://$paramfile --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region us-west-2
    echo "Stack Creation Completed."
    sleep 1
}
function UpdateStack {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| UpdateStk |"
    echo "~~~~~~~~~~~~~"
    echo ""
    aws cloudformation update-stack --stack-name $stackname --template-body file://$tempfile --parameters file://$paramfile --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region us-west-2
    echo "Stack Update Completed."
    sleep 1
}
function DeleteStack {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| DeleteStk |"
    echo "~~~~~~~~~~~~~"
    echo ""
    aws cloudformation delete-stack --stack-name $stackname
    echo "Stack Delete Completed."
    sleep 1
}
function ValidateTemplate {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| ValTempl  |"
    echo "~~~~~~~~~~~~~"
    echo ""
    aws cloudformation validate-template --template-body file://$tempfile
    sleep 1
}
function DescribeStack {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| DescStack |"
    echo "~~~~~~~~~~~~~"
    echo ""
    aws cloudformation describe-stacks --stack-name $stackname
    sleep 1
}
function SetupStack {
    printf "\033c"
    echo "~~~~~~~~~~~~~"
    echo "| SetupStack |"
    echo "~~~~~~~~~~~~~"
    echo ""
    echo "Select from the following options:"
    echo "1) Network Stack"
    echo "2) Bastion Stack"
    echo "3) Postgres Stack"
    echo "4) Cassandra Stack"
    echo "5) Redshift Stack"
    echo "6) Spark Stack"
    echo "~:"
    read choice
    case $choice in
        1)
            stackname="NetworkStack"
            tempfile="network.yml"
            paramfile="network-parameters.json"
            ;;
        2)
            stackname="BastionStack"
            tempfile="bastion.yml"
            paramfile="bastion-parameters.json"
            ;;
        3)
            stackname="PostgresStack"
            tempfile="postgres.yml"
            paramfile="postgres-parameters.json"
            ;;
        4)
            stackname="CassandraStack"
            tempfile="cassandra.yml"
            paramfile="cassandra-parameters.json"
            ;;
        5)
            stackname="RedshiftStack"
            tempfile="redshift.yml"
            paramfile="redshift-parameters.json"
            ;;
        6)
            stackname="SparkStack"
            tempfile="spark.yml"
            paramfile="spark-parameters.json"
            ;;
    esac
}
function CloudFormationModifications {
    SetupStack
    choice = 0 
    PromptUser
    while read choice
    do
        case $choice in
            1)
                CreateStack
                ;;
            2)
                UpdateStack
                ;;
            3)
                DeleteStack
                ;;
            4)
                DescribeStack
                ;;
            5)
                ValidateTemplate
                read end_wait
                ;;
            6)
                SetupStack
                ;;
            7) 
                echo "Exiting program!"
                break
                ;;
        esac
        PromptUser
    done
}
CloudFormationModifications