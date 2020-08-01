#!/bin/bash

docker build -t idle-trading-hero-strategies .
docker tag idle-trading-hero-strategies idletradinghero.azurecr.io/idle-trading-hero-strategies
docker push idletradinghero.azurecr.io/idle-trading-hero-strategies