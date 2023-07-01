#!/bin/bash

# Send GET request to the URL with X-School-User-Id header
curl -s -H "X-School-User-Id: 98" "$1"
