import json
import time
from TugasAkhir.Dinas.StagingDetail_function import staggingTransform

def identifikasiIndexData(con_database,cur_database,filename,index):
    cur_database.execute("select nama_file, index_file from tb_data where nama_file='%s'" % (filename))
    indexAcuan = cur_database.fetchone()

    if indexAcuan is None:
        print("+++Data Belum Terdaftar")
        cur_database.execute("insert into tb_data values(null,'default','%s','%s')" % (filename,index))
        con_database.commit()

        time.sleep(2)
        print("+++Index Baru Berhasil Dimasukkan")

    elif indexAcuan is not None:
        print("+++Data Sudah Terdaftar")

        for loopIndex in indexAcuan[1].split(' '):

            if loopIndex == index:
                print("+++Data Sudah Memiliki Index Tersebut")
                break
        if loopIndex != index:
            cur_database.execute("select index_file from tb_data where nama_file='%s'" % (filename))
            acuanIndex = cur_database.fetchone()

            print("+++Data Belum Memiliki Index Tersebut")
            cur_database.execute("update tb_data set index_file='%s' where nama_file='%s'" % (acuanIndex[0]+ " " +index, filename))
            con_database.commit()
            time.sleep(2)
            print("+++Index Baru Berhasil Dimasukkan")

def transformDanMappingData(con_database,cur_database,filename,locateFile):
    cur_database.execute("select index_file from tb_data where nama_file='%s'" % (filename))
    indexF = cur_database.fetchone()
    indexFile = indexF[0].split(' ')[1:][:2]

    for column in indexFile:
        cur_database.execute("select * from tb_det_category")
        det_category = cur_database.fetchall()
        cur_database.execute("select * from tb_mapping_det_category")
        det_categoryMapping = cur_database.fetchall()

        cur_database.execute("select * from tb_det_list_category")
        det_list_category = cur_database.fetchall()
        cur_database.execute("select * from tb_mapping_det_list_category")
        det_list_categoryMapping = cur_database.fetchall()

        cur_database.execute("select * from tb_category_shu")
        shu_category = cur_database.fetchall()
        cur_database.execute("select * from tb_mapping_category_shu")
        shu_categoryMapping = cur_database.fetchall()

        with open(locateFile, "r+") as jsonFile:
            filejson = json.load(jsonFile)
            for split in filejson:
                splitJson = split[column].split(' ')
                splitid = split[indexF[0].split(' ')[0]]  # pengambilan index ID dari tb_data sebagai penyimpan index file entry

                splitid = staggingTransform(con_database,cur_database,column,split,splitJson,splitid,det_category,det_categoryMapping,
                                                 det_list_category,det_list_categoryMapping,shu_category,shu_categoryMapping)

