#!/bin/bash

pidwait() {
  kill -0 $1
  while [[ $? -ne 1 ]]; do
    sleep 1
    kill -0 $1
  done
}
