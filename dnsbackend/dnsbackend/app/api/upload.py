from flask import jsonify, request
from . import api
import time
import xlrd
from .. import common
from werkzeug import secure_filename
from app.api.decorator import *
from app.auth.auth import Auth
import simplejson as json
from functools import wraps
from app.models import db
from app.models.normal_models import *
import csv

def session_commit():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        reason = str(e)
        # print(reason)
        return reason

# @api.route('/upload', methods=['POST'])
# def uploadFile():
#     dict_is_occupied = {1: '占用', 0: '空闲'}
#     dict_type = {0: '互联地址', 1: 'Loopback地址'}

#     dict_is_occupied_rev = {'占用': 1, '空闲': 0}
#     dict_type_rev = {'互联地址': 0, 'Loopback地址': 1}

#     city_list = ['广州', '深圳', '东莞', '佛山', '中山', '珠海', '江门', '肇庆', '汕头', '汕尾', '湛江', '揭阳',
#                  '韶关', '阳江', '梅州', '清远', '云浮', '茂名', '惠州', '潮州', '河源']

#     if 'multipart/form-data' in request.content_type:
#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             if filename.split('.')[-1] != 'xlsx':
#                 return jsonify(common.falseReturn('', '导入文件类型错误！'))
#             else:
#                 filename = '%s.xlsx' % str(int(time.time() * 10000000))
#                 fileFullPath = 'upload/' + filename
#                 file.save(fileFullPath)

#                 try:
#                     workbook = xlrd.open_workbook(fileFullPath)
#                     booksheet = workbook.sheet_by_name('Sheet1')
#                     if booksheet.row(0)[0].value != '地市' or booksheet.row(0)[1].value != 'IP' \
#                             or booksheet.row(0)[2].value != '是否占用' or booksheet.row(0)[3].value != '地址类型':
#                         return jsonify(common.falseReturn('', '文件格式不正确！'))
#                     else:
#                         tmpList = []
#                         for row in range(1, booksheet.nrows):
#                             tmpData = {}
#                             if booksheet.row(row)[0].value in city_list:
#                                 tmpData['city'] = booksheet.row(row)[0].value
#                             else:
#                                 raise Exception

#                             tmpData['ipAddress'] = booksheet.row(row)[1].value

#                             if booksheet.row(row)[2].value in dict_is_occupied_rev.keys():
#                                 tmpData['isOccupied'] = dict_is_occupied_rev[booksheet.row(row)[2].value]
#                             else:
#                                 raise Exception

#                             if booksheet.row(row)[3].value in dict_type_rev.keys():
#                                 tmpData['type'] = dict_type_rev[booksheet.row(row)[3].value]
#                             else:
#                                 raise Exception

#                             newLine = IP_Table(city= tmpData['city'], ipAddress=tmpData['ipAddress'],
#                                                isOccupied=tmpData['isOccupied'], type=tmpData['type'])
#                             IP_Table.add(IP_Table, newLine)
#                             tmpList.append(tmpData)
#                         return jsonify(common.trueReturn(tmpList, '导入成功！'))
#                 except Exception as e:
#                     print(e)
#                     return jsonify(common.falseReturn('', '导入失败！'))
#     else:
#         return jsonify(common.falseReturn('', 'Error！'))


@api.route('/upload/key-domain', methods=['POST'])
def uploadFileDomain():
    if 'multipart/form-data' in request.content_type:
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if filename.split('.')[-1] != 'xlsx':
                return jsonify(common.falseReturn('', '导入文件类型错误！'))
            else:
                filename = 'domain-' + '%s.xlsx' % str(int(time.time() * 10000000))
                fileFullPath = 'upload/dns/' + filename
                file.save(fileFullPath)
                try:
                    workbook = xlrd.open_workbook(fileFullPath)
                    booksheet = workbook.sheet_by_name('Sheet1')
                    if booksheet.row(0)[0].value != '域名' or booksheet.row(0)[1].value != 'IP':
                        return jsonify(common.falseReturn('', '文件格式不正确！'))
                    else:
                        tmpList = []
                        for row in range(1, booksheet.nrows):
                            tmpData = {}
                            tmpData['domain'] = booksheet.row(row)[0].value
                            tmpData['legal_ip'] = booksheet.row(row)[1].value
                            newLine = Key_Domain(domain= tmpData['domain'], legal_ip=tmpData['legal_ip'])
                            Key_Domain.add(Key_Domain, newLine)
                            tmpList.append(tmpData)
                        return jsonify(common.trueReturn(tmpList, '导入成功！'))
                except Exception as e:
                    print(e)
                    return jsonify(common.falseReturn('', '导入失败！'))
        else:
            return jsonify(common.falseReturn('', 'Error！'))
    else:
        return jsonify(common.falseReturn('', 'Error！'))


