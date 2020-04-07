# DeFog: Fog Computing Benchmarks
## Demystifying Cloud-Edge Interactions of a Fog System Using Container-based Benchmarking

### Citing this Research
Jonathan McChesney, Nan Wang, Ashish Tanwer, Eyal de Lara, and Blesson Varghese, "DeFog: Fog Computing Benchmarks," ACM/IEEE Symposium on Edge Computing, 2019. 

Link to PDF: http://bvarghese.staff.cs.qub.ac.uk/papers/DeFog-SEC2019.pdf.

### How to Run
navigate to the DeFog folder:
```$ sh defog .```

### How to View Help
navigate to the DeFog folder:
```$ sh defog -?```
* view the help video for further information regardings setting up the .ssh and .aws folders, as well as JMeter and Taurus integration.

### How to run iPokeMon JMeter
* First build the docker image and container, use `$ . enter` to manually enter the container
* Navigate to the Cloud-Server using `$ cd Experiments/iPokeMon/ipokemon/Application/iPokeMon-CloudServer/`
* Start up the server `$ . runCloud.sh`, and use `crtl-c` to return from console output
* Enter `ctrl-p and ctrl-q` to detach container
exit back to the user device

### User Device Dependencies
* Install 'bc'
* Ensure the latest version of bash is installed
* Install the latest version JMeter to the JMeter folder, a template structure is provided, but this may not be compatible with the edge devices local java version etc. Ensure the version of JMeter installed has the ApacheJMeter.jar within the bin folder. As of April 2019, the latest version of JMeter may not have the Jar file, use apache-jmeter-2-6 in this case. As such, the contents of this folder can be overwritten with the newest version of JMeter running Java 8.
* Ensure JMeter user and system path/environment variables are set up (JAVA_HOME and PATH). Defog has been using `jdk1.8.0_101` and `jdk1.8.0_102`.
```
Include a JAVA_HOME path variable, with value C:\Program Files\Java\jdk1.8.0_181 (or the latest version of JAVA 8 jdk/jre)
Append C:\Users\jmcch\AppData\Local\Taurus\bin, C:\Program Files (x86)\Common Files\Oracle\Java\javapath and C:\Program Files\Java\jdk1.8.0_181 to the system and user variables
```

If `Files/Java/jdk1.8.0_102/bin/java: No such file or directory` appears, this means the path/user variables are not set up correctly for JMeter, please consult the Apache JMeter documentation to fix this issue.

* Install `Taurus` bzt
* Update the configuration file (DeFog/configs/config.sh) is updated to the relevant values.
Using root access allows elevated permissions, e.g. root@123.123.12 etc. Ensure DeFog can use SSH without prompting for user interaction, e.g. entering a password. If prompted to enter a password consult ssh password-less documentation. If its the first time use, the terminal may prompt to add the address to known hosts, which is populated in the user device (or edge nodes) .ssh folder.
* Use putty to create a .pem file and update the awsemptykey.pem
* Use putty or keygen to create a ssh keys
```
$ ssh-keygen
// copy to authorized keys - should now allow ssh without prompting a password
root@123.123.12
```
* Update the .aws folder and  create a ```config``` folder and add the region: 
```
[default]
region = eu-west-1
```
* Update the .aws folder and  create a ```credentials``` folder and add the iam users aws_access_key_id and secret_aws_access_key_id: 
```
[default]
aws_access_key_id = XXXX
aws_secret_access_key = YYYY
```
* Update the .ssh folder with the devices id_rsa and id_rsa.pub ssh keys
Creating a ssh key documentation: ```https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows```

If an issue us thrown regarding '\r' line endings, this is due to GitLab automatically converting line endings LF to CRLF, this can mitigated by updating the config: `$ git config --global core.eol lf`. The line endings should be Unix (LF) format, consult git documentation to update the local git attributes to ensure the correct line endings are used.
```
* text=auto
*.txt text
*.c text
*.h text
*.jpg binary
```

If an error is thrown when connecting to the Cloud instance this is likely due to the .aws folder's contents not being set up correctly, ensure the IAM user created has the necessary priviliges/authentication to remotely access the EC2 instance and the keys are added in the format above. If the issue persists then it may be benefical to consult the AWS documentation regarding remotely accessing an EC2, as this will outline the individual steps required to set up the .aws folder.

If an issue is thrown when using secure shell to connect to the Edge or Cloud, then ensure the .ssh folder has been set up correctly. This should contain the public and private ssh keys generated. Authorized keys and known_hosts will be populated to this folder over time.

### Cloud Platform
* DeFog has been tested using an AWS EC2 ubuntu 18.04 instance, located in Dublin, Ireland. As well as an AWS S3 bucket.
* Create an AWS account and create an IAM user with the necessary privileges.
* Create an EC2 instance and S3 bucket. Assign the name `csc4006benchbucket` to the bucket.
* Update the local .ssh and .aws with the IAM users credentials (secret access keys) on the user device and Edge Nodes.

If issues arise when setting up IAM users or updating the ssh or aws credentials on the edge nodes and user device consult the AWS documentation: 
```https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html```

### Edge Platform
* DeFog has been tested using an Odroid XU 4 board with ubuntu 14.04 and a Raspberry Pi 3 running NOOBS Raspbian.
* Update the local .aws with the IAM users credentials on the edge Edge Nodes.
* Update the local .ssh with an `authorized_keys` file, containing the generated public rsa ssh key on the user device. Use ssh or scp to add this file to the .ssh folder.

If an error is thrown when DeFog attempts to upload the results to the S3 bucket, it is likely the .aws credentials are not set up correctly on the edge node. If necessary, ssh/scp the relevant access keys to the devices .aws folder. Ensure the .aws folder is located at root, i.e. `/root/.aws` as this is the location the docker run scripts look for.

If an error is thrown or ssh prompts a password or terminal interaction then the .ssh folder may not be set up correctly on the edge node. Ensure the the folder is located at `/root/.ssh` and contains the `authorized_keys` folder which is populated with the user devices public rsa key e.g. `ssh-rsa VVVV343BJ...`.
