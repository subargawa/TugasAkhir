import time
def staggingTransform(con_database,cur_database,column,split,splitJson,splitid,det_category,det_categoryMapping,
                      det_list_category,det_list_categoryMapping,shu_category,shu_categoryMapping):

    splitIdJson=splitid
    # Transform pada Detail Category
    for detCat in det_category:
        detail = detCat[2].split(' ')

        if len(detail) == 1 and len(splitJson) == 1:
            if detCat[2] == split[column] or detCat[2].upper() == split[column].upper():
                cur_database.execute("select id_det_category from tb_det_category where category ='%s'" %
                                     (detCat[2]))
                id_det_cat = cur_database.fetchone()[0]

                print("==================Transform Detail Category=================")
                print("ini data json", split[column])
                print("ini data category", detCat[2])

                if det_categoryMapping is None:
                    cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                         (id_det_cat, splitIdJson, detCat[2], split[column]))

                    con_database.commit()
                    print("insert to maapping")
                    pass

                elif det_categoryMapping is not None:
                    cur_database.execute("select category_in_file_det from tb_mapping_det_category where category_in_file_det='%s'" %
                                         (split[column]))
                    validJsonCategory = cur_database.fetchone()

                    if validJsonCategory is None or validJsonCategory[0] != split[column]:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Belum Terdaftar pada Database")
                        cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                             (id_det_cat, splitIdJson, detCat[2], split[column]))
                        con_database.commit()
                        print("insert to maapping")
                        pass

                    elif validJsonCategory is not None and validJsonCategory[0] == split[column] or validJsonCategory[0] == split[column]:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Sudah Terdaftar pada Database")
                        pass

            else:
                print("Field Tidak Cocok")
                pass

        elif len(detail) > 1 and len(splitJson) == 1:
            for detCatLoopa, detCatLoopb in zip(detail[0::1], detail[1::1]):
                detailCat = detCatLoopa + detCatLoopb

                if detCatLoopa == split[column] or detCatLoopb == split[column] or detCatLoopa.upper() == split[
                    column].upper() or detCatLoopb.upper() == split[column].upper():
                    cur_database.execute("select id_det_category from tb_det_category where category ='%s'" %
                                         (detCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    print("==================Transform Detail Category=================")
                    print("ini data json", split[column])
                    print("ini data category", detailCat)

                    if det_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas :"))
                        if menuPilih == 1:
                            print(detCat[3])


                        elif menuPilih == 2:
                            print("AHSHDAHSDA", id_det_cat, splitIdJson, detCat, split[column])
                            cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif det_categoryMapping is not None:
                        cur_database.execute("select category_in_file_det from tb_mapping_det_category where category_in_file_det='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        cur_database.execute("select category from tb_mapping_det_category where category='%s'" %
                                             (detCat[2]))
                        validDetList = cur_database.fetchone()

                        if validDetList is None or validDetList[0] != detCat[2]:

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                                print("=====[2] Masukkan Field Kedalam Database================")
                                print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                                menuPilih = int(input("Pilih Menu Diatas :"))
                                if menuPilih == 1:
                                    print(detCat[3])

                                elif menuPilih == 2:
                                    print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                    print("Object Json Belum Terdaftar pada Database")
                                    cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                         (id_det_cat, splitIdJson, detCat[2], split[column]))
                                    con_database.commit()
                                    print("insert to maapping")
                                    pass

                                elif menuPilih == 3:
                                    # pass karena value json dan value database tidak sesuai
                                    pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

                        elif validDetList is None and validDetList[0] == detCat[2] or validDetList[0] == detCat[2]:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(detail) == 1 and len(splitJson) > 1:
            for dataFile1, dataFile2 in zip(splitJson[0::1], splitJson[1::1]):
                dataFileKedua = dataFile1 + dataFile2

                if detCat[2] == dataFile1 or detCat[2] == dataFile2 or detCat[2].upper() == dataFile1.upper() \
                        or detCat[2].upper() == dataFile2.upper():
                    cur_database.execute("select id_det_category from tb_det_category where category ='%s'" %
                                         (detCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    print("==================Transform Detail Category=================")
                    print("ini data json", dataFileKedua)
                    print("ini data category", detCat[2])

                    if det_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas1 :"))
                        if menuPilih == 1:
                            print(detCat[3])


                        elif menuPilih == 2:
                            cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif det_categoryMapping is not None:
                        cur_database.execute("select category_in_file_det from tb_mapping_det_category where category_in_file_det='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        if validJsonCategory is None or validJsonCategory[0] != split[column]:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(detCat[3])

                            elif menuPilih == 2:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                or validJsonCategory[0] == split[column]:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(detail) > 1 and len(splitJson) > 1:
            for detCatLoopa, detCatLoopb in zip(detail[0::1], detail[1::1]):
                detailCat = detCatLoopa + detCatLoopb

                for dataFile1, dataFile2 in zip(splitJson[0::1], splitJson[1::1]):
                    dataFileKedua = dataFile1 + dataFile2

                    cur_database.execute("select id_det_category from tb_det_category where category ='%s'" %
                                         (detCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    if dataFileKedua == detailCat or dataFileKedua.upper() == detailCat.upper():
                        print("==============Transform Detail Category===============")
                        print("ini data json", dataFileKedua)
                        print("ini data cat", detailCat)

                        if det_categoryMapping is None:
                            cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif det_categoryMapping is not None:
                            cur_database.execute("select category_in_file_det from tb_mapping_det_category where category_in_file_det='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

                    elif dataFile1 == detCatLoopa or dataFile1 == detCatLoopb or dataFile2 == detCatLoopa or dataFile2 == detCatLoopb or dataFile1.upper() == detCatLoopa.upper() or dataFile1.upper() == detCatLoopb.upper() or dataFile2.upper() == detCatLoopa.upper() or dataFile2.upper() == detCatLoopb.upper():
                        print("==============Transform Detail Category===============")
                        print("ini data json", dataFileKedua)
                        print("ini data cat", detailCat)

                        if det_categoryMapping is None:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(detCat[3])

                            elif menuPilih == 2:
                                cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif det_categoryMapping is not None:
                            cur_database.execute("select category_in_file_det from tb_mapping_det_category where category_in_file_det='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                                print("=====[2] Masukkan Field Kedalam Database================")
                                print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                                menuPilih = int(input("Pilih Menu Diatas :"))
                                if menuPilih == 1:
                                    print(detCat[3])

                                elif menuPilih == 2:
                                    print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                    print("Object Json Belum Terdaftar pada Database")
                                    cur_database.execute("insert into tb_mapping_det_category values(null,'%s','%s','%s','%s')" %
                                                         (id_det_cat, splitIdJson, detCat[2], split[column]))
                                    con_database.commit()
                                    print("insert to maapping")
                                    pass

                                elif menuPilih == 3:
                                    # pass karena value json dan value database tidak sesuai
                                    pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

    # Transform pada Detail List Category
    for detListCat in det_list_category:
        detailis = detListCat[2].split(' ')

        if len(detailis) == 1 and len(splitJson) == 1:
            if detListCat[2] == split[column] or detListCat[2].upper() == split[column].upper():
                cur_database.execute("select id_det_list_category from tb_det_list_category where list_name_category ='%s'" %
                                     (detListCat[2]))
                id_det_cat = cur_database.fetchone()[0]

                print("==================Transform Detail List Category=================")
                print("ini data json", split[column])
                print("ini data category", detListCat[2])

                if det_list_categoryMapping is None:
                    cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                         (id_det_cat, splitIdJson, detListCat[2], split[column]))
                    con_database.commit()
                    print("insert to maapping")
                    pass

                elif det_list_categoryMapping is not None:
                    cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where category_in_file_det_list ='%s'" %
                                         (split[column]))
                    validJsonCategory = cur_database.fetchone()

                    cur_database.execute("select list_name_category from tb_mapping_det_list_category where list_name_category='%s'" %
                                         (detListCat[2]))
                    validSHU = cur_database.fetchone()

                    if validJsonCategory is None or validJsonCategory[0] != split[column]:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Belum Terdaftar pada Database")
                        cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                             (id_det_cat, splitIdJson, detListCat[2], split[column]))
                        con_database.commit()
                        print("insert to maapping")
                        pass

                    elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                            or validJsonCategory[0] == split[column] or validSHU is not None:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Sudah Terdaftar pada Database")
                        pass
            else:
                print("Field Tidak Cocok")
                pass

        elif len(detailis) > 1 and len(splitJson) == 1:
            for detList1, detList2 in zip(detailis[0::1], detailis[1::1]):
                detailList = detList1 + detList2

                if detList1 == split[column] or detList2 == split[column] or detList1.upper() == split[
                    column].upper() or detList2.upper() == split[column].upper():
                    cur_database.execute("select id_det_list_category from tb_det_list_category where list_name_category ='%s'" %
                                         (detListCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    print("==================Transform Detail List Category=================")
                    print("ini data json", split[column])
                    print("ini data category", detailList)

                    if det_list_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas :"))
                        if menuPilih == 1:
                            print(detListCat[3])

                        elif menuPilih == 2:
                            cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detListCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif det_list_categoryMapping is not None:
                        cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where category_in_file_det_list ='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        cur_database.execute("select list_name_category from tb_mapping_det_list_category where list_name_category='%s'" %
                                             (detListCat[2]))
                        validSHU = cur_database.fetchone()

                        if validJsonCategory is None or validJsonCategory[0] != split[column]:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(detListCat[3])

                            elif menuPilih == 2:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detListCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                or validJsonCategory[0] == split[column] or validSHU is not None:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(detailis) == 1 and len(splitJson) > 1:
            for dataFile3, dataFile4 in zip(splitJson[0::1], splitJson[1::1]):
                dataFileKetiga = dataFile3 + dataFile4

                if detListCat[2] == dataFile3 or detListCat[2] == dataFile4 or detListCat[2].upper() == dataFile3 \
                        or detListCat[2].upper() == dataFile4.upper():
                    cur_database.execute("select id_det_list_category from tb_det_list_category where list_name_category ='%s'" %
                                         (detListCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    print("==================Transform Detail List Category=================")
                    print("ini data json", dataFileKetiga)
                    print("ini data category", detListCat[2])

                    if det_list_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas :"))
                        if menuPilih == 1:
                            print(detListCat[3])

                        elif menuPilih == 2:
                            cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detListCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif det_list_categoryMapping is not None:
                        cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where category_in_file_det_list ='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        cur_database.execute("select list_name_category from tb_mapping_det_list_category where list_name_category='%s'" %
                                             (detListCat[2]))
                        validSHU = cur_database.fetchone()

                        if validSHU is None or validSHU[0] != detListCat[2]:
                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                                print("=====[2] Masukkan Field Kedalam Database================")
                                print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                                menuPilih = int(input("Pilih Menu Diatas :"))
                                if menuPilih == 1:
                                    print(detListCat[3])

                                elif menuPilih == 2:
                                    print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                    print("Object Json Belum Terdaftar pada Database")
                                    cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                         (id_det_cat, splitIdJson, detListCat[2], split[column]))
                                    con_database.commit()
                                    print("insert to maapping")
                                    pass

                                elif menuPilih == 3:
                                    # pass karena value json dan value database tidak sesuai
                                    pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

                        elif validSHU is None and validSHU[0] == detListCat[2] or validSHU[0] == detListCat[2]:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(detailis) > 1 and len(splitJson) > 1:
            for detList1, detList2 in zip(detailis[0::1], detailis[1::1]):
                detailList = detList1 + detList2

                for dataFile3, dataFile4 in zip(splitJson[0::1], splitJson[1::1]):
                    dataFileKetiga = dataFile3 + dataFile4

                    cur_database.execute("select id_det_list_category from tb_det_list_category where list_name_category ='%s'" %
                                         (detListCat[2]))
                    id_det_cat = cur_database.fetchone()[0]

                    if dataFileKetiga == detailList or dataFileKetiga.upper() == detailList.upper():
                        print("==============Transform Detail List Category===============")
                        print("ini data json", dataFileKetiga)
                        print("ini data category", detailList)

                        if det_list_categoryMapping is None:
                            cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                 (id_det_cat, splitIdJson, detListCat[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif det_list_categoryMapping is not None:
                            cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where category_in_file_det_list ='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            cur_database.execute("select list_name_category from tb_mapping_det_list_category where list_name_category='%s'" %
                                                 (detListCat[2]))
                            validSHU = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detListCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column] or validSHU is not None:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass


                    elif dataFile3 == detList1 or dataFile3 == detList2 or dataFile4 == detList1 \
                            or dataFile4 == detList2 or dataFile3.upper() == detList1.upper() or dataFile3.upper() == detList2.upper() \
                            or dataFile4.upper() == detList1.upper() or dataFile4.upper() == detList2.upper():
                        print("==============Transform Detail Category===============")
                        print("ini data json", dataFileKetiga)
                        print("ini data cat", detailList)

                        if det_list_categoryMapping is None:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(detListCat[3])

                            elif menuPilih == 2:
                                cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                     (id_det_cat, splitIdJson, detListCat[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif det_list_categoryMapping is not None:
                            cur_database.execute("select category_in_file_det_list from tb_mapping_det_list_category where category_in_file_det_list ='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            cur_database.execute("select list_name_category from tb_mapping_det_list_category where list_name_category='%s'" %
                                                 (detListCat[2]))
                            validSHU = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                                print("=====[2] Masukkan Field Kedalam Database================")
                                print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                                menuPilih = int(input("Pilih Menu Diatas :"))
                                if menuPilih == 1:
                                    print(detListCat[3])

                                elif menuPilih == 2:
                                    print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                    print("Object Json Belum Terdaftar pada Database")
                                    cur_database.execute("insert into tb_mapping_det_list_category values(null,'%s','%s','%s','%s')" %
                                                         (id_det_cat, splitIdJson, detListCat[2], split[column]))
                                    con_database.commit()
                                    print("insert to maapping")
                                    pass

                                elif menuPilih == 3:
                                    # pass karena value json dan value database tidak sesuai
                                    pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column] or validSHU is not None:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

    # Transform pada SHU Category
    for shu in shu_category:
        shu_cat = shu[2].split(' ')

        if len(shu_cat) == 1 and len(splitJson) == 1:
            if shu[2] == split[column] or shu[2].upper() == split[column].upper():
                cur_database.execute("select id_category_shu from tb_category_shu where category_jenis_perhitungan ='%s'" %
                                     (shu[2]))
                id_det_shu = cur_database.fetchone()[0]

                print("==================Transform SHU Category=================")
                print("ini data json", split[column])
                print("ini data category", shu[2])

                if shu_categoryMapping is None:
                    cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                         (id_det_shu, splitIdJson, shu[2], split[column]))
                    con_database.commit()
                    print("insert to maapping")
                    pass

                elif shu_categoryMapping is not None:
                    cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_in_file_perhitungan ='%s'" %
                                         (split[column]))
                    validJsonCategory = cur_database.fetchone()

                    if validJsonCategory is None or validJsonCategory[0] != split[column]:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Belum Terdaftar pada Database")
                        cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                             (id_det_shu, splitIdJson, shu[2], split[column]))
                        con_database.commit()
                        print("insert to maapping")
                        pass

                    elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                            or validJsonCategory[0] == split[column]:
                        print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                        print("Object Json Sudah Terdaftar pada Database")
                        pass
            else:
                print("Field Tidak Cocok")
                pass

        elif len(shu_cat) > 1 and len(splitJson) == 1:
            for detSHU1, detSHU2 in zip(shu_cat[0::1], shu_cat[1::1]):
                cat_shu = detSHU1 + detSHU2

                if detSHU1 == split[column] or detSHU2 == split[column] or detSHU1 == split[column].upper() \
                        or detSHU2 == split[column].upper():
                    cur_database.execute("select id_category_shu from tb_category_shu where category_jenis_perhitungan ='%s'" %
                                         (shu[2]))
                    id_det_shu = cur_database.fetchone()[0]

                    print("==================Transform SHU Category=================")
                    print("ini data json", split[column])
                    print("ini data category", cat_shu)

                    if shu_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas :"))
                        if menuPilih == 1:
                            print(shu[3])

                        elif menuPilih == 2:
                            cur_database.execute( "insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                  (id_det_shu, splitIdJson, shu[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif shu_categoryMapping is not None:
                        cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_in_file_perhitungan ='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        if validJsonCategory is None or validJsonCategory[0] != split[column]:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(shu[3])

                            elif menuPilih == 2:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                     (id_det_shu, splitIdJson, shu[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                or validJsonCategory[0] == split[column]:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(shu_cat) == 1 and len(splitJson) > 1:
            for dataFile5, dataFile6 in zip(splitJson[0::1], splitJson[1::1]):
                dataFileKeempat = dataFile5 + dataFile6

                if shu[2] == dataFile5 or shu[2] == dataFile6 or shu[2].upper() == dataFile5.upper() or shu[
                    2].upper() == dataFile6.upper():
                    cur_database.execute("select id_category_shu from tb_category_shu where category_jenis_perhitungan ='%s'" %
                                         (shu[2]))
                    id_det_shu = cur_database.fetchone()[0]

                    print("==================Transform SHU Category=================")
                    print("ini data json", dataFileKeempat)
                    print("ini data category", shu[2])

                    if shu_categoryMapping is None:
                        print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                        print("=====[2] Masukkan Field Kedalam Database================")
                        print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                        menuPilih = int(input("Pilih Menu Diatas :"))
                        if menuPilih == 1:
                            print(shu[3])

                        elif menuPilih == 2:
                            cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                 (id_det_shu, splitIdJson, shu[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif menuPilih == 3:
                            # pass karena value json dan value database tidak sesuai
                            pass

                    elif shu_categoryMapping is not None:
                        cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_in_file_perhitungan ='%s'" %
                                             (split[column]))
                        validJsonCategory = cur_database.fetchone()

                        if validJsonCategory is None or validJsonCategory[0] != split[column]:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(shu[3])

                            elif menuPilih == 2:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                     (id_det_shu, splitIdJson, shu[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                or validJsonCategory[0] == split[column]:
                            print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                            print("Object Json Sudah Terdaftar pada Database")
                            pass

        elif len(shu_cat) > 1 and len(splitJson) > 1:
            for detSHU1, detSHU2 in zip(shu_cat[0::1], shu_cat[1::1]):
                cat_shu = detSHU1 + detSHU2

                for dataFile5, dataFile6 in zip(splitJson[0::1], splitJson[1::1]):
                    dataFileKeempat = dataFile5 + dataFile6

                    cur_database.execute("select id_category_shu from tb_category_shu where category_jenis_perhitungan ='%s'" %
                                         (shu[2]))
                    id_det_shu = cur_database.fetchone()[0]

                    if dataFileKeempat == cat_shu or dataFileKeempat.upper() == cat_shu.upper():
                        print("==================Transform SHU Category=================")
                        print("ini data json", dataFileKeempat)
                        print("ini data category", cat_shu)

                        if shu_categoryMapping is None:
                            cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                 (id_det_shu, splitIdJson, shu[2], split[column]))
                            con_database.commit()
                            print("insert to maapping")
                            pass

                        elif shu_categoryMapping is not None:
                            cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_in_file_perhitungan ='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Belum Terdaftar pada Database")
                                cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                     (id_det_shu, splitIdJson, shu[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass

                    elif dataFile5 == detSHU1 or dataFile5 == detSHU2 or dataFile6 == detSHU1 or dataFile6 == detSHU2 or dataFile5.upper() == detSHU1.upper() or dataFile5.upper() == detSHU2.upper() or dataFile6.upper() == detSHU1.upper() or dataFile6.upper() == detSHU2.upper():
                        print("==================Transform SHU Category=================")
                        print("ini data json", dataFileKeempat)
                        print("ini data category", cat_shu)

                        if shu_categoryMapping is None:
                            print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                            print("=====[2] Masukkan Field Kedalam Database================")
                            print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                            menuPilih = int(input("Pilih Menu Diatas :"))
                            if menuPilih == 1:
                                print(shu[3])

                            elif menuPilih == 2:
                                cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                     (id_det_shu, splitIdJson, shu[2], split[column]))
                                con_database.commit()
                                print("insert to maapping")
                                pass

                            elif menuPilih == 3:
                                # pass karena value json dan value database tidak sesuai
                                pass

                        elif shu_categoryMapping is not None:
                            cur_database.execute("select category_in_file_perhitungan from tb_mapping_category_shu where category_in_file_perhitungan ='%s'" %
                                                 (split[column]))
                            validJsonCategory = cur_database.fetchone()

                            if validJsonCategory is None or validJsonCategory[0] != split[column]:
                                print("=====[1] Lihat Deskripsi Field Category pada Dinas======")
                                print("=====[2] Masukkan Field Kedalam Database================")
                                print("=====[3] Tidak Input ke Database Karena Tidak Seusai====")
                                menuPilih = int(input("Pilih Menu Diatas :"))
                                if menuPilih == 1:
                                    print(shu[3])

                                elif menuPilih == 2:
                                    print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                    print("Object Json Belum Terdaftar pada Database")
                                    cur_database.execute("insert into tb_mapping_category_shu values(null,'%s','%s','%s','%s')" %
                                                         (id_det_shu, splitIdJson, shu[2], split[column]))
                                    con_database.commit()
                                    print("insert to maapping")
                                    pass

                                elif menuPilih == 3:
                                    # pass karena value json dan value database tidak sesuai
                                    pass

                            elif validJsonCategory is not None and validJsonCategory[0] == split[column] \
                                    or validJsonCategory[0] == split[column]:
                                print("Field Json dengan Value", splitIdJson, "dan", splitJson)
                                print("Object Json Sudah Terdaftar pada Database")
                                pass