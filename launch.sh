#!/bin/bash

heroku ps:scale web=1
heroku ps
heroku open
