#!/usr/bin/env bash
#########################################################################################################################
# CSC4006 - Research And Development Project
# Developed by: Jonathan McChesney (MEng Computer Games Development)
# Queen's University Belfast
#
# Component: config.sh
#
# Purpose: Configuration (config) file paramter setup, used to customise the development/deployment environment.
#
#########################################################################################################################
cloudaddress="ec2-XXX" 							# Cloud EC2 instance address
clouduser="ubuntu" 								# Cloud username e.g. IAM user ec2user1
cloudpublicip=XX.XXX.XX.XXX						# Cloud public ip address
edgeaddress1=192.168.0.101						# Edge Node 01 ip address
edgeuser1=pi									# Edge Node 01 username
edgeaddress2=192.168.0.101						# Edge Node 02 ip address
edgeuser2=pi									# Edge Node 02 username
awskey=~/home/farooq/DeFog/DeFog/configs/emptyawskey.pem 		# .pem file location on the local user device
edgeawskey=/home/DeFog/DeFog/configs/emptyawskey.pem 		# .pem file location on the Edge Node
foglampaddress="http://localhost:8081"			# foglamp localhost server addresss
