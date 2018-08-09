from flask_restful import Resource, reqparse

from app.models import db, IP_Table

dict_is_occupied = {1: '占用', 0: '空闲'}
dict_type = {0: '互联地址', 1: 'Loopback地址'}

dict_is_occupied_rev = {'占用': 1, '空闲': 0}
dict_type_rev = {'互联地址': 0, 'Loopback地址': 1}


class TableApi(Resource):

    def get(self):
        all_query = db.session.query(IP_Table.id, IP_Table.city, IP_Table.ipAddress,
                                     IP_Table.isOccupied, IP_Table.type).all()
        res_list = []
        for query in all_query:
            id = query[0]
            city = query[1]
            ipAddress = query[2]
            isOccupied = query[3]
            type = query[4]
            if isOccupied in dict_is_occupied.keys():
                isOccupied = dict_is_occupied[isOccupied]
            if type in dict_type.keys():
                type = dict_type[type]
            tmp_dict = {"id": id, "city": city, "ipAddress": ipAddress, "isOccupied": isOccupied, "type": type}
            # res_dict = dict(res_dict, **tmp_dict)
            res_list.append(tmp_dict)
        return res_list
        # res_dict = {
        #     "msg":"OK",
        #     "data": res_list
        # }
        # return res_dict

    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('city', type=str)
        parser.add_argument('ipAddress', type=str)
        parser.add_argument('isOccupied', type=str)
        parser.add_argument('type', type=str)
        args = parser.parse_args()

        query = IP_Table.query.filter_by(id=id).first()
        if query:
            try:
                if args["city"] and args["isOccupied"] and args["ipAddress"] and args["type"]:
                    query.city = args["city"]
                    query.ipAddress = args["ipAddress"]
                    if args["isOccupied"] in dict_is_occupied_rev.keys():
                        query.isOccupied = dict_is_occupied_rev[args["isOccupied"]]
                    if args["type"] in dict_type_rev.keys():
                        query.type = dict_type_rev[args["type"]]
                    db.session.commit()
                    return {"msg": 0}
                else:
                    return {"msg": 1}
            except:
                return {"msg": 2}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('action', type=int, required=True)
        parser.add_argument('city', type=str)
        parser.add_argument('ipAddress', type=str)
        parser.add_argument('isOccupied', type=str)
        parser.add_argument('type', type=str)
        args = parser.parse_args()
        try:
            if args['action'] == 1:
                if args["city"] and args["ipAddress"] and args["isOccupied"] and args["type"]:
                    if args["isOccupied"] in dict_is_occupied_rev.keys():
                        isOccupied = dict_is_occupied_rev[args["isOccupied"]]
                    if args["type"] in dict_type_rev.keys():
                        type = dict_type_rev[args["type"]]
                    newLine = IP_Table(city=args["city"], ipAddress=args["ipAddress"], isOccupied=isOccupied,
                                       type=type)
                    db.session.add(newLine)
                    db.session.commit()
                    return {"msg": 0}
                else:
                    return {"msg": 1}
            elif args['action'] == 2:
                if args["type"] in dict_type_rev.keys():
                    type = dict_type_rev[args["type"]]
                else:
                    type = ''
                if args["isOccupied"] in dict_is_occupied_rev.keys():
                    isOccupied = dict_is_occupied_rev[args["isOccupied"]]
                else:
                    isOccupied = ''
                if args['ipAddress']:
                    ipAddress = args['ipAddress'].strip()
                else:
                    ipAddress = ''

                all_query = db.session.query(IP_Table.id, IP_Table.city, IP_Table.ipAddress,
                                     IP_Table.isOccupied, IP_Table.type)\
                    .filter(IP_Table.city.like('%' + args['city'] + '%'))\
                    .filter(IP_Table.isOccupied.like('%' + str(isOccupied) + '%'))\
                    .filter(IP_Table.type.like('%' + str(type) + '%'))\
                    .filter(IP_Table.ipAddress.like('%' + ipAddress + '%')).all()
                res_list = []
                for query in all_query:
                    id = query[0]
                    city = query[1]
                    ipAddress = query[2]
                    isOccupied = query[3]
                    type = query[4]
                    if isOccupied in dict_is_occupied.keys():
                        isOccupied = dict_is_occupied[isOccupied]
                    if type in dict_type.keys():
                        type = dict_type[type]
                    tmp_dict = {"id": id, "city": city, "ipAddress": ipAddress, "isOccupied": isOccupied, "type": type}
                    res_list.append(tmp_dict)
                return res_list

            else:
                return {"msg": 1}
        except:
            return {"msg": 2}

    def delete(self, id):
        try:
            selectLine = IP_Table.query.filter_by(id=id).first()
            db.session.delete(selectLine)
            db.session.commit()
            return {"msg": 0}
        except:
            return {"msg": 1}