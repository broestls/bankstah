import datetime

APP_EPOCH = 1420070400000

def snowflake_to_ts(snowflake):
    #snowflake_binary = '{:064b}'.format(snowflake)
    #ts = int(snowflake_binary[0:42],2) + APP_EPOCH
    return (snowflake >> 22) + APP_EPOCH
