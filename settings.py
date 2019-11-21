# Setting Proxy (KN Only)
prx_user = 'rudolf.wolter'
prx_pwd = 'C3t3d3s3!'
proxies = {
    "http": "http://{}:{}@kn.proxy.int.kn:80".format(prx_user, prx_pwd),
    "https": "http://{}:{}@kn.proxy.int.kn:80".format(prx_user, prx_pwd)
}

# Files
resources_file = 'db/resources.csv'
craftables_file = 'db/craftables.csv'
dict_resources = 'db/resources.dict'
dict_commons = 'db/commons.dict'
dict_rares = 'db/rares.dict'
dict_epics = 'db/epics.dict'
dict_legendaries = 'db/legendaries.dict'
dict_relics = 'db/relics.dict'
