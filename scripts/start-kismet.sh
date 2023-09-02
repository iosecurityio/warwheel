#!/bin/bash

# datasource is USB wifi adapter interface in this case
# kismet -c <datasource> -f <config-file>
# The configuration file eliminates cli opts
kismet -c wlp0s20f0u1 -f ../conf/kismet.conf
