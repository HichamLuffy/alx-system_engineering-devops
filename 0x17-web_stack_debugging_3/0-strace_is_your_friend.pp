# run apach2 'sudo service apach2 start'
# check apach statu 'sudo service apache2 status'
# run `ps aux | grep apache` to find PID of the Apache process
# use 'sudo strace -p <PID>' to trace the Apache process
# open another terminal and run 'curl http://localhost'
# Analyze the strace output:  the output that might indicate the cause of the 500 error.
# focus on lines that contain "ERROR", "FAIL", or "500"
# take appropriate actions to resolve it.

# replace .phpp with .php in wp-settings.php
exec { 'fix wordpress':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
