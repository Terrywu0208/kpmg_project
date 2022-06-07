# 資料庫串接
import MySQLdb
import pandas as pd
import re
import pandas as pd

# 資產負債表
流動資產合計 = {"流動資產合計":"現金及約當現金+透過損益按公允價值衡量之金融資產－流動+按攤銷後成本衡量之金融資產－流動+應收票據淨額+應收帳款淨額+應收帳款－關係人淨額+其他應收款+其他應收款－關係人+本期所得稅資產+存貨+預付款項+其他流動資產+其他金融資產－流動+其他流動資產－其他"}

非流動資產合計 = {"非流動資產合計":"透過其他綜合損益按公允價值衡量之金融資產－非流動 +按攤銷後成本衡量之金融資產－非流動 +採用權益法之投資+不動產、廠房及設備+使用權資產+投資性不動產淨額+無形資產+遞延所得稅資產+其他非流動資產+預付設備款+其他非流動資產－其他"}

資產總計 = {"資產總計":"流動資產合計+非流動資產合計"}

流動負債合計 = {"流動負債合計":"短期借款+應付短期票券+合約負債－流動+應付票據+應付帳款+其他應付款+其他應付款項－關係人+本期所得稅負債+租賃負債－流動+其他流動負債+其他流動負債－其他"}

非流動負債合計 = {"非流動負債合計":"合約負債－非流動 +應付公司債 +長期借款  +負債準備－非流動+遞延所得稅負債+租賃負債－非流動+其他非流動負債+淨確定福利負債-非流動+存入保證金"}

負債總計 = {"負債總計":"流動負債合計+非流動負債合計"}

股本合計 = {"股本合計":"普通股股本"}

資本公積合計 = {"資本公積合計":"資本公積－發行溢價 +資本公積－認股權"}


保留盈餘合計 = {"保留盈餘合計":"法定盈餘公積+特別盈餘公積+未分配盈餘（或待彌補虧損）"}

歸屬於母公司業主之權益合計 = {"歸屬於母公司業主之權益合計":"股本合計+資本公積合計+保留盈餘合計+其他權益合計+庫藏股票"}

權益總額 = {"權益總計":"歸屬於母公司業主之權益合計+非控制權益"}

負債及權益總計 = {"負債及權益總計":"負債總計+權益總計"}
# 資產負債表

# 綜合損益表
營業毛利_毛損 = {"營業毛利（毛損）":"營業收入合計-營業成本合計"}

營業毛利_毛損_淨額 = {"營業毛利（毛損）淨額":"營業毛利（毛損）"}

營業費用合計 = {"營業費用合計":"推銷費用+管理費用+研究發展費用+預期信用減損損失(利益)"}

營業利益_損失 = {"營業利益（損失）":"營業毛利（毛損）-營業費用合計+其他收益及費損淨額"}

營業外收入及支出合計 = {"營業外收入及支出合計":"利息收入合計+其他收入合計+其他利益及損失淨額-財務成本淨額+採用權益法認列之關聯企業及合資損益之份額淨額"} 

繼續營業單位稅前淨利_淨損 = {"繼續營業單位稅前淨利（淨損）":"營業利益（損失）+營業外收入及支出合計"}

繼續營業單位本期淨利_淨損 = {"繼續營業單位本期淨利（淨損）":"繼續營業單位稅前淨利（淨損）-所得稅費用（利益）合計"}

本期淨利_淨損 = {"本期淨利（淨損）":"繼續營業單位本期淨利（淨損）"}

不重分類至損益之項目總額 = {"不重分類至損益之項目總額":"確定福利計畫之再衡量數+透過其他綜合損益按公允價值衡量之權益工具投資未實現評價損益+採用權益法認列之關聯企業及合資之其他綜合損益之份額-不重分類至損益之項目-與不重分類之項目相關之所得稅"}

其他綜合損益_淨額 = {"其他綜合損益（淨額）":"不重分類至損益之項目總額"} 

後續可能重分類至損益之項目總額 = {"後續可能重分類至損益之項目總額":"國外營運機構財務報表換算之兌換差額-與可能重分類之項目相關之所得稅"}

其他綜合損益_淨額_1 = {"其他綜合損益（淨額）":"不重分類至損益之項目總額+後續可能重分類至損益之項目總額"}

本期綜合損益總額 = {"本期綜合損益總額":"本期淨利（淨損）+其他綜合損益（淨額）"}

本期淨利_淨損_1 = {"本期淨利（淨損）":"母公司業主（淨利／損）+非控制權益（淨利／損）"}

綜合損益總額歸屬於 = {"綜合損益總額歸屬於":"母公司業主（綜合損益）+非控制權益（綜合損益）"}
# 綜合損益表

