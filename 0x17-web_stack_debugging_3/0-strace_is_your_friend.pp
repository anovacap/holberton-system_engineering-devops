# puppet script to correct a typo in a file
exec { 'modify_file':
  command => "/bin/sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php"
}
