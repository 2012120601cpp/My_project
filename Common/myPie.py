import matplotlib.pyplot as plotter
import matplotlib.pyplot as plt


def my_pie():
        from Common.my_Sql import Allmysql
        allmysql = Allmysql()
        allmysql.all_sql()
        # bug的所有状态
        bug_state = ['剩余待解决', '已解决', '重新打开']

        place_count = [11, 12, 5]
        # 展现bug的占比
        plt.figure(figsize=(10,5), dpi=100)
        # 防止中文乱码
        plotter.rcParams['font.sans-serif'] = ['SimHei']
        # 通过pie
        plt.pie(place_count, labels=bug_state, autopct='%1.1f%%')

        # 指定显示的pie是正圆
        plt.axis('equal')

        plt.legend(loc='best')

        plt.title("Bug占比示意图")
        plt.show()


if __name__ == '__main__':
        my_pie()
