#!/bin/bash

# Список таблиц для исключения
exclude_tables=("calls" "calls_contacts" "cases" "contacts_proj2_sms_pool_1_c" "contacts_pws_meets_1_c" "leads" "opportunities" "opportunities_contacts" "proj1_finoperation" "proj1_finoperation_contacts_c" "pupil" "visits" "contacts_cases")

# Восстановление всех таблиц, кроме исключенных
zcat /rsnapshot-mysql/crm_fors.sql.gz | sed -n -e '/DROP TABLE/,/UNLOCK TABLES/p' | awk '/DROP TABLE/ {flag=1; table=substr($3, 2, length($3)-2)} flag==0 || table ~ /^(calls|calls_contacts|cases|contacts_proj2_sms_pool_1_c|contacts_pws_meets_1_c|leads|opportunities|opportunities_contacts|proj1_finoperation|proj1_finoperation_contacts_c|pupil|visits|contacts_cases)$/ {print} flag==1 && table ~ /^(calls|calls_contacts|cases|contacts_proj2_sms_pool_1_c|contacts_pws_meets_1_c|leads|opportunities|opportunities_contacts|proj1_finoperation|proj1_finoperation_contacts_c|pupil|visits|contacts_cases)$/ {flag=0}' | mysql -u 'root' -p crm_videoforme
