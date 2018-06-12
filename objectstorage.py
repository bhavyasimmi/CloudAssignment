#!/usr/bin/python2
import  cgi,commands,os
print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

#  drive name 
drive_name=web.getvalue('dn')
#  drive size in MB 
drive_size=web.getvalue('ds')
button_name=web.getvalue('button')
#  creating  thin LVM  partition 


commands.getoutput('sudo lvcreate  --name  '+drive_name+'  -V'+drive_size+'M   --thin  cloud/pool1')

#  now formating the Partion 
commands.getoutput('sudo mkfs.xfs    /dev/cloud/'+drive_name )

#  mount storage  on server side first  
commands.getoutput('sudo mkdir   /var/www/html/'+drive_name)
# now mounting 
commands.getoutput('sudo mount  /dev/cloud/'+drive_name+'       /var/www/html/'+drive_name)
#<a href='http://192.168.122.44/drive_name'>GO TO Your Storage</a>
print """
Content-type:text/html\n
<html>
<body>
<p>Your Storage Is Sucessfully Generated</p>

</body>
</html>
      """
