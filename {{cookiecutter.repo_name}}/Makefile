# Use: cat -e -t -v makefile_name 
# to check formatting. There must be tabs on each line
.PHONY: build deploy

build:
		git init
		heroku create
		heroku config:set SECRET_KEY=myscretekeybaz
		git add .
		git commit -m "initial commit"

deploy:
		git push -u heroku master