# 現金流量表
本期稅前淨利_淨損 = {"本期稅前淨利（淨損）":"繼續營業單位稅前淨利（淨損）"}

收益費損項目合計 = {"收益費損項目合計":"折舊費用+攤銷費用+利息費用+預期信用減損損失（利益）數／呆帳費用提列（轉列收入）數+透過損益按公允價值衡量金融資產及負債之淨損失（利益）+利息費用+利息收入+股份基礎給付酬勞成本+採用權益法認列之關聯企業及合資損失（利益）之份額+處分及報廢不動產、廠房及設備損失（利益）+ 不動產、廠房及設備轉列費用數+處分投資性不動產損失（利益）+處分其他資產損失（利益）+處分採用權益法之投資損失（利益）+非金融資產減損損失+非金融資產減損迴轉利益+逾期未領董監酬勞轉列其他收入+其他項目"}

與營業活動相關之資產之淨變動合計 = {"與營業活動相關之資產之淨變動合計":"強制透過損益按公允價值衡量之金融資產（增加）減少+應收票據（增加）減少+應收帳款（增加）減少+ 應收帳款－關係人（增加）減少+ 其他應收款（增加）減少 + 其他應收款－關係人（增加）減少 +存貨（增加）減少+ 預付費用（增加）減少 +預付款項（增加）減少+其他流動資產（增加）減少+ 其他營業資產（增加）減少"}

與營業活動相關之負債之淨變動合計 = {"與營業活動相關之負債之淨變動合計":"合約負債增加（減少）+應付票據增加（減少）+應付帳款增加（減少）+應付帳款－關係人增加（減少）+其他應付款增加（減少）+其他應付款－關係人增加（減少）+其他流動負債增加（減少）+淨確定福利負債增加(減少)+ 其他營業負債增加（減少）"}

與營業活動相關之資產及負債之淨變動合計 = {"與營業活動相關之資產及負債之淨變動合計":"與營業活動相關之資產之淨變動合計+與營業活動相關之負債之淨變動合計"}

調整項目合計 = {"調整項目合計":"收益費損項目合計+與營業活動相關之資產及負債之淨變動合計"}

與營業活動相關之負債之淨變動合計 = {"與營業活動相關之負債之淨變動合計":"合約負債增加（減少）+應付票據增加（減少）+應付帳款增加（減少）+其他應付款增加（減少）+其他流動負債增加（減少）+淨確定福利負債增加(減少)+其他營業負債增加（減少）"}

與營業活動相關之資產及負債之淨變動合計 = {"與營業活動相關之資產及負債之淨變動合計":"與營業活動相關之資產之淨變動合計 +與營業活動相關之負債之淨變動合計"}

營運產生之現金流入_流出 = {"營運產生之現金流入（流出）":"本期稅前淨利（淨損）+調整項目合計"}

營業活動之淨現金流入_流出 = {"營業活動之淨現金流入（流出）":"營運產生之現金流入（流出）+收取之利息 +收取之股利  +支付之利息+退還（支付）之所得稅"}

投資活動之淨現金流入_流出 = {"投資活動之淨現金流入（流出）":"處分透過其他綜合損益按公允價值衡量之金融資產 + 取得按攤銷後成本衡量之金融資產+ 取得採用權益法之投資 +處分按攤銷後成本衡量之金融資產+處分採用權益法之投資+預付投資款增加+處分子公司 +取得不動產、廠房及設備+處分不動產、廠房及設備+存出保證金增加+存出保證金減少 +取得無形資產+取得使用權資產+處分投資性不動產  +其他金融資產增加+其他非流動資產減少 +預付設備款增加+收取之利息+其他投資活動"}

籌資活動之淨現金流入_流出 = {"籌資活動之淨現金流入（流出）":"短期借款增加+ 短期借款減少 +存入保證金增加+租賃本金償還+發放現金股利+ 應付短期票券增加+ 應付短期票券減少 + 舉借長期借款 +員工購買庫藏股+ 存入保證金增加 +存入保證金減少 +租賃本金償還 + 發放現金股利  +取得子公司股權+非控制權益變動"}

本期現金及約當現金增加_減少數 = {"本期現金及約當現金增加（減少）數":"營業活動之淨現金流入（流出）+ 投資活動之淨現金流入（流出）+ 籌資活動之淨現金流入（流出）+匯率變動對現金及約當現金之影響"}

# 期末現金及約當現金餘額=期初現金及約當現金餘額=)=資產負債表帳列之現金及約當現金

期末現金及約當現金餘額 = {"期末現金及約當現金餘額":"本期現金及約當現金增加（減少）數+期初現金及約當現金餘額"}
# 現金流量表

