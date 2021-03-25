#!/usr/bin/python3

import os
#import pyttsx3
import platform
my_system = platform.uname()

print("----------------------------------- Greeting from Us ! -------------------------------")
print("----------------------------  Hello Sir ! How can I serve you ? -------------------------")
print()

#pyttsx3.speak("Helllllo ! How can I help")
print("                                     ***          ***\n                                     ***          ***\n                                     ***          ***\n                                            **\n                                            **\n                                      **          **\n                                      ***        ***\n                                        ***     ***\n                                           *****\n")

#Functions Starts
def EC2Options():
    if my_system.system == 'Windows' :
        os.system('cls')
    elif my_system.system == 'Linux' :
        os.system('clear')
    else :
        print("We are Sorry but the program is not meant for your OS")
        exit()
    print("Make your Choice: ")
    print()
    print("1: Get Info about Running Instances")
    print("2: Create a Key Pair for EC2 Instances")
    print("3: Create a security group and Configure Created Security Group")
    print("4: Add Ingress Rules in Security Group")
    print("5: Launch an instance")
    print("6: Create an EBS Storage")
    print("7: Attach an EBS Storage")
    ans = input("Your Answer : ")
    print()
    if ans == "1" :
        print("Creating Key Pair.....",)
        name = input("Name of Key Pair: ")
        os.system('aws ec2 describe-instances')
        print()
    elif ans == "2" :
        print("Creating Key Pair.....",)
        name = input("Name of Key Pair: ")
        os.system('aws ec2 create-key-pair --key-name {0} --query KeyMaterial --output text > {0}.pem'.format(name))
        print("!! Key Created Successfully !!")
    elif ans == "3" :
        print("Creating Security Group......")
        name = input("Name of Security Group: ")
        des = input("A little description of your security group: ")
        os.system('aws ec2  create-security-group --group-name {} --description "{}" '.format(name,des))
        print("!! Security Group created Successfully !!")
        print()
        print("Configuring security group......\n")
        print('Example:\n For SSH from any IPv4: \n tcp,22,0.0.0.0/0')
        info = input("Protocol: ,Port No: , CIDR Range: ")
        info = info.split(',')
        os.system('aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}'.format(name,info[0],info[1],info[2]))
        print("!! Security Group Created Successfully")
        print("You can allow more ingress rules from the config menu")
    elif ans == "4" :
        print("Adding Ingress Rules in Security Group........")
        name = input("Name of Security Group: ")
        info = input("Protocol: ,Port No: , CIDR Range: ")
        info = info.split(',')
        os.system('aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}'.format(name,info[0],info[1],info[2]))
        print("!! Ingress Rules Added Successfully")
    elif ans == "5" :
        print("About to Launch an Instance")
        print()
        print("Example: Redhat AMI = ami-052c08d70def0ac62")
        image = input("AMI ID: ")
        cout = input("No. of Instances: ")
        print()
        print("Example: t2.micro is one the Instance type available free for 12-months from registration")
        instype = input("Instance type: ")
        key = input("Key Name: ")
        sgname = input("Security Group Name:")
        print()
        #print("Example: You can give list of Tags like {Key=string,Value=string},{Key=string,Value=string}")
        #tag = input("Tags (list): ")
        print("Output: ")
        os.system('aws ec2 run-instances --image-id {} --count {}  --instance-type {}  --key-name {} --security-groups {} '.format(image,cout,instype,key,sgname))
        print()
        print("Instance Launched if No error Appears in output")
    elif ans == "6":
        print("About to Create an EBS Storage......")
        print()
        print("Example: By default we have gp2 volume-type i.e. general purpose ssd harddisk")
        vol = input("Volume-type: ")
        size = input("Size (in GBS): ")
        print()
        print("Example: In Mumbai Datacenter we have three availability zone namely ap-south-1a,ap-south-1b and ap-south-1c")
        az = input("Availability Zone: ")
        os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vol,size,az))
    elif ans == "7":
        print("About to Attach EBS storage to any Instance ")
        print("Note: You must know the volume-id and instance-id to attach to and find it below")
        print()
        print('Current Volumes Present :')
        os.system('aws ec2 describe-volumes')
        print()
        vid = input("So tell the Volume ID: ")
        print('Current Instances Present : ')
        os.system('aws ec2 describe-instances')
        print()
        iid = input("So Tell the Instance ID: ")
        os.system('aws ec2 attach-volume volume-id {} --instance-id {} --device /dev/sdf'.format(vid,iid))


