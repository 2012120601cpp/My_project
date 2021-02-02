import psycopg2

class MyPgsql(object):
    def __init__(self):
        self.conn = psycopg2.connect(host="",user="",password="",port="",database="")
        self.cursor =self.conn.cursor()


    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def excute_sql(self,sql):
        self.cursor.excute(sql)

    def ask_question(self):
        sql = ""
        self.excute_sql(sql)


    def run(self):
        while True:
            num = input("请输入你想要查询的问题：")
            if num ==  "3":
                pass



def main(self):
    mypgsql =MyPgsql()
    mypgsql.run()



if __name__ == '__main__':
    main()