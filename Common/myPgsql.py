import psycopg2
import logging
from Common import myLogger

class MyPgsql(object):
    # 连接数据库
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host="172.16.129.79",user="postgres",password="postgres",port="5432",database="empi_2")
            logging.info("数据库连接成功！")
        except Exception as e:
            logging.info("数据库连接失败：%s",e)
            raise e
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()



    # sql执行
    def excute_sql(self,sql):
        try:
            self.cursor.execute(sql)
            logging.info("sql查询成功！")
            # print(self.cursor.fetchall())
            return self.cursor.fetchall()
        except:
            self.conn.rollback()


    # 关闭数据库
    def close_pgsql(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库
        self.conn.close()
        logging.info("关闭数据库成功！")

def main():
    sql = "select euid from  patient where id='26882' limit 1;"
    mypgsql =MyPgsql()
    mypgsql.excute_sql(sql)





if __name__ == '__main__':
    main()