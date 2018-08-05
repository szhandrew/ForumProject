# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end


# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
	path "/etc/ntp.conf"
end
execute 'ntp_restart' do
	command 'service ntp restart'
end
package "curl"
package "python3-pip"
package "python3-dev"
package "nodejs"



#Postgres
package "postgresql"
execute 'postgres_user' do
	command 'echo "CREATE DATABASE mydb; CREATE USER vagrant; GRANT ALL PRIVILEGES ON DATABASE mydb TO vagrant;" | sudo -u postgres psql'
end

# nginx
package "nginx"
cookbook_file "nginx-default" do
	path "/etc/nginx/sites-available/default"
end
service "nginx" do
	action :restart
end

# Django Deploy mode
package "postgresql-server-dev-all"
package "libpython3-dev"
execute 'install django uwsgi' do
	command 'pip3 install django psycopg2 uwsgi'
end




#### -------------project dependencies---------------
execute 'install_django' do
	command 'pip3 install Django==1.11'
end

execute 'install_dependencies' do
	command 'pip3 install Markdown==2.6.8 \
	Pygments==2.2.0 \
	pytz==2016.10 \
	django-haystack==2.6.1 \
	jieba==0.38 \
	Whoosh==2.7.4 \
	beautifulsoup4'
end

execute 'install_channels' do
	command 'pip3 install channels'
end

execute 'install_redis' do
	command 'pip3 install channels_redis'
end

execute 'add_docker_gpg_key' do
	command 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -'
end

execute 'add_docker_repository' do
	command 'sudo add-apt-repository \
	"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) \
	stable"'
end

package "docker-ce"


execute 'django_db_makemigrations' do
	user 'vagrant'
	cwd '/home/vagrant/project/'
	command 'python3 manage.py makemigrations'
end


execute 'django_db_migrate' do
	user 'vagrant'
	cwd '/home/vagrant/project/'
	command 'python3 manage.py migrate'
end

# execute 'start_redis_server' do
# 	command 'docker run -p 6379:6379 -d redis:2.8'
# end


execute 'fixture' do
	user 'vagrant'
	cwd '/home/vagrant/project/'
	command 'python3 manage.py loaddata initial_data.json'
end



# execute 'start_django_server' do
# 	cwd '/home/vagrant/project/'
# 	command 'python3 manage.py runserver 0:8000 &'
# end