@api.route('/upload/domain-list', methods=['POST'])
def uploadFileDomainList():
    if 'multipart/form-data' in request.content_type:
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if filename.split('.')[-1] not in ['xlsx', 'csv']:
                return jsonify(common.falseReturn('', '导入文件类型错误！'))
            elif filename.split('.')[-1] == 'xlsx':
                filename = 'domain_' + '%s.xlsx' % str(int(time.time() * 10000000))
                fileFullPath = 'upload/dns/' + filename
                file.save(fileFullPath)
                try:
                    workbook = xlrd.open_workbook(fileFullPath)
                    booksheet = workbook.sheet_by_name('Sheet1')
                    if booksheet.row(0)[0].value != 'domain' or booksheet.row(0)[1].value != 'tld_plus_two'\
                        or booksheet.row(0)[2].value != 'tld_plus_one' or booksheet.row(0)[3].value != 'like_pattern'\
                        or booksheet.row(0)[4].value != 'regexp_pattern' or booksheet.row(0)[5].value != 'is_focused'\
                        or booksheet.row(0)[6].value != 'category' or booksheet.row(0)[7].value != 'website_name'\
                        or booksheet.row(0)[8].value != 'comment':
                        return jsonify(common.falseReturn('', '文件格式不正确！'))
                    else:
                        tmpList = []
                        for row in range(1, booksheet.nrows):
                            tmpData = {}
                            tmpData['domain'] = booksheet.row(row)[0].value
                            tmpData['tld_plus_two'] = booksheet.row(row)[1].value
                            tmpData['tld_plus_one'] = booksheet.row(row)[2].value
                            tmpData['like_pattern'] = booksheet.row(row)[3].value
                            tmpData['regexp_pattern'] = booksheet.row(row)[4].value
                            tmpData['is_focused'] = booksheet.row(row)[5].value
                            tmpData['category'] = booksheet.row(row)[6].value
                            tmpData['website_name'] = booksheet.row(row)[7].value
                            tmpData['comment'] = booksheet.row(row)[8].value
                            # newLine = Key_Domain(domain= tmpData['domain'], legal_ip=tmpData['legal_ip'])
                            focusDomain = DimFocusedDomain(domain=tmpData['domain'], tld_plus_two=tmpData['tld_plus_two'],
                                tld_plus_one=tmpData['tld_plus_one'], like_pattern=tmpData['like_pattern'],
                                regexp_pattern=tmpData['regexp_pattern'], is_focused=tmpData['is_focused'],
                                category=tmpData['category'], website_name=tmpData['website_name'], comment=tmpData['comment'])
                            db.session.begin()
                            db.session.add(focusDomain)
                            db.session.commit()
                            # Key_Domain.add(Key_Domain, newLine)
                            tmpList.append(tmpData)
                        return jsonify(common.trueReturn(tmpList, '导入成功！'))
                except Exception as e:
                    print(e)
                    return jsonify(common.falseReturn('', '导入失败！'))
            else:
                filename = 'domain_' + '%s.csv' % str(int(time.time() * 10000000))
                fileFullPath = 'upload/dns/' + filename
                file.save(fileFullPath)
                with open(fileFullPath, encoding = "utf-8") as f:
                    readCSV = csv.reader(f, delimiter=',')
                    content = [row for row in readCSV]
                headers = content[0]
                if headers[0] != 'domain' or headers[1] != 'tld_plus_two' or headers[2] != 'tld_plus_one' and headers[3] != 'like_pattern'\
                    or headers[4] != 'regexp_pattern' or headers[5] != 'is_focused' or headers[6] != 'category' \
                    or headers[7] != 'website_name' or headers[8] != 'comment':
                    return jsonify(common.falseReturn('', '文件格式不正确！'))
                else:
                    tmpList = []
                    for row in range(1, len(content)):
                        tmpData = {}
                        tmpData['domain'] = content[row][0]
                        tmpData['tld_plus_two'] = content[row][1]
                        tmpData['tld_plus_one'] = content[row][2]
                        tmpData['like_pattern'] = content[row][3]
                        tmpData['regexp_pattern'] = content[row][4]
                        tmpData['is_focused'] = content[row][5]
                        tmpData['category'] = content[row][6]
                        tmpData['website_name'] = content[row][7]
                        tmpData['comment'] = content[row][8]
                        focusDomain = DimFocusedDomain(domain=tmpData['domain'], tld_plus_two=tmpData['tld_plus_two'],
                            tld_plus_one=tmpData['tld_plus_one'], like_pattern=tmpData['like_pattern'],
                            regexp_pattern=tmpData['regexp_pattern'], is_focused=tmpData['is_focused'],
                            category=tmpData['category'], website_name=tmpData['website_name'], comment=tmpData['comment'])
                        db.session.begin()
                        db.session.add(focusDomain)
                        result = session_commit()
                        if result:
                            result = common.falseReturn('', "导入失败！")
                        else:
                            tmpList.append(tmpData)
                            result = common.trueReturn('', '导入成功！')
                        return jsonify(result)
        else:
            return jsonify(common.falseReturn('', 'Error！'))
    else:
        return jsonify(common.falseReturn('', 'Error！'))