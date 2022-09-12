#!/bin/bash

# datasource is USB wifi adapter interface in this case
# kismet -c <datasource> -f <config-file>
kismet -c wlp0s20f0u1 -f ./kismet_site.conf