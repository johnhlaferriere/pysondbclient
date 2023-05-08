

from pysondb.client import PysonDBClient
import uuid

HOST, PORT = "localhost", 9999


generator = "lambda: str(uuid.uuid4())"
#generator = "lambda x: x['first'] == 'Bill'"

def main() -> int:

    #f = eval(generator)
    #print (f())
    #return 0
    s = PysonDBClient(HOST, PORT)
    s.connect()
    ok = True
    while ok:
        print('?: ')
        data = input()
        if len(data) > 0:

            ok = data != "done"
            if ok:
                #s.create_db("testfile3",True,True)
                #print(s.add_section("test2"))
                s.use_db("testfile3","test2")
                #s.use_section("test2")
                #print(s.add_new_key("first"))
                #print(s.add_new_key("last"))
                print (s.set_id_generator(generator))
                print(s.add({"first":"Bill","last":"Smith"}))
                print(s.add({"first":"Bill","last":"Davis"}))
                print(s.add({"first":"Bill","last":"Harrison"}))
                print (s.update_by_query(query = "lambda x: x['first'] == 'Bill'",new_data = {'last':'Nye'}))
                print (s.get_by_query(query = "lambda x: x['first'] == 'Bill'"))
                print (s.delete_by_query(query = "lambda x: x['first'] == 'Bill'"))
    s.close()

if __name__ == "__main__":
    main()


"""

{
    "version": 2,
    "keys": {
        "test2": [
            "first",
            "last"
        ]
    },
    "test2": {
        "263512584592280692": {
            "first": "Bill",
            "last": "Nye"
        },
        "150640287217051014": {
            "first": "Bill",
            "last": "Nye"
        },
        "846464917529999116": {
            "first": "Bill",
            "last": "Nye"
        },
        "301532115955613905": {
            "first": "Bill",
            "last": "Nye"
        },
        "812041525185350293": {
            "first": "Bill",
            "last": "Nye"
        }
    }
}


"""
