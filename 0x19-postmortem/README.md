0x19-Postmortem
System Engineering & DevOps - On Call
Objective -  Write a 400 to 600 word Postmortem, describing a server outage and how the outage was corrected. 

Summary
GET requests to the Apache2 server were returning 500 errors, indicating an internal server error. This could be a misconfiguration or syntax error of the PHP or MySQL files.

Timeline
3-4-2019, 6:00 am PDT: Problem identified when GET request returned 500 error.
3-4-2019, 6:01 am PDT: Checked if Apache and MySql were running.
3-4-2019, 6:02 am PDT: Ran a strace on the Apache www-data process.
3-4-2019, 6:04 am PDT: Found syntax error in wp-settings.php file.
3-4-2019, 6:25 am PDT: Corrected syntax error manually.
3-4-2019, 6:45 am PDT: Restarted Apache server. 200 status returned.
3-4-2019, 7:00 am PDT: Deployed a Puppet script to all servers, fixing the syntax error.
3-4-2019, 7:10 am PDT: Pushed Puppet code to Git Hub.

Impact 
Outage lasted 7 hours. Users were unable to reach the site during this time

Root Cause
A typo in the wp-settings.php file, located at var/www/html. The typo was in line that read "/class-wp-locale-phpp" -  should have been "/class-wp-locale.php". Human error. Testing before deploying code is the proper procedure.

Solution
Find running processes with ps auxf command. Run strace on suspected processes to find error. Manually fix error and restart server. Write script to fix all servers.

Prevention
Testing files after making changes. A simple curl -sI to the server would be the first step, ensuring the proper response is returned. Testing procedures should be reviewed and implemented by all.  