def S3Options():
    if my_system.system == 'Windows' :
        os.system('cls')
    elif my_system.system == 'Linux' :
        os.system('clear')
    else :
        print("We are Sorry but the program is not meant for your OS")
        exit()
    print("Make your Choice: ")
    print("1: Get info About Running S3 Storage")
    print("2: Create an Object Storage S3")
    print("3: Delete a S3 Bucket")
    print("4: Public Access for Buckets")
    print("5: Put an Object into Bucket")
    print("6: Manage Object Permissions")
    ans = input("Your Answer : ")
    print()
    if ans == "1" :
        os.system('aws s3api list-buckets')
    elif ans == "2" :
        print("Creating S3 Bucket.....",)
        name = input("Name of Bucket: ")
        region = input("Region to which Bucket has to be Launched: ")
        os.system('aws s3api create-bucket --bucket {0} --region {1} --create-bucket-configuration LocationConstraint={1}  --object-lock-enabled-for-bucket '.format(name,region))
        print("!! Bucket Created Successfully !!")
    elif ans == "3" :
        print("About to Delete a Bucket",)
        name = input("Name of Bucket: ")
        region = input("Region on which Bukcet is present: ")
        os.system('aws s3api delete-bucket --bucket {} --region {} '.format(name,region))
        print("!! Bucket Created Successfully !!")
    elif ans == "4":
        name = input("Name of Bucket: ")
        choice = input("Public Access Allow(y)/Disable(n): ")
        if choice == "y":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" '.format(name))
        elif choice == "n":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" '.format(name))    
    elif ans == "4":
        name = input("Name of Bucket: ")
        choice = input("Public Access Allow(y)/Disable(n): ")
        if choice == "y":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" '.format(name))
        elif choice == "n":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" '.format(name))    
    elif ans == "5":
        name = input("Name of Bucket: ")
        print()
        print("Example: IN Windows --> \to\path \nIN Linux --> /to/path")
        print()
        path = input("Location/Path of Object in Your OS/PC: ")
        opath = input("Location/Path of Object to be reflected in S3: ")
        os.system('aws s3api put-object --bucket {} --key {} --body {} '.format(name,opath,path))
    elif ans == "6":
        name = input("Name of Bucket: ")
        print()
        opath = input("Location/Path of Object in S3: ")
        print("Permissions to Object : ")
        print()
        print("1: Make Object Public Readable")
        print("2: Make Object Public Read-Writable")
        print("3: Make Object Private")
        ans = input("Your Answer: ")
        if ans == "1":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "public-read" '.format(name,opath))
        elif ans == "2":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "public-read-write" '.format(name,opath))
        elif ans == "3":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "private" '.format(name,opath))
        else:
            print("Unsupported Option")
            exit()
        print("!! Permissions Changed Successfully !!")
    else:
        print("Unsupported Option")
        exit()

