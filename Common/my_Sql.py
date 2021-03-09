class Allmysql:
    def all_sql(self):
        # 版本下需求总数
        sum_requirement = 'select count(*) from  mat_lib_accuracy_result_set mlars   where  text_type = 0;'

        # 开发提测需求数
        dev_complete_requirement = 'select count(*)  from mat_lib_accuracy_result_set mlars where project_id >90;'

        # 测试完成需求数
        test_complete_requirement = 'select count(*)  from mat_lib_corpus_tag_rel mlctr where corpus_id >598;'

        # bug总数37
        sum_bug = 'select count(*)  from mat_lib_corpus_tag_rel mlctr where corpus_id >598;'

        # 今日新增bug数
        new_bug = 2

        # 今日关闭bug数30
        close_bug = 'select count(*)  from mat_lib_corpus_tag_rel mlctr where corpus_id >599;'

        # 待解决bug数
        open_bug = 3

        # 优先级为高及以上bug数
        serious_bug = 1

        # 需求详情地址
        requirement_addr = 'https://redmine.synyi.com/projects/sck/issues?query_id=2554'

        # bug详情地址
        bug_addr = 'https://redmine.synyi.com/projects/sck/issues?query_id=2555'
        return sum_requirement,dev_complete_requirement,test_complete_requirement,sum_bug,\
               close_bug,new_bug,open_bug,serious_bug,requirement_addr,bug_addr