Balance_Sheet_all_function = [流動資產合計,非流動資產合計,資產總計,流動負債合計,非流動負債合計,負債總計,股本合計,資本公積合計,保留盈餘合計,歸屬於母公司業主之權益合計,權益總額,負債及權益總計]
Profit_and_Loss_Account_all_function = [營業毛利_毛損,營業毛利_毛損_淨額,營業費用合計,營業利益_損失,營業外收入及支出合計,繼續營業單位稅前淨利_淨損,繼續營業單位本期淨利_淨損,本期淨利_淨損,不重分類至損益之項目總額,其他綜合損益_淨額,後續可能重分類至損益之項目總額,其他綜合損益_淨額_1,本期綜合損益總額,本期淨利_淨損_1,綜合損益總額歸屬於]
Cash_Flow_Statement_all_function = [本期稅前淨利_淨損,收益費損項目合計,與營業活動相關之資產之淨變動合計,與營業活動相關之負債之淨變動合計,與營業活動相關之資產及負債之淨變動合計,調整項目合計,與營業活動相關之負債之淨變動合計,與營業活動相關之資產及負債之淨變動合計,營運產生之現金流入_流出,營業活動之淨現金流入_流出,投資活動之淨現金流入_流出,籌資活動之淨現金流入_流出,本期現金及約當現金增加_減少數,期末現金及約當現金餘額]
negative_ls = ["營業費用合計","財務成本淨額","所得稅費用（利益）合計","不重分類至損益之項目","與不重分類之項目相關之所得稅"]
kind_function_dict = {"Balance_Sheet": Balance_Sheet_all_function,"Profit_and_Loss_Account":Profit_and_Loss_Account_all_function,"Cash_Flow_Statement":Cash_Flow_Statement_all_function}
new_dict = {}
kind_list = []
money_list = []
status_list = []


def main_calculate(df,kind_input):
    for f in kind_function_dict[kind_input]:
        for k ,v in f.items():
            temp_sum = 0    
            temp_ls = re.split(r"-|\+",v)
            for i in temp_ls:
                filt = (df["會計項目Accounting Title"].str.contains(i))
                x = df.loc[filt]
                # print(i)
                if x.empty:
                    continue
                else:
                    # try:
                    temp_num = x.iloc[0,[3]][0]
                    if "(" in str(temp_num):
                        temp_num = temp_num.replace("(","")
                        temp_num = temp_num.replace(")","")
                        temp_num = temp_num.replace(",","")
                        temp_num = -(int(temp_num))
                        if i in negative_ls:
                            temp_num = -(temp_num)
                            temp_sum+=temp_num
                        else:
                            temp_sum+=temp_num
                    elif pd.isna(temp_num):
                        continue
                    elif type(temp_num) == float:
                        temp_sum += temp_num
                    elif i in negative_ls:
                        temp_num = -(int(temp_num))
                        temp_sum+=temp_num
                    elif "成本" in i:
                        temp_num = -(int(temp_num))
                        temp_sum+=temp_num
                    else:
                        temp_num = int(temp_num)
                        temp_sum += temp_num 
            try:
                k_filt = (df["會計項目Accounting Title"].str.contains(k))
                k_x = df.loc[k_filt]
                k_num = k_x.iloc[0,[3]][0]
                if "(" in k_num:
                    k_num = k_num.replace("(","")
                    k_num = k_num.replace(")","")
                    k_num = k_num.replace(",","")
                    k_num = -(int(k_num))
                else:
                    k_num = int(k_num)

                if k_num == temp_sum:
                    kind_list.append(k)
                    money_list.append(k_num)
                    status_list.append("True")
                else:
                    kind_list.append(k)
                    money_list.append(k_num)
                    status_list.append("False")


                new_dict["會科"]=kind_list
                new_dict["金額"]=money_list
                new_dict["符合"]=status_list
            except:
                pass

    n_df = pd.DataFrame(new_dict)
    return n_df

def connect_mysql(company_id_input,kind_input,year_input,season_input):
    conn = MySQLdb.Connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       db = 'kpmg',
                       charset='utf8')
    # 輸入你的資料庫連線資訊
    cur = conn.cursor()

    company_id_input = 2707
    # kind_input = "Balance_Sheet" #你要查的表
    # kind_input = "Profit_and_Loss_Account" #你要查的表
    kind_input = "Cash_Flow_Statement" #你要查的表


    year_input = 2019
    season_input = 4
    cur.execute(f"SELECT `path` FROM `financial_statements` WHERE `company_id` = {company_id_input} AND `kind` = '{kind_input}' AND `year` = {year_input} AND `season` = {season_input} ")
    result_set = cur.fetchall()
    # result_set
    df = pd.read_csv(f"../../{result_set[0][0]}")
    new_df = main_calculate(df,kind_input)
    return new_df


final_result = connect_mysql(2707,"Cash_Flow_Statement",2019,4)
