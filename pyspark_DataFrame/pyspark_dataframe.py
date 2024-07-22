from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark_task2').getOrCreate()

category_table = spark.createDataFrame([
    (1, 'Cat №1'),
    (2, 'cat №2'),
    (3, 'cat №3'),
    (4, 'cat №4'),
    (5, 'cat №5'),
], ['id', 'category_name'])

product_table = spark.createDataFrame([
    (1, 'prod №1'),
    (2, 'prod №2'),
    (3, 'prod №3'),
    (4, 'prod №4'),
    (5, 'prod №5'),
    (6, 'prod №6'),
    (7, 'prod №7 '),
], ['id', 'product_name'])

collection_data = spark.createDataFrame([
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (2, 6),
    (1, 7),
    (2, 1),
], ['category_id', 'product_id'])


query_data = (
    product_table.join(collection_data, product_table.id == collection_data.product_id, how='left').join(category_table,
                                                                                                         category_table.id == collection_data.category_id,
                                                                                                         how='left').select(
        ['category_name', 'product_name']))

query_data.orderBy('category_id', 'product_id').show(truncate=True)