def LVMOptions():
    
        if my_system.system == 'Windows' :
            os.system('cls')
        elif my_system.system == 'Linux' :
            os.system('clear')
        else :
            print("We are Sorry but the program is not meant for your OS")
            exit()
        print("Make your Choice: ")
        os.system("clear")		
        print("Press 1 : to know how many virtual harddisk are there")
        print("Press 2 : to know all about the filesystems present in system")
        print("Press 3 : to make physical volume from the no of disk as you want")
        print("Press 4 : to know whether phycical volume is created or not")
        print("Press 5 : to create volume group from the physical volume created")
        print("Press 6 : to know whether volume group is created or not")
        print("Press 7 : to make partition of volume group created")
        print("Press 8 : to know the information regarding the partitions created")
        print("Press 9 : to format the partitions created")
        print("Press 10 : to mount the partitions created")
        print("press 11 : to extend the partion size")
        print("Press 12 : to reduce the partition size")
        print("Press 13 : to know about the partition whether the partion is created/mounted or not")
        print("Print 14 : to check any disruption in filesystem")
        c=input("Enter your choice : ")
        print(c)
        if int(c)==1:
            os.system("fdisk -l")
        elif int(c)==2:
            os.system("df -hT")
        elif int(c)==3:
                j=input("no of disks from which you wanna make physical volume : ")
                for i in range(int(j)):
                    print("type the disk name to create physical volume : ")
                    diskname = input()
                    os.system("pvcreate "+diskname)
        elif int(c)==4:
                os.system("pvdisplay")
        elif int(c)==5:
                t=input("no. of pvs from which you wanna make vg : ")
                q=" "
                for r in range(int(t)):
                    pvname = input("type your pv name : " )
                    q=q+" "+pvname
                print(q)
                vgname = input("type the name of vg you want to create : ")
                os.system("vgcreate "+vgname+" "+q)
        elif int(c)==6:
                os.system("vgdisplay")
        elif int(c)==7:
                vgname=input("type the volume group name : ")
                prtnname=input("type the partition name : ")
                print("type the size in Gb/Mb to create partiton.. specify Mb as M and Gb as G")
                s=input()
                print("type the name of partition that you wish to create")
                prtnname=input()
                os.system("lvcreate --size "+s+ "--name" +prtnname+" "+vgname)
        elif int(c)==8:
                os.system("lvdisplay")
        elif int(c)==9:
                vgname=input("type the volume group name : ")
                prtnname=input("type the partition name : ")
                os.system("mkfs.ext4  /dev/"+vgname+"/"+prtnname)
        elif int(c)==10:
                vgname=input("type the volume group name : ")
                prtnname=input("type the partition name : ")
                print("type the name of directory to mount ")
                dirname=input()
                os.system("mkdir "+dirname)
                os.system("mount /dev/"+vgname+"/"+prtnname+"+/"+dirname)
        elif int(c)==11:
                vgname=input("type the volume group name : ")
                prtnname=input("type the partition name : ")
                print("type the size in gb by which you wish to extend the size")
                esize=input()
                os.system("lvextend --size +"+esize+" /dev/"+vgname+"+/"+prtnname)
                os.system("resize2fs /dev/"+vgname+"+/"+prtnname)
        elif int(c)==12:
                vgname=input("type the volume group name : ")
                prtnname=input("type the partition name : ")
                dirname=input()
                os.system("mkdir "+dirname)
                print("type the size by which you wish to reduce the size ..specify Mb as M and Gb as G")
                rs=input()
                os.system("umount /dev/"+vgname+"/"+prtnname+"+/"+dirname)
                os.system("lvreduce --size +"+rs+" /dev/"+vgname+"+/"+prtnname1)
                os.system("resize2fs /dev/"+vgname+"+/"+prtnname)
                os.system("mount /dev/"+vgname+"/"+prtnname+"+/"+dirname)
        elif int(c)==13:
                os.system("df -h")
        elif int(c)==14:
                fsname=input("type disk name for which you wanna check desruption : ")
                os.system("e2fsck -f "+fsname)
        else:
                print("System could not able to find specified cmd")




