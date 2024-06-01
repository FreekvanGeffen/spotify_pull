SHELL=/bin/bash
NAME=spotify_pull

build:
	docker build --tag $(NAME) .

# interactive environment to play around
run: build
	docker run --entrypoint /bin/bash \
               --env-file .env \
               --interactive \
               --name $(NAME) \
               --rm \
               --tty \
               --user "$$(id -u)":"$$(id -g)" \
               --volume /etc/group:/etc/group:ro \
               --volume /etc/passwd:/etc/passwd:ro \
               --volume /etc/shadow:/etc/shadow:ro \
               --volume $(PWD):/usr/src \
               $(NAME)

# # run all the tests defined in this repository
# test: build
# 	docker run --env-file .env --name $(NAME)-tests --rm --tty $(NAME) \
# 		python -m pytest --capture=no \
# 							--color=yes \
# 							--cov=purview_push \
# 							--cov-report=term-missing \
# 							--override-ini="cache_dir=/tmp/pytest" \
# 							--verbose