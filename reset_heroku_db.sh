git pull
git push heroku
heroku pg:reset HEROKU_POSTGRESQL_COBALT_URL --confirm obscure-gorge-1962
#heroku run rake db:migrate
#heroku run rake db:seed
#heroku run rake db:setup
echo "no" | heroku run python manage.py syncdb
echo -e "import pizza_build\nquit()" | heroku run python manage.py shell