def DockOptions():
    
        if my_system.system == 'Windows' :
            os.system('cls')
        elif my_system.system == 'Linux' :
            os.system('clear')
        else :
            print("We are Sorry but the program is not meant for your OS")
            exit()
        print("Make your Choice: ")
        print("Press 1 : to install docker")
        print("Press 2 : to check whether docker is installed or not")
        print("Press 3 : to start docker services")
        print("Press 4 : to know about the docker images present") 
        print("press 5 : to downlod docker image")
        print("Press 6 : to remove docker image")
        print("Press 7 : to run the os/container")
        print("Press 8 : to exit from os which is currently running") 
        print("Press 9 : to remove perticular container")
        print("Press 10 : to remove all the running container")
        print("press 11 : to know how many os/containers are running under docker")
        print("Press 12 : to enable docker permanently")
        print("Press 13 : to check docker state(active/inactive)")
        
        ch=input("Enter your choice : ")
        print(ch)
        
        if int(ch)==1:
            url=input("Enter the url of required docker : ")
            os.system("curl -sSL " +url)
            print("docker has installed pls check to confirm by pressing no two")
        elif int(ch)==2:
            os.system("rpm -q docker -ce")
        elif int(ch)==3:
            os.system("systemctl start docker")
        elif int(ch)==4:
            os.system("docker images")
        elif int(ch)==5:
            imgname=input("type the docker image name that you wish to download : ")
            os.system("docker pull" +imgname)
        elif int(ch)==6:
            img=input("type the image name alog with its version in the formate name:version that you wish to remove")
            os.system("docker rmi "+img+ "-f")
        elif int(ch)==7:
            dn=input("type os/container name that you wish to run : ")
            nm=input("type the name you wish to give this os : ")
            os.system("docker run -i -t --name" +nm+ ""+dn)
        elif int(ch)==8:
            os.system("exit")
        elif int(ch)==9:
            cn=input("type the docker container name that you wish to remove : ")
            os.system("docker container rm "+cn)
        elif int(ch)==10:
            os.system("docker container rm -f $(docker conatiner ls -a -q)")
        elif int(ch)==11:
            os.system("docker ps -a")
        elif int(ch)==12:
            os.system("systemctl enable docker")
        elif int(ch)==13:
            os.system("systemctl status docker")
        else:
            print("system has not found the specified command")


