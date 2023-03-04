import xmlrpc.client

url = 'http://localhost:8085'
db = 'Odoo'
username = 'son'
password = 1

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})
print(uid)

# uid = common.authenticate(db, username, password, {})
# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# products = models.execute_kw(db, uid, password, 'product.template', 'search', [[]])
