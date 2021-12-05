from util import  Load_data ,Send_to_all


data_list,content,ip,port=Load_data()

Send_to_all(data_list,ip,port,content)


