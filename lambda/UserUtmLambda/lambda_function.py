from __future__ import print_function

import json
import psycopg2


REDSHIFT_DBNAME = "INSERT_NAME_HERE"
REDSHIFT_USER = "INSERT_USER_HERE"
REDSHIFT_PASS ="INSERT_PASSWD_HERE"
REDSHIFT_PORT ="INSERT_PORT_HERE"
REDSHIFT_ENDPOINT ="INSERT_REDSHIFT_ENDPOINT_HERE"
REDSHIFT_ROLE ="INSERT_REDSHIFT_ROLE_HERE"


def lambda_handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    print(message)
    
    conn = psycopg2.connect("dbname=" + REDSHIFT_DBNAME + " user=" + REDSHIFT_USER + " password=" + REDSHIFT_PASS + " port=" + REDSHIFT_PORT + " host=" + REDSHIFT_ENDPOINT, sslmode='require')
    conn.autocommit = True
    cur = conn.cursor()
    
    print(message)
    
    insert_query = """
        INSERT INTO tracking.utm (
            request_id,
            source,
            medium,
            campaign,
            content,
            term,
            matchtype,
            network,
            ad_id,
            ad_pos,
            placement,
            placement_category,
            testgroup,
            device
        )
        VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14});
    """.format(message["request_id"], message["source"], message["medium"], message["campaign"], message["content"], message["term"], \
    message["matchtype"], message["network"], message["ad_id"], message["ad_pos"], message["placement"], message["placement_category"], \
    message["testgroup"], message["device"])
    
    cur.execute(insert_query)
    cur.close()
    conn.close()
