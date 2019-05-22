ifeq (run,$(firstword $(MAKECMDGOALS)))
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(RUN_ARGS):;@:)
endif

build:
	python Proj.py
run :
	 ./Proj.py $(APPID) $(CITY) $(RUN_ARGS)