def HadoopOptions():
    
    if my_system.system == 'Windows' :
        os.system('cls')
    elif my_system.system == 'Linux' :
        os.system('clear')
    else :
        print("We are Sorry but the program is not meant for your OS")
        exit()
    print("Make your Choice: ")
    print()
    print("1: Install Hadoop Software")
    print("2: Setup your system as NameNode")
    print("3: Setup your system as DataNode")
    print("4: Start your system as NameNode")
    print("5: Start your system as Datanode")
    print("6: Insert some text file into your cluster")
    print("7: Read a file from your cluster")
    print("8: Change Block Size")
    print("9: Change No. of Replicas")
    print("10: Enter/Exit Safe Mode")
    ans = input("Your Answer : ")
    print()
    if ans == "1" :
        print("Note: Make sure that Java is installed in your system for HAdoop to work")
        print()
        print("Do you Wish to Download JDK and Hadoop from Internet \n[y] for Online [n] for Offline : ")
        ans = input("Your Answer: ")
        if ans == "y":
            os.system('wget -c https://archive.apache.org/dist/hadoop/common/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm')
            print("!! Software Downloaded !!")
        elif ans == "n":
            os.system('Proceeding Offline Mode')
        else:
            print("Unsupported Option")
            exit()
        print("Starting Installation.....")
        os.system('rpm -i --force hadoop-1.2.1-1.x86_64.rpm ')
        print("!! Hadoop-1.2.1 is installed in your system !!")
        print("Note: Ignore the two errors that you may see above ")
    elif ans == "2":
        print()
        print("Note: This will Remove all previous configuration for HDFS And Core file !!")
        print()
        print("Eample: You can use /nn as the directory")
        direct = input("Enter the directory for NameNode: ")
        print()
        print("Example: localhostip:port (192.168.43.123:9001)")
        print("Note: Make Sure that the port is free for usage")
        ip = input("Enter the Ip Address:Port of NameNode hadoop server")
        print()
        os.system('mkdir {}'.format(direct))
        os.system('sudo cp -rf menu/hdfs-site.xml /etc/hadoop/hdfs-site.xml')
        os.system('sudo cp -rf menu/core-site.xml /etc/hadoop/core-site.xml')
        os.system("echo -e '<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>' >> /etc/hadoop/hdfs-site.xml ".format(direct))
        os.system("echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}</value>\n</property>\n</configuration>' >> /etc/hadoop/core-site.xml ".format(ip))
        os.system('hadoop namenode -format')
        print("!!Your System has been configured for NameNode!!")
    elif ans == "3":
        print("Note: This will Remove all previous configuration for HDFS And Core file !!")
        print()
        print("Example: You can use /nn as the directory")
        direct = input("Enter the directory for DataNode: ")
        print()
        print("Example: localhostip:port (192.168.43.123:9001)")
        print("Note: Make Sure that the port is free for usage")
        ip = input("Enter the Ip Address:Port of NameNode hadoop server: ")
        print()
        os.system('mkdir {}'.format(direct))
        os.system('sudo cp -rf menu/hdfs-site.xml /etc/hadoop/hdfs-site.xml')
        os.system('sudo cp -rf menu/core-site.xml /etc/hadoop/core-site.xml')
        os.system("echo -e '<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n</configuration>' >> /etc/hadoop/hdfs-site.xml ".format(direct))
        os.system("echo -e '<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}</value>\n</property>\n</configuration>' >> /etc/hadoop/core-site.xml ".format(ip))
        print("!!Your System has been configured for DataNode!!")
    elif ans == "4":
        print("Starting as NameNode...")
        os.system('hadoop-daemon.sh start namenode')
    elif ans == "5":
        print("Starting as DataNode...")
        os.system('hadoop-daemon.sh start datanode')
    elif ans == "6":
        print("Example: You can use syntax /root/filename.txt")
        print()
        path = ("Give the Path to file in your System ")
        print("Example: Normally we give path of file like /")
        print()
        hpath = ("Give the Path of file to be reflected into your cluster")
        os.system("hadoop fs -put {} {}".format(path,hpath))
    elif ans == "7":
        print("Example: IF Your file is saved in /file.txt directiry then use /file.txt")
        hpath = ("Give the Path of file to be reflected into your cluster")
        os.system("hadoop fs -cat {}".format(hpath))
    elif ans == "8":
        print("Note: Please first configure hsdfs and core files before coming into this option")
        rep = input("Enter no. of Replicas: ") 
        os.system('grep -v "/configuration" /etc/hadoop/hdfs-site.xml > a.txt')
        os.system('cat a.txt > /etc/hadoop/hdfs-site.xml')
        os.system("echo -e  '\n<property>\n<name>dfs.replication</name>\n<value>{}</value>\n</property>\n</configuration>' >> /etc/hadoop/hdfs-site.xml ".format(rep))
        print("!! Configuration Changed !!")
    elif ans == "9":
        print("Note: Please first configure hsdfs and core files before coming into this option")
        size = input("Enter Block Size (in Bytes): ")
        os.system('grep -v "/configuration" /etc/hadoop/hdfs-site.xml > a.txt')
        os.system('cat a.txt > /etc/hadoop/hdfs-site.xml')
        print()
        os.system("echo -e  '\n<property>\n<name>dfs.block.size</name>\n<value>{}</value>\n</property>\n</configuration>' >> /etc/hadoop/hdfs-site.xml ".format(size))
        print("!! Configuration Changed !!")
    elif ans == "10":
        print("Make your Choice: ")
        print()
        print("1: Enter Safemode")
        print("2: Leave Safemode")
        print("3: Check Mode Status")
        print()
        ans = input("Your Answer: ")
        if "1" in ans:
            os.system('hadoop dfsadmin -safemode enter')
        elif "2" in ans:
            os.system('hadoop dfsadmin -safemode leave')
        elif "3" in ans:
            os.system('hadoop dfsadmin -safemode get' )
    else:
        print("Unsupported Options")


def Options():
    print("Which of the Services you want to Access ? : ")
    print()
    print("AWS Services")
    print(" 1: EC2 Services")
    print(" 2: S3 Services")
    print()
    print("3: LVM Services")
    print("4: Docker Services ")
    print("5: Hadoop Services")
    choice = input("Option: ")
    print()
    if choice == "1":
        EC2Options()
    elif choice == "2":
        S3Options()
    elif choice == "3":
        LVMOptions()
    elif choice == "4":
        DockOptions()
    elif choice == "5":
        HadoopOptions()
    else :
        print("Unsupported Option")
        print("Exiting....")

#Code Starts
Options()

while True :
    choice = input("So would you like to continue the program [y] / n : ")
    if (choice == "y"):
        if my_system.system == 'Windows' :
            os.system('cls')
        elif my_system.system == 'Linux' :
            os.system('clear')
        Options()
    elif (choice == "n") :
        print()
        print("See you Later.......")
 #       pyttsx3.speak("Bye Bye")
        exit()
