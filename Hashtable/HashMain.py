import hash_table as ht
import YellowPages as YP
import numpy as np

object1 = YP.YellowPages('An','holly', 'yosemite','555-999-0000')

object2 =  YP.YellowPages('Chad','Holmes' ,'645','000-555-1111')
object3 =  YP.YellowPages('Anna','Ferris' ,'los Angeles','555 555-5555')
object4 =  YP.YellowPages('natasha','kilman' ,'San Diego','666-666-6666')

pair_list =np.array( [(object1.first_name, object1),(object2.first_name, object2)], dtype = object )
hashtable = ht.hashing(pair_list)
hashtable = ht.hashtable_update((object3.first_name, object3),hashtable)
hashtable = ht.hashtable_update((object4.first_name, object4),hashtable)
hashtable = ht.hashtable_update(('2', 46),hashtable)
hashtable = ht.hashtable_update(('11', 76),hashtable)
hashtable = ht.hashtable_update(('9', 11),hashtable)
hashtable = ht.hashtable_update(('87', 144),hashtable)
hashtable = ht.hashtable_update(('34', 54),hashtable)
hashtable = ht.hashtable_update(('30', 87),hashtable)
hashtable = ht.hashtable_update(('76', 123),hashtable)
hashtable = ht.hashtable_update(('100', 908),hashtable)
hashtable = ht.hashtable_update(('67', 46),hashtable)
hashtable = ht.hashtable_update(('22', 76),hashtable)
hashtable = ht.hashtable_update(('33', 11),hashtable)
hashtable = ht.hashtable_update(('69', 144),hashtable)
hashtable = ht.hashtable_update(('45', 54),hashtable)
hashtable = ht.hashtable_update(('700', 87),hashtable)
hashtable = ht.hashtable_update(('322', 123),hashtable)
hashtable = ht.hashtable_update(('666', 908),hashtable)

print(ht.hashtable_lookup('9', hashtable))
print(ht.hashtable_lookup('87', hashtable))
print(ht.hashtable_lookup(object1.first_name, hashtable).email())
