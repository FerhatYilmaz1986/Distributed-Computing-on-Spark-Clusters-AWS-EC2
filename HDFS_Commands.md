## HDFS Commands Reference List With Examples

Some frequently used HDFS commands along with examples.


1. If you need HDFS command help

```
hadoop fs -help
```
Gives the list of all the HDFS commands and command description.

To get help about a specific command use that command with help.

As Example: If you want help about rm command

```
hadoop fs -help rm
```

-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ... :
  Delete all files that match the specified file pattern. Equivalent to the Unix
  command "rm <src>"
                                                                                 
  -f          If the file does not exist, do not display a diagnostic message or 
              modify the exit status to reflect an error.                        
  -[rR]       Recursively deletes directories.                                   
  -skipTrash  option bypasses trash, if enabled, and immediately deletes <src>.  
  -safely     option requires safety confirmation, if enabled, requires          
              confirmation before deleting large directory with more than        
              <hadoop.shell.delete.limit.num.files> files. Delay is expected when
              walking over large directory recursively to count the number of    
              files to be deleted before the confirmation. 

2. Another way to get help for an individual command is to use usage command. It will list all the options that can be used with the given command.

```
hadoop fs -usage rm 
```

Usage: hadoop fs [generic options] -rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...

3. HDFS command to create a directory

```
hadoop fs -mkdir
```

As example– HDFS command to create test directory inside /user directory.

```
hadoop fs -mkdir  /user/test
```

If you want to create parent directories along the path use -p switch.

As example If you want to create whole directory structure /user/test/abc

hadoop fs -mkdir -p /user/test/abc

4. To list all the directories and files in the given path

```
hadoop fs -ls
```

As example– HDFS command to list all the files under /user/test

```
hadoop fs -ls /user/test
```

To recursively list all the files and sub directories use -R switch.

For example, HDFS command to recursively list all the files and directories starting from root directory.

```
hadoop fs -ls -R /
```

5. HDFS command to delete a file

```
hadoop fs -rm
```

As example – To delete file display.txt in the directory /user/test

```
hadoop fs -rm /user/test/display.txt
```

To recursively delete a directory and any content under it use -R or -r option.

For example, HDFS command to recursively delete directory /user/test along with all the content under /user/test.

```
hadoop fs -rm -R /user/test/
```

Deleted /user/test

6. HDFS command to delete a directory.

```
hadoop fs -rmdir
```

As example – To delete directory /user/test. Note that rmdir command will delete a directory only if it is empty.

```
hadoop fs -rmdir /user/test/
```

7. To copy file from local file system to HDFS.

```
hadoop fs -put
```

As example – To copy file display.txt from /usr/netjs to /user/process in HDFS.

```
hadoop fs -put /usr/netjs/display.txt /user/process
```

8. To copy file from local file system to HDFS using copyFromLocal command.

As example – To copy file display.txt from /usr/netjs in local file system to /user/process in HDFS.

```
hadoop fs -copyFromLocal /usr/netjs/display.txt /user/process
```

9. To move file from local file system to HDFS. IF you use this command local file is deleted after it’s copied.

As example– HDFS command to move file display.txt from /usr/netjs to /user/process in HDFS.

hadoop fs -moveFromLocal /usr/netjs/display.txt /user/process

10. HDFS command to copy file from HDFS to local

```
hadoop fs -get
```

As example – If you want to copy file display.txt from /user/process in HDFS to /usr/netjs in local

```
hadoop fs -get /user/process/display.txt /usr/netjs/
```

11. Another way to copy file from HDFS to local is using copyToLocal command.

As example – If you want to copy file display.txt from /user/process in HDFS to /usr/netjs in local

```
hadoop fs -copyToLocal /user/process/display.txt /usr/netjs/
```

12. To copy file from one HDFS location to another HDFS location.

```
hadoop fs -cp
```

As example- If you want to copy display.txt file from /user/process to /user/test with in HDFS.

```
hadoop fs -cp /user/process/display.txt /user/test
```

13. HDFS command to display free space.

```
hadoop fs -df
```

14. To displays sizes of files and directories contained with in the given directory.

```
hadoop fs -du
```

As example - If you want to see the disk usage for /user directory

```
hadoop fs -du /user
```

22  /user/process
22  /user/test
0   /user/test1

15. HDFS command to see the content of the file.

```
hadoop fs -cat
```

As example – To display the content of the file /usr/process/display.txt

```
hadoop fs -cat /user/process/display.txt
```

16. Permanently delete files in checkpoints older than the retention threshold from trash directory, and create new checkpoint.

```
hadoop fs -expunge
```

17. HDFS command to change replication factor of a file.

```
hadoop fs -setrep
```

As example – If you want to change the replication factor of the file /user/process/display.txt to two.

```
hadoop fs -setrep 2 /user/process/display.txt
```

Replication 2 set: /user/process/display.txt

18. HDFS command to run HDFS filesystem checking utility.

```
hdfs fsck
```

As example – Running fsck for files under directory /user/process

```
hdfs fsck /user/process
```

/user/process/display.txt:  Under replicated BP-1309973318-127.0.1.1-1513945999329:blk_1073741865_1041. Target Replicas is 2 but found 1 live replica(s), 0 decommissioned replica(s), 0 decommissioning replica(s).
Status: HEALTHY
 Total size: 22 B
 Total dirs: 1
 Total files: 1
 Total symlinks:  0
 Total blocks (validated): 1 (avg. block size 22 B)
 Minimally replicated blocks: 1 (100.0 %)
 Over-replicated blocks: 0 (0.0 %)
 Under-replicated blocks: 1 (100.0 %)
 Mis-replicated blocks:  0 (0.0 %)
 Default replication factor: 1
 Average block replication: 1.0
 Corrupt blocks:  0
 Missing replicas:  1 (50.0 %)
 Number of data-nodes:  1
 Number of racks:  1
FSCK ended at Mon Feb 26 13:57:40 IST 2018 in 1 milliseconds

19. If you want to change group association of files.

```
hadoop fs -chgrp
```

As example – Change group of /user/process/display.txt file to sales.

```
hadoop fs -chgrp sales /user/process/display.txt
```

20. To change the permissions of files.

```
hadoop fs -chmod
```

As example - If you want to provide read, write and execute permissions to user and read permission to group and others for file /user/process/display.txt.

```
hadoop fs -chmod 744 /user/process/display.txt
```

21. block and file information

```
hdfs fsck / -files -blocks
```


