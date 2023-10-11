from flask import Blueprint, render_template, request, current_app
from DB.work_with_db import select_dict
from DB.sql_provider import SQLProvider

import os

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))




@blueprint_query.route('/', methods=['GET', 'POST'])
def query_index():
    if request.method == 'GET':
        return render_template('input_param.html')
    else:
        category = request.form.get('category')  # объект form - словарь, где ключ - название category, извлекается методом get
        sql1 = provider.get('category.sql', category=category)
        category = select_dict(current_app.config['db_config'], sql1)

        price = request.form.get('price')
        sql2 = provider.get('price.sql', price=price)
        price = select_dict(current_app.config['db_config'], sql2)

        product_name = request.form.get('product_name')
        sql3 = provider.get('name.sql', product_name=product_name, price=price)
        product_name = select_dict(current_app.config['db_config'], sql3)


        product_measure = request.form.get('product_measure')
        sql4 = provider.get('measure.sql', product_measure=product_measure)
        product_measure = select_dict(current_app.config['db_config'], sql4)



        prod_title = 'Полученный результат'

        if category:
            return render_template('dynamic.html', products=category, prod_title=prod_title)
        if price:
            return render_template('dynamic.html', products=price, prod_title=prod_title)
        if product_measure:
            return render_template('dynamic.html', products=product_measure, prod_title=prod_title)
        if product_name:
            return render_template('dynamic.html', products=product_name, prod_title=prod_title)

        else:
            return render_template('error.html')