def importDataToDatabase(con_database,cur_database,column,category,split):
    for categoryL in category:
        cur_database.execute("select id_det_category,category from tb_det_category where id_category='%s'" %
                             (categoryL[0]))
        detail = cur_database.fetchall()

        # input tb_modal dan tb_kasdanbank
        for detCat in detail:
            cur_database.execute("select category_in_file_det from tb_mapping_det_category where category ='%s'" %
                                 (detCat[1]))
            catfile1 = cur_database.fetchall()  # apabila 1 det category memiliki lebih dari 1 mapping data

            for catfile in catfile1:
                if catfile[0] == split[column]:
                    cur_database.execute("select nama_modal from tb_modal where nama_modal='%s'" %
                                         (detCat[1]))
                    validCategory = cur_database.fetchone()

                    cur_database.execute("select jenis_kas from tb_kasdanbank where jenis_kas='%s'" %
                                         (detCat[1]))
                    validCategory1 = cur_database.fetchone()

                    if validCategory is None and categoryL[1] == 'modal':
                        print("+++++++++++INPUT PADA MODAL++++++++++++")
                        print("+++++++++INPUT CATEGORY MODAL:", detCat[1])
                        cur_database.execute("insert into tb_modal values (null,1,'%s',null)" %
                                             (detCat[1]))
                        con_database.commit()
                        print("Category Telah di-input-kan kedalam tabel Modal")
                        pass

                    elif validCategory1 is None and categoryL[1] == 'kas':
                        print("+++INPUT CATEGORY KAS DAN BANK:", detCat[1])
                        print("++++++++INPUT PADA KAS DAN BANK++++++++")
                        cur_database.execute("insert into tb_kasdanbank values (null,1,'%s',null)" %
                                             (detCat[1]))
                        con_database.commit()
                        print("Category Telah di-input-kan kedalam tabel Kas dan Bank")
                        pass

                    elif validCategory is not None or validCategory1 is not None:
                        print("Category Sudah Tercatat pada Database")
                        pass

            # input tb_detail_modal dan tb_detail_kas
            cur_database.execute("select id_det_list_category, list_name_category from tb_det_list_category where id_det_category='%s'" %
                                 (detCat[0]))
            detailis = cur_database.fetchall()

            for detailList in detailis:
                cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where list_name_category = '%s'" %
                                     (detailList[1]))
                listFile1 = cur_database.fetchall()  # apabila 1 det_list_category memiliki lebih dari 1 mapping data

                for listFile in listFile1:
                    if listFile[0] == split[column]:
                        cur_database.execute("select jenis_detail_modal from tb_detail_modal where jenis_detail_modal='%s'" %
                                             (detailList[1]))
                        validCategory = cur_database.fetchone()

                        cur_database.execute("select jenis_detail_kas from tb_detail_kas where jenis_detail_kas='%s'" %
                                             (detailList[1]))
                        validCategory1 = cur_database.fetchone()

                        if validCategory is None and categoryL[1] == 'modal':
                            cur_database.execute("select id_modal from tb_modal where nama_modal = '%s'" %
                                                 (detCat[1]))
                            id_modal = cur_database.fetchone()[0]
                            print("+++++++++++INPUT PADA MODAL++++++++++++")
                            print("+++++++++INPUT CATEGORY MODAL:", detailList[1])
                            cur_database.execute("insert into tb_detail_modal values (null,'%s','%s',null)" %
                                                 (id_modal, detailList[1]))
                            con_database.commit()
                            print("Category Telah di-input-kan kedalam tabel Detail Modal")
                            time.sleep(1)
                            pass

                        elif validCategory1 is None and categoryL[1] == 'kas':
                            cur_database.execute("select id_kas from tb_kasdanbank where jenis_kas = '%s'" %
                                                 (detCat[1]))
                            id_kas = cur_database.fetchone()[0]
                            print("+++INPUT CATEGORY KAS DAN BANK:", detailList[1])
                            print("++++++++INPUT PADA KAS DAN BANK++++++++")
                            cur_database.execute("insert into tb_detail_kas values (null,'%s','%s',null)" %
                                                 (id_kas, detailList[1]))
                            con_database.commit()
                            print("Category Telah di-input-kan kedalam tabel Detail Kas")
                            time.sleep(1)
                            pass

                        elif validCategory is not None or validCategory1 is not None:
                            print("Category Detail Sudah Tercatat pada Database")
                            pass

                # input tb_shu dan hitung all jumlah pada modal dan kas
                cur_database.execute("select category_jenis_perhitungan from tb_category_shu where id_det_list_category = '%s'" %
                                     (detailList[0]))
                shu_cat = cur_database.fetchall()

                for cat_shu in shu_cat:
                    cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_jenis_perhitungan = '%s'" %
                                         (cat_shu))
                    shu_file1 = cur_database.fetchall()  # apabila 1 category shu memiliki lebih dari 1 mapping data

                    for shu_file in shu_file1:
                        if shu_file[0] == split[column]:
                            cur_database.execute("select jenis_perhitungan from tb_shu where jenis_perhitungan='%s'" %
                                                 (cat_shu))
                            validCategory = cur_database.fetchone()

                            cur_database.execute("select id_detail_modal from tb_detail_modal where jenis_detail_modal = '%s'" %
                                                 (detailList[1]))
                            id_det_lis = cur_database.fetchone()[0]

                            if validCategory is None:
                                print("+++INPUT CATEGORY SHU:", cat_shu)
                                print("++++++++INPUT PADA SHU++++++++")
                                cur_database.execute( "insert into tb_shu values (null,'%s','%s',null)" %
                                                      (id_det_lis, cat_shu[0]))
                                con_database.commit()
                                print("Category Telah di-input-kan kedalam tabel SHU")
                                # sum jumlah
                                pass

                            elif validCategory is not None:
                                print("Category SHU Sudah Tercatat pada Database")
                                